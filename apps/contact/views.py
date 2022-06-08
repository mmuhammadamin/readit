from django.shortcuts import render, redirect

# Create your views here.
from apps.contact.forms import ContactForm
from apps.contact.models import Contact


def contact_view(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('/contact/')

    ctx={
        'form':form
    }
    return render(request,'contact.html',context=ctx)