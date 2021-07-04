from django.shortcuts import render, get_object_or_404, redirect
from .models import crudapp
from .forms import PostForm
# Create your views here.
def home(request):
    crudapps = crudapp.objects
    return render(request, 'home.html', {'crudapps':crudapps})

def detail(request, crudapp_id):
    crudapp_detail = get_object_or_404(crudapp, pk=crudapp_id)
    return render(request, 'detail.html', {'crudapp':crudapp_detail})

def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form':form})

def edit(request):
    return render(request, 'edit.html')

def postupdate(request, crudapp_id):
    post = get_object_or_404(crudapp, pk=crudapp_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', crudapp_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def postdelete(request, crudapp_id):
    post = get_object_or_404(crudapp, pk=crudapp_id)
    post.delete()
    return redirect('home')
