from django.shortcuts import render
from .models import toDoItem

# Create your views here.
def post_list(request):
    list = toDoItem.objects.all()
    return render(request,'toDo/post_list.html',{'list':list})

def post_edit(request):
    return render(request,'toDo/post_edit.html')
