from django import forms

from .models import Task

from django.contrib.auth.forms import (
    AuthenticationForm
)

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'limit_date','is_completed')
