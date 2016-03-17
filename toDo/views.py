from django.shortcuts import render, get_object_or_404
from .models import toDoItem

# Create your views here.
def post_list(request):
    list = toDoItem.objects.all()
    return render(request,'toDo/post_list.html',{'list':list})

def post_edit(request, pk):
    post = get_object_or_404(toDoItem, pk=pk)
    return render(request,'toDo/post_edit.html',{'post':post})
