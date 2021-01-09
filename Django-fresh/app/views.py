from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
	current_time = datetime.datetime.now()
	return render(request, 'index.html', {'current_time': current_time})	

def time(request):
	current_time = datetime.datetime.now()
	return render(request, 'time.html', {'current_time': current_time})
