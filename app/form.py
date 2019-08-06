from django import forms


class PostForm(forms.Form):
    author = forms.CharField(max_length=100, required=True)
    title = forms.CharField(max_length=100, required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
