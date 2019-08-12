from coderedcms.blocks import base_blocks, html_blocks
from django.test import SimpleTestCase

from wagtail.tests.utils import WagtailTestUtils

from coderedcms.settings import cr_settings


class TestMultiSelectBlock(WagtailTestUtils, SimpleTestCase):
    def test_render_single_choice(self):
        block = base_blocks.MultiSelectBlock(
            choices=[('tea', 'Tea'), ('coffee', 'Coffee'), ('water', 'Water')])
        html = block.render_form(['tea'])
        self.assertInHTML('<option value="tea" selected>Tea</option>', html)
        self.assertTrue(html.count('selected'), 1)

    def test_render_multi_choice(self):
        block = base_blocks.MultiSelectBlock(
            choices=[('tea', 'Tea'), ('coffee', 'Coffee'), ('water', 'Water')])
        html = block.render_form(['coffee', 'tea'])
        self.assertInHTML('<option value="tea" selected>Tea</option>', html)
        self.assertInHTML('<option value="coffee" selected>Coffee</option>', html)
        self.assertTrue(html.count('selected'), 2)


# class TestHeaderBlocks(WagtailTestUtils, SimpleTestCase):
#     def test_h1_block(self):
#         block = html_blocks.H1Block(text='Test Header')
#         html = block.render_form('Test Header')


class TestButtonBlock(WagtailTestUtils, SimpleTestCase):
    def test_render_button_block(self):
        block = html_blocks.ButtonBlock(other_link='https://coderedcorp.com', button_title='Go To Codered')
        value = {'settings': {'custom_template': block.child_blocks['settings'].child_blocks['custom_template']._constructor_args[1]['choices'][0][0]}}
        html = block.render(value)
        print(html)
        self.assertInHTML('<a href="{}"'.format('https://coderedcorp.com'), html)
