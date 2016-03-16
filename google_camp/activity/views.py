from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from camper_mng.models import Camper
from .forms import NregForm

# Create your views here.
def activities(request):
	return render(request,'act.html')

def gogogo(request):
	form = NregForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data['name']
		phone = form.cleaned_data['phone']
		created = Camper.objects.filter(phone=phone)
		if len(created)==0:
			print "no user"
			new_camper , created = Camper.objects.get_or_create(student_id=000000,phone=phone,name=name,GDG=True)
			# send_complex_message(mail)
			return HttpResponseRedirect('https://gdgdocs.org/forms/d/1pWpBIzU2ldRD8OKhDFYap_3YyQ5ROAPJ_CJFqtpsnAk/viewform')
		else:
			created[0].GDG = True
			created[0].save()
			return HttpResponseRedirect('https://gdgdocs.org/forms/d/1pWpBIzU2ldRD8OKhDFYap_3YyQ5ROAPJ_CJFqtpsnAk/viewform')
	else:
		return HttpResponseRedirect('https://gdgdocs.org/forms/d/1pWpBIzU2ldRD8OKhDFYap_3YyQ5ROAPJ_CJFqtpsnAk/viewform')