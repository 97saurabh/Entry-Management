from django import forms
from myapp.models import Host,Visitor


class HostForm(forms.ModelForm):
    #meta class is used to directly take entry of a form to given models
    class Meta():
        model=Host
        fields=('host_name','email','phone_no')

class VisitorForm(forms.ModelForm):
    #meta class is used to directly take entry of a form to given models
    class Meta():
        model=Visitor
        fields=('host','visitor_name','email','phone_no')
