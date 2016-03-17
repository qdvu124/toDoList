from django.shortcuts import render, get_object_or_404
from .models import toDoItem
from .forms import EditTask
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    list = toDoItem.objects.all()
    return render(request,'toDo/post_list.html',{'list':list})

def post_edit(request, pk):
    post = get_object_or_404(toDoItem, pk=pk)
    return render(request,'toDo/post_edit.html',{'post':post})

def post_detail(request, pk):
    post = get_object_or_404(toDoItem, pk=pk)
    return render(request,'toDo/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = EditTask(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = EditTask()
    return render(request, 'toDo/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(toDoItem, pk=pk)
    if request.method == "POST":
        form = EditTask(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = EditTask(instance=post)
    return render(request, 'toDo/post_edit.html', {'form': form})