from django import forms

class Checkboks(forms.Form):
	CHOICE1=[('select1','extrovert'), ('select2','introvert')]
	CHOICE2=[('select1','sensing'), ('select2','intuitive')]
	CHOICE3=[('select1','thinking'), ('select2','feeling')]
	CHOICE4=[('select1','judging'), ('select2','percieving')]
	attitude = forms.ChoiceField(label='attitude', choices=CHOICE1, widget=forms.RadioSelect())
	intuition = forms.ChoiceField(label='intuition', choices=CHOICE2, widget=forms.RadioSelect())
	thinking = forms.ChoiceField(label='thinking', choices=CHOICE3, widget=forms.RadioSelect())
	life = forms.ChoiceField(label='life', choices=CHOICE4, widget=forms.RadioSelect())