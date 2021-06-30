from django import forms


class AddStudentForm(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    age = forms.CharField(max_length=20)


class SearchStudentForm(forms.Form):
    name = forms.CharField(max_length=20)


class UpdateStudentForm(forms.Form):
    old_name = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    age = forms.CharField(max_length=20)


class DeleteStudentForm(forms.Form):
    name = forms.CharField(max_length=20)
