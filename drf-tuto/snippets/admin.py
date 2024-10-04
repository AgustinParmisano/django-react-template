from django.contrib import admin
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ['created','title','code','linenos','language','style']

admin.site.register(Snippet, SnippetAdmin)