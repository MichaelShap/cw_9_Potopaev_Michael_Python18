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


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
