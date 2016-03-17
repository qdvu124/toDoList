from django import forms

from .models import toDoItem

class EditTask(forms.ModelForm):

    class Meta:
        model = toDoItem
        fields = ('task', 'deadline',)