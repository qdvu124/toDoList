from django.shortcuts import render, get_object_or_404
from .models import toDoItem
from .forms import EditTask
from django.shortcuts import redirect
import logging

# Create your views here.
logger = logging.getLogger("view")
LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
logging.debug('This message should go to the log file')


def post_list(request):
    list = toDoItem.objects.order_by('deadline')
    return render(request, 'toDo/post_list.html', {'list': list})


def post_edit(request, pk):
    post = get_object_or_404(toDoItem, pk=pk)
    return render(request, 'toDo/post_edit.html', {'post': post})


def post_delete(request, pk):
    post = get_object_or_404(toDoItem, pk=pk)
    if request.method == "POST":
        post.isCompleted = True
        post.save()
        if (post.isCompleted):
            logger.error("Hey")
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
    post = get_object_or_404(toDoItem, pk=pk)
    if request.method == "POST":
        form = EditTask(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = EditTask(instance=post)
    return render(request, 'toDo/post_edit.html', {'form': form})
