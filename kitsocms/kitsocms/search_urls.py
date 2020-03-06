from django.urls import re_path
from kitsocms.views import search

urlpatterns = [
    re_path(r'', search, name='codered_search'),
]
