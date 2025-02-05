from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogapp.forms import BlogForm
from blogapp.models import Blogs

# Create your views here.
def blogsite(request):
    if request.method == "POST":
        form= BlogForm(request.POST)
        print("Execute")
        if form.is_valid():
            print("Valid")
            try:
                print("trying")
                form.save()
                print("saved")
                return redirect('/show')
            except:
                pass
    else:
        print("staff")
        form = BlogForm()
        
    # template = loader.get_template('sign_up.html')
    # return HttpResponse(template.render())
    return render(request,'blogsite.html',{'form':form})

def show(request):
    Blog_Table=Blogs.objects.all()
    return render(request,"show.html",{'Blogs':Blog_Table})

def edit(request,id):
    Blog_Table = Blogs.objects.get(id=id)
    print(Blog_Table)
    return render(request,"edit.html",{'Blogs':Blog_Table})

def update(request,id):
    Blog_Table =Blogs.objects.get(id=id)
    form =BlogForm(request.POST,instance= Blog_Table)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"edit.html",{'Blogs':Blog_Table})

def destroy(request,id):
    Blog_Table = Blogs.objects.get(id=id)
    print(Blog_Table)
    Blog_Table.delete()
    return redirect("/show")
        
