from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from .models import Category, Topic, Idea
# Register your models here.
admin.site.site_header = "Manage Topic"

class TopicAdmin(admin.ModelAdmin):
    Fieldset = [
        (None, {'fields':['title','closure_date','final_closure_date']})
    ]
    inlines = [Idea]
admin.site.register(Topic)
admin.site.register(Idea)
admin.site.register(Category)