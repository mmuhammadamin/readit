from django.shortcuts import render
from .models import TeamModel,ClientModel
from apps.articles.models import Post
# Create your views here.
def team_view(request):
    about=TeamModel.objects.all()
    client = ClientModel.objects.all()
    blogs1=Post.objects.all().order_by('-id')[:2]


    ctx={
        'about':about,
        'client': client,
        'blogs1':blogs1

    }

    return render(request,'about.html',ctx)

