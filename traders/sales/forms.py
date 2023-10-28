from django import forms
from .models import Trader, Tracker, CustomUser, MyUserModel

class TraderForm(forms.ModelForm):
    class Meta:
        model = Trader
        fields = '__all__'

class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = '__all__'

class UserForm(forms.Form):
    firstname = forms.CharField(required=True, max_length=200)
    lastname = forms.CharField(required=True, max_length=200)
    username = forms.CharField(required=True, max_length=200)
    email = forms.EmailField(required=False, max_length=200)
    password = forms.CharField(widget=forms.PasswordInput, max_length=200, required=True)

    def save(self, commit=True):
        user = CustomUser.objects.create(
            first_name=self.cleaned_data['firstname'],
            last_name=self.cleaned_data['lastname'],
            username=self.cleaned_data['username'],
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data['password']
        )

        if commit:
            user.save()
        return user

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = MyUserModel
        fields = '__all__'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])  # Assuming you are using Django's built-in password hashing
        if commit:
            user.save()
        return user
