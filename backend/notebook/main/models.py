from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=150)
    descr = models.TextField(max_length=350)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title