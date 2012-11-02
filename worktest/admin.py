from worktest.models import Question, Answer
from django.contrib import admin


class AnswerAdmin(admin.ModelAdmin):
    pass

class AnswerInline(admin.TabularInline):
    model = Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]


    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
