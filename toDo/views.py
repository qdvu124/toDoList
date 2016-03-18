from django.shortcuts import render, get_object_or_404
from .models import ToDoItem, User
from .forms import EditTask, LoginForm
from django.shortcuts import redirect
from django.utils import timezone
import logging
from django.views.decorators.cache import never_cache

# Create your views here.
logger = logging.getLogger(__name__)

@never_cache
def post_list(request):
    if request.session.get('user_id', None) is None:
        return redirect('login')
    list = ToDoItem.objects.filter(user_id=request.session.get('user_id', None))
    return render(request, 'toDo/post_list.html', {'list': list, 'time': timezone.localtime(timezone.now())})


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

@never_cache
def log_in(request):
    if request.session.get('user_id', None) is not None:
        return redirect('post_list')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if request.POST['Button'] == 'Register':
            if form.is_valid():
                username = form.cleaned_data['username']


                userlist = User.objects.filter(username=username)

                if userlist.count() == 0:
                    form.save()
                    return redirect('post_list')
        else:
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                request.session['username'] = username
                logger.error(request.session.session_key)
                logger.error(request.session['username'])
                user = get_object_or_404(User, username=username)
                if password != user.password:
                    form = LoginForm()
                    return render(request, 'toDo/login.html', {'form': form})
                request.session['user_id'] = user.pk
                request.session.set_expiry(15)
                return redirect('post_list')
    form = LoginForm()
    return render(request, 'toDo/login.html', {'form': form})

@never_cache
def log_out(request):
    request.session.clear()
    # del request.session['user_id']
    return redirect('login')