from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
        required=True)

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
        required=True)

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=75)

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'email', 'password', 'confirm_password',]

    def __int__(self, *args, **kwargs):
        super(SignupForm, self).__int__(*args, **kwargs)


    def clean(self):
        super(SignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and password != confirm_password:
            self.errors['password'] = self.error_class(
                ['Password don\'t  match']
            )
        return self.cleaned_data
