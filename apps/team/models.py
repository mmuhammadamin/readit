from django.db import models

# Create your models here.
class TeamModel(models.Model):


    image = models.ImageField(upload_to='team/')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    content1 = models.TextField(max_length=100)
    content2 = models.TextField(max_length=100)
    content3 = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class ClientModel(models.Model):
    content=models.CharField(max_length=150)
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    image=models.ImageField(upload_to='clients/')