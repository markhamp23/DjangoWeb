from django.shortcuts import render

# Create your views here.

def pag_ini(request):
	return render(request,'inici.html')