from django import forms

class NameForm(forms.Form):
    #firstname = forms.CharField(label='u42_div', max_length=100)
    pas = forms.CharField(max_length=100)


#lass NameForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    #passw = forms.CharField(label='passw', max_lenght=100)