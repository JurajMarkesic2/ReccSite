from django import forms
from django.forms.widgets import RadioSelect

class quizForm(forms.Form):
	firstQ = forms.BooleanField(label='First question',required=False, initial=True,widget=RadioSelect(choices=[(True, 'Extrovert'), 
                                                            (False, 'Introvert')]))
	secondQ = forms.BooleanField(label='Second question',required=False,initial=True,widget=RadioSelect(choices=[(True, 'Sensing'), 
                                                            (False, 'Intuitive')]))
	thirdQ = forms.BooleanField(label='Third question',required=False,initial=True,widget=RadioSelect(choices=[(True, 'Thinking'), 
                                                            (False, 'Feeling')]))
	fourthQ = forms.BooleanField(label='Forth question',required=False,initial=True,widget=RadioSelect(choices=[(True, 'Judging'), 
                                                            (False, 'Perceiving')]))


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)    
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
       super(ContactForm, self).__init__(*args, **kwargs)
       self.fields['contact_name'].label = "Name:"
       self.fields['contact_email'].label = "E-mail:"
       self.fields['content'].label = "Message:"	