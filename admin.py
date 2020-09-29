from django.contrib import admin
from quizapp.models import Question, Choice

# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)

