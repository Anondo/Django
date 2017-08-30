from django import forms



class StudentForm(forms.Form):
    name = forms.CharField(max_length = 180)
    program = forms.CharField(max_length = 80)
    year = forms.IntegerField()
    cgpa = forms.FloatField()
