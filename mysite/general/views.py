from django.shortcuts import render, get_object_or_404
from general.models import Result
from general.forms import quizForm
from django.http import HttpResponseRedirect

def index(request):              #home page view, renders home.html, survey form in here, submit form to get the result
	if request.method == 'POST':    #check if POST method is use, if it is check if the form is valid, if it is it declared variables and runs a test to see which result we will server the client
		form = quizForm(request.POST)
		if form.is_valid():
			firstQ = request.POST.get('firstQ','')
			secondQ = request.POST.get('secondQ','')
			thirdQ = request.POST.get('thirdQ','')
			fourthQ = request.POST.get('fourthQ','')

			if firstQ == 'yes':
				if secondQ == 'yes':
					if thirdQ == 'yes':
						if fourthQ == 'yes':
							idv = 1
						else:
							idv = 2
					else:
						if fourthQ == 'yes':
							idv = 3
						else:
							idv = 4
				else:
					if thirdQ == 'yes':
						if fourthQ == 'yes':
							idv = 5
						else:
							idv = 6
					else:
						if fourthQ == 'yes':
							idv = 7
						else:
							idv = 8
			else:
				if secondQ == 'yes':
					if thirdQ == 'yes':
						if fourthQ == 'yes':
							idv = 9
						else:
							idv = 10
					else:
						if fourthQ == 'yes':
							idv = 11
						else:
							idv = 12
				else:
					if thirdQ == 'yes':
						if fourthQ == 'yes':
							idv = 13
						else:
							idv = 14
					else:
						if fourthQ == 'yes':
							idv = 15
						else:
							idv = 16


			return HttpResponseRedirect(idv) #returns id-based url for a desired result

	else:
		form = quizForm()		

	return render(request, 'general/home.html', {   
		'form':form,
		}) 


def result(request, id):        #result page view, renders result.html --needs to serve info from the model to the html file, result logic goes in here(?)

	res = get_object_or_404(Result, pk=id)
	return render(request, 'general/result.html', {  
         'res' : res, })  

     
#def about(request):             #about page view, renders about.html  -- static page, simple
	#return	  

 
#def contact(request):           #contact page view, renders contact.html	--- needs contact app (downloadable) and email setup
	#return
		