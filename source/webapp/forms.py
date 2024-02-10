from django import forms
from webapp.models import Advert, Comment


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        exclude = ('author', 'advert_status', 'created', 'published', 'updated')
        widgets = {'advert_category': forms.Select}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('author', 'advert')