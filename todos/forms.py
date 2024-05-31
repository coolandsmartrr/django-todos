from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
  class Meta:
    model = Todo
    fields = ['task', 'is_done']