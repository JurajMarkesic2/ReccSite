from django import forms
from django.forms.widgets import RadioSelect

class quizForm(forms.Form):
	firstQ = forms.BooleanField(label='First question',required=False,widget=RadioSelect(choices=[(True, 'Extrovert'), 
                                                            (False, 'Introvert')]))
	secondQ = forms.BooleanField(label='Second question',required=False,widget=RadioSelect(choices=[(True, 'Sensing'), 
                                                            (False, 'Intuitive')]))
	thirdQ = forms.BooleanField(label='Third question',required=False,widget=RadioSelect(choices=[(True, 'Thinking'), 
                                                            (False, 'Feeling')]))
	fourthQ = forms.BooleanField(label='Forth question',required=False,widget=RadioSelect(choices=[(True, 'Judging'), 
                                                            (False, 'Perceiving')]))