from django import forms
from django.contrib.admin import widgets
from .models import ToDoItem, User


class EditTask(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('task', 'deadline',)

    def __init__(self, *args, **kwargs):
        super(EditTask, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget = widgets.AdminDateWidget()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
