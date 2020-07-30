from django import forms
class register1(forms.Form):
    firstname = forms.CharField(max_length=150)
    lastname = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField(max_length=150)
    email = forms.CharField(max_length=150)
    address = forms.CharField(max_length=150)

class login(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

class order1(forms.Form):
    it_quantity = forms.IntegerField()

