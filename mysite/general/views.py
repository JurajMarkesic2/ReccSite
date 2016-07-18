from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from general.models import Result
from general.forms import quizForm, ContactForm
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from django.template import RequestContext
from django.conf import settings
from django.template import Context


def index(request):              #home page view, renders home.html, survey form in here, submit form to get the result
	qForm = quizForm
	if request.method == 'POST':    #check if POST method is use, if it is check if the form is valid, if it is it declared variables and runs a test to see which result we will server the client
		form = qForm(data=request.POST)
		if form.is_valid():
			firstQ = request.POST.get('firstQ','')
			secondQ = request.POST.get('secondQ','')
			thirdQ = request.POST.get('thirdQ','')
			fourthQ = request.POST.get('fourthQ','')


			if firstQ == 'True':
				if secondQ == 'True':
					if thirdQ == 'True':
						if fourthQ == 'True':
							idv = 1
						else:
							idv = 2
					else:
						if fourthQ == 'True':
							idv = 3
						else:
							idv = 4
				else:
					if thirdQ == 'True':
						if fourthQ == 'True':
							idv = 5
						else:
							idv = 6
					else:
						if fourthQ == 'True':
							idv = 7
						else:
							idv = 8
			else:
				if secondQ == 'True':
					if thirdQ == 'True':
						if fourthQ == 'True':
							idv = 9
						else:
							idv = 10
					else:
						if fourthQ == 'True':
							idv = 11
						else:
							idv = 12
				else:
					if thirdQ == 'True':
						if fourthQ == 'True':
							idv = 13
						else:
							idv = 14
					else:
						if fourthQ == 'True':
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

     
def about(request):             #about page view, renders about.html  -- static page, simple
	return render(request, 'general/about.html')

 
def contact(request):           #contact page view, renders contact.html	--- needs contact app (downloadable) and email setup
    form_class = ContactForm     
    success = False
    success_msg="Your messege was sent successfully!"
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            template = get_template('general/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(     
                "New contact form submission",
                form_content,
                'xyz@gmail.com',
                [settings.EMAIL_HOST_USER],
                headers = {'Reply-To': contact_email})
            email.send(fail_silently=False)
            success = True

            return render_to_response('general/contact.html',
                        {'form' : form_class,'success': success,'success_msg':success_msg}, context_instance=RequestContext(request))
                          

    return render(request, 'general/contact.html', {
        'form': form_class,
    })

		