from django import forms
from durationwidget.widgets import TimeDurationWidget
from lesoon_4.models import Client

class MyForm(forms.Form):
    name = forms.CharField(label="User name", initial="User name", disabled=True)
    profile_picture = forms.ImageField(widget=forms.FileInput)
    email = forms.EmailField(error_messages={'required' : "Please fill this field! "})
    password = forms.CharField(max_length=20, min_length=10, widget=forms.PasswordInput())
    age = forms.IntegerField(required=False, help_text="Enter your current age")
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(initial=10.1)
    birthday = forms.DateField(widget=forms.SelectDateWidget)
    # work_experience = forms.DurationField(widget=TimeDurationWidget(), required=False)
    gender = forms.ChoiceField(choices=[("1","man"),("2","woman")])

class FormFromModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'second_email']
