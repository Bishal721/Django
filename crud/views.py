from django.shortcuts import redirect, render
from .models import Blog, Contact
from .forms import BlogForm
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    # return HttpResponse("Hello, This is Bishal's Project")
    blog = Blog.objects.all()
    data = request.GET.get("search")
    if data != "" and data is not None:
        searchData = Blog.objects.filter(title__contains=data)
        print(searchData)
        return render(request,"crud/index.html",{"blog":searchData})
    return render(request,"crud/index.html",{"Blogs":blog})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        crud = Contact(
            name = name,
            email= email,
            message = message
        )
        crud.save()
        print(crud)
        return redirect("crud:home")


    return render(request,"crud/contact.html")

def particularData(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,"crud/post.html",{"blog":blog})

def create(request):
    forms = BlogForm(request.POST or None)
    print(forms)
    if(forms.is_valid()):
        forms.save()
        return redirect("crud:home")
    return render(request, "crud/create.html")

def deleteData(request,id):
    deldata = Blog.objects.get(id=id)   
    deldata.delete()
    return redirect('crud:home')


def updateData(request,id):
    blog = Blog.objects.get(id=id)
    forms = BlogForm(request.POST or None,instance=blog)
    context = {
        "forms":forms,
        "title":blog.title,
        "subtitle":blog.subtitle,
        "description":blog.description
    }
    if forms.is_valid():
        forms.save()
        return redirect("crud:home")
    return render(request, "crud/create.html",context)

def aboutus(request):
    return render(request,"crud/about.html")
