from django.db import models


class Timestamp(models.Model):
    crated_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Tag(Timestamp):
    tag=models.CharField(max_length=50)
    def __str__(self):
        return self.tag
class Category(models.Model):
    title=models.CharField(max_length=100)


    def __str__(self):
        return self.title


class Post(Timestamp):
    image=models.ImageField(upload_to='posts',null=True)
    title=models.CharField(max_length=100)
    tag=models.ManyToManyField(Tag,blank=True)
    category=models.ForeignKey(Category,blank=True,on_delete=models.CASCADE)
    content=models.TextField(max_length=500)
    slug=models.SlugField()


    def __str__(self):
        return self.title


class Comment(Timestamp):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=222)
    message=models.TextField()
    def __str__(self):
        return self.full_name
