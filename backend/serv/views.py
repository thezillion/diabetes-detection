from django.http import HttpResponse
from .models import Person
from .classification import Classify


def index(request):

	if request.method== 'POST':

		name= request.POST.get('name', -1)
		age= request.POST.get('age', -1)
		insulin= request.POST.get('insulin',-1)
		gender=request.POST.get('gender',-1)
		email=request.POST.get('email',-1)
		bmi=request.POST.get('bmi',-1)
		bp=request.POST.get('bp',-1)
		glucose=request.POST.get('glu',-1)

		p=Person(name,age, insulin, gender, email, bmi,bp)
		classify=Classify('data.csv')
		return HttpResponse(classify.predict(glucose,bp,insulin,bmi))




		
	else:
		return HttpResponse("NO POST")
