from django.shortcuts import render, get_object_or_404
from general.models import Result
from django.http import HttpResponseRedirect
from .forms import Checkboks

def index(request):
    form = Checkboks()
    return render(request, 'general/home.html', {'form': form})


#def result(request, id):        #result page view, renders result.html --needs to serve info from the model to the html file, result logic goes in here(?)
	#res = get_object_or_404(res, pk=id)
	#return render(request, 'general/result.html', {  
    #    'res': res, })  

     
#def about(request):             #about page view, renders about.html  -- static page, simple
	#return	  

 
#def contact(request):           #contact page view, renders contact.html	--- needs contact app (downloadable) and email setup
	#return
		
