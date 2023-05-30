from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

    content = forms.CharField(label='Post', max_length=200, widget=forms.Textarea(attrs={
        'class': 'textbox',
        'placeholder': 'Write A Post',
        'rows': 3,
        })
    )
