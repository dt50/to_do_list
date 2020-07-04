from django import forms
from .models import MyUser


class CustomUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.CharField(label='Username', max_length = 20)
    telegram = forms.CharField(label='Telegram nickname', max_length=20)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'telegram')


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'telegram')
