from django.contrib import admin
from .models import Post, AnonymousPost
# Register your models here.
admin.site.register(Post)
admin.site.register(AnonymousPost)