from django.contrib import admin
from .models import Article

admin.site.site_header = 'Rest Framework Practice'

admin.site.register(Article)