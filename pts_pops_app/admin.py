from django.contrib import admin
from .models import Post, Feedback, Question, Choice
# Register your models here.
admin.site.register(Post)
admin.site.register(Feedback)
admin.site.register(Question)
admin.site.register(Choice)