from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'email', 'status', ]
        widgets = {
            'title': forms.TextInput(attrs={'font-size': '2rem',
                                            'color': '#246rdf'}),
        }
