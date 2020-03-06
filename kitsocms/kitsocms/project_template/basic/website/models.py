"""
Createable pages used in Kitso CMS.
"""
from modelcluster.fields import ParentalKey
from kitsocms.forms import KitsoFormField
from kitsocms.models import (
    KitsoArticlePage,
    KitsoArticleIndexPage,
    KitsoEmail,
    KitsoFormPage,
    KitsoWebPage
)


class ArticlePage(KitsoArticlePage):
    """
    Article, suitable for news or blog content.
    """
    class Meta:
        verbose_name = 'Article'
        ordering = ['-first_published_at', ]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ['website.ArticleIndexPage']

    template = 'kitsocms/pages/article_page.html'
    amp_template = 'kitsocms/pages/article_page.amp.html'
    search_template = 'kitsocms/pages/article_page.search.html'


class ArticleIndexPage(KitsoArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """
    class Meta:
        verbose_name = 'Article Landing Page'

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = 'website.ArticlePage'

    # Only allow ArticlePages beneath this page.
    subpage_types = ['website.ArticlePage']

    template = 'kitsocms/pages/article_index_page.html'


class FormPage(KitsoFormPage):
    """
    A page with an html <form>.
    """
    class Meta:
        verbose_name = 'Form'

    template = 'kitsocms/pages/form_page.html'


class FormPageField(KitsoFormField):
    """
    A field that links to a FormPage.
    """
    class Meta:
        ordering = ['sort_order']

    page = ParentalKey('FormPage', related_name='form_fields')


class FormConfirmEmail(KitsoEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """
    page = ParentalKey('FormPage', related_name='confirmation_emails')


class WebPage(KitsoWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    Template renders all Navbar and Footer snippets in existance.
    """
    class Meta:
        verbose_name = 'Web Page'

    template = 'kitsocms/pages/web_page.html'
