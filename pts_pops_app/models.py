from django.db import models

# Create your models here.

class Post(models.Model):
    comments = models.TextField()
    picture = models.ImageField(default=None, upload_to='uploaded_img', blank=True)
    date_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comments}'