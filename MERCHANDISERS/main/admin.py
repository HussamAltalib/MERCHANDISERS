from django.contrib import admin
from .models import Question, Answer

# Register your models here.

#to customize the panel
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'asked_at')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question')
    list_filter = ('question',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

