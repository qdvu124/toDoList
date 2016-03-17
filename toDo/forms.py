from django import forms
from django.contrib.admin import widgets
from .models import toDoItem


class EditTask(forms.ModelForm):
    class Meta:
        model = toDoItem
        fields = ('task', 'deadline',)

    def __init__(self, *args, **kwargs):
        super(EditTask, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget = widgets.AdminDateWidget()
