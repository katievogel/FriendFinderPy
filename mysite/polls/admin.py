from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    # admin.StackedInline creates individual sections
    # admin.TabularInline creates a table-like format
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    # below is more useful for many fields
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    # search_fields uses 'LIKE' query, so best to keep num of fields limited
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)




