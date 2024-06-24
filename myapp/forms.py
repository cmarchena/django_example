# myapp/forms.py

from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        def clean_title(self):
            title = self.cleaned_data.get('title')
            if not title:
                raise forms.ValidationError('This field is required.')
            if len(title) < 5:
                raise forms.ValidationError('Title must be at least 5 characters long.')
            return title
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']