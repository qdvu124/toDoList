from django.shortcuts import render, get_object_or_404
from .models import ToDoItem, User
from .forms import EditTask, LoginForm
from django.shortcuts import redirect
from django.utils import timezone
import logging

# Create your views here.
logger = logging.getLogger(__name__)

def post_list(request, username):
    list = ToDoItem.objects.filter(username=username)
    return render(request, 'toDo/post_list.html', {'list': list, 'time':timezone.localtime(timezone.now())})


def post_edit(request, pk):
    post = get_object_or_404(ToDoItem, pk=pk)
    return render(request, 'toDo/post_edit.html', {'post': post})


def post_delete(request, pk):
    post = get_object_or_404(ToDoItem, pk=pk)
    if request.method == "POST":
        post.isCompleted = not post.isCompleted
        post.save()
    return redirect('post_list')


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
    post = get_object_or_404(ToDoItem, pk=pk)
    if request.method == "POST":
        form = EditTask(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = EditTask(instance=post)
    return render(request, 'toDo/post_edit.html', {'form': form})


def log_in(request):
    logger.error("Hey")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if request.POST['Login'] == "Login":
            logger.error("Logged in")
            if form.is_valid():
                user = form.save()
                username = form.fields['username']
        else:
            if form.is_valid():
                username = form.fields['username']
        return render(request, 'toDo/post_list.html', {'username': username})
    form = LoginForm()
    return render(request, 'toDo/login.html', {'form': form})
