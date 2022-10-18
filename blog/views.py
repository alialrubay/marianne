from django.shortcuts import render ,  redirect
from .models import *

# Create your views here.
def admin(request):
    response = redirect('admin')
    return response

def home_page(request):
    my_photo = MyPhoto.objects.all()
    book_photo = BookPhoto.objects.all()
    pictures = Pictures.objects.all()
    context = {'pictures':pictures,
                'my_photo':my_photo,
                'book_photo':book_photo,
                
                 }
    return render(request,'home_page.html',context)


# display pictures
def display_pictures(request):  
    pictures = Pictures.objects.all()
    book_photo = BookPhoto.objects.all()
    return render(request , 'pictures.html',{'pictures':pictures,'book_photo':book_photo})


# aboit me
def about(request):  
    my_photo = MyPhoto.objects.all()
    return render(request , 'about.html',{'my_photo':my_photo})