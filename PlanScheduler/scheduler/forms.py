from django import forms

class NameForm(forms.Form):
    #firstname = forms.CharField(label='u42_div', max_length=100)
    pas = forms.CharField(max_length=100)


#lass NameForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    #passw = forms.CharField(label='passw', max_lenght=100)

#User forms

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    rePassword = forms.CharField()

class ChangePassword(forms.Form):
    currPass = forms.CharField(max_length=100)
    newPass = forms.CharField()
    newRePass = forms.CharField()

class LoginData(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

#Filling data forms

class PlanNameForm(forms.Form):
    planName = forms.CharField(max_length=60)

class AddTime(forms.Form):
    className = forms.CharField()

class AddTeacher(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    # = forms.CharField()
    #password = forms.CharField()
    maxWeeklyHours = forms.Form()
    minWeeklyHours = forms.Form()

