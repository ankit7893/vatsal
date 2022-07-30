
from django.http import HttpResponse
from django.shortcuts import render

from .models import Image
from .forms import ImageForm


def index(request):
    if request.method == "POST":
        form  = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()  
     
    form  = ImageForm() 
    imgs = Image.objects.all()  
    return render(request , 'enroll/index.html' , {'fm':form , 'imgs':imgs})


