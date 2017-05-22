from django.shortcuts import render
import random
import string

# Create your views here.
def index(request):
	request.session['count'] = 0
	return render(request, 'first_app/index.html')

def submit(request):
	str = ''
	if request.method == 'POST':
		for i in range(0,14):
			str += random.choice(string.ascii_uppercase)
		request.session['count'] += 1
		context = {
			'str': str
		}
		return render(request, 'first_app/index.html', context)