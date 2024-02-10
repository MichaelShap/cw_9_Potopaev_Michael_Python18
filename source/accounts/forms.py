from .models import User
from django import forms


class MyUserCreationForm(forms.ModelForm):
    password_confirm = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'}
            )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'password_confirm')

    def clean(self):
        cleaned_data = super(MyUserCreationForm, self).clean()
        if not cleaned_data.get('password_confirm') == cleaned_data.get('password'):
            self.add_error('password_confirm', 'Password does not match.')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
