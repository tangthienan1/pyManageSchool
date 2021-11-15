from django.contrib import admin
from django.http import HttpResponse
import csv
from django.contrib.admin.decorators import action
from django.contrib.admin.helpers import Fieldset
from .models import Category, Comment, Topic, Idea
# Register your models here.
admin.site.site_header = "Manage Topic"
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class TopicAdmin(admin.ModelAdmin):
    fieldset = [
        (None, {'fields':['title']}),
        ('Date information', {'fields':['closure_date','final_closure_date']})
    ]
    inline = [Comment]


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class IdeaAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv"]
    inlines = [CommentInline]



admin.site.register(Topic, TopicAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Category)