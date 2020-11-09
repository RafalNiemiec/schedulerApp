from django import forms

class NameForm(forms.Form):
    pas = forms.CharField(max_length=100)
    username = forms.CharField(label='username', max_length=100)

#User forms
class LoginData(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, min_length=8,
                               help_text='Min 8 characters')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, min_length=8,
                               help_text='Min 8 characters')
    rePassword = forms.CharField(max_length=30, min_length=8,
                                 help_text='Min 8 characters')

class ChangePassword(forms.Form):
    currPass = forms.CharField(max_length=30)
    newPass = forms.CharField(max_length=30, min_length=8,
                              help_text='Min 8 characters')
    newRePass = forms.CharField(max_length=30, min_length=8,
                                help_text='Min 8 characters')


#Filling data forms
class PlanNameForm(forms.Form):
    planName = forms.CharField(max_length=30)

class AddTimeForm(forms.Form):
    className = forms.CharField(max_length=30)

class AddClassesForm(forms.Form):
    groupName = forms.CharField(initial='Group Name', max_length=60, help_text='max 60 characters',
                                error_messages={'required': 'Please insert data'})
class AddTeacherForm(forms.Form):
    name = forms.CharField(initial='Name', max_length=30, help_text='max 60 characters',
                           error_messages={'required': 'Please insert data'})
    surname = forms.CharField(initial='Surname', max_length=30, help_text='max 100 characters',
                              error_messages={'required': 'Please insert data'})
    #maxWeeklyHours = forms.Form()
    #minWeeklyHours = forms.Form()

class AddLessonForm(forms.Form):
    lessonName = forms.CharField(initial='Lesson name', max_length=60, help_text='max 60 characters',
                                 error_messages={'required': 'Please insert data'})

class AddClassroomForm(forms.Form):
    classroomName = forms.CharField(initial='Classroom name', max_length=15, help_text='max 60 characters',
                                 error_messages={'required': 'Please insert data'})
