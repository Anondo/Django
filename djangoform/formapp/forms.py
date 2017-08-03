from django import forms

#create your forms here

class PersonForm(forms.Form):
    name = forms.CharField(label = "Enter Your Name" , max_length=180)
    email = forms.EmailField(label = "Enter Your Email")
    age = forms.IntegerField(label = "Enter Your Age")
