from django.db import models

# Create your models here.

class Todo_bord(models.Model):
    new_message = models.CharField(max_length=200,)
    image_url = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True,)
