from django.db import models


class Basket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.FileField(upload_to='uploads')
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.title
