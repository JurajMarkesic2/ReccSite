from django import forms
from django.forms.widgets import RadioSelect

class quizForm(forms.Form):
	firstQ = forms.BooleanField(label='First question',required=False,widget=RadioSelect(choices=[(True, 'yes'), 
                                                            (False, 'no')]))
	secondQ = forms.BooleanField(label='Second question',required=False,widget=RadioSelect(choices=[(True, 'yes'), 
                                                            (False, 'no')]))
	thirdQ = forms.BooleanField(label='Third question',required=False,widget=RadioSelect(choices=[(True, 'yes'), 
                                                            (False, 'no')]))
	fourthQ = forms.BooleanField(label='Forth question',required=False,widget=RadioSelect(choices=[(True, 'yes'), 
                                                            (False, 'no')]))