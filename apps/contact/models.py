from django.db import models


class  Contact(models.Model):
    full_name=models.CharField(max_length=222)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return self.full_name


# Create your models here.
