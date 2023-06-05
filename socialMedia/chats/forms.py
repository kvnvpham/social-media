from django import forms

from .models import ChatMessages


class MessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessages
        fields = ['content']

    content = forms.CharField(label='Message', max_length=150, widget=forms.Textarea(attrs={
        'class': 'write-message',
        'placeholder': 'Write Message',
        'rows': 2,
    }))