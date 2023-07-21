from django.shortcuts import redirect, render
from .models import Blog
from .forms import BlogForm
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    # return HttpResponse("Hello, This is Bishal's Project")
    blog = Blog.objects.all() 
    return render(request,"crud/index.html",{"Blogs":blog})


def create(request):
    forms = BlogForm(request.POST or None)
    if(forms.is_valid()):
        forms.save()
        return redirect("home")
    return render(request, "crud/create.html",{"forms":forms})