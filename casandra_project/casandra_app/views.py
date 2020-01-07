from django.shortcuts import render
from .models import Exampledata
from .models import bat

 

# Create your views here.
def index(request):
	data = bat.objects.all()

	data = {'data':data}

	# return render(request, "index.html")
	return render(request, "index.html", data)