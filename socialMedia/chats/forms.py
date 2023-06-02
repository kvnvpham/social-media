from django import forms


from .models import ChatMessages


class MessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessages
        fields = ['content']

    content = forms.CharField(label='Message', max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Write Message'
    }))