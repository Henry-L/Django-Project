from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['publication_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'publication_date', 'was_published_recently')

    list_filter = ['publication_date']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
