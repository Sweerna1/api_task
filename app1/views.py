from django.shortcuts import render
import requests
from django.http import JsonResponse

def api_list(request):
	url = "https://api.github.com/events"


	nxt = request.GET.get('next_page')
	prv = request.GET.get('previous_page')

	if nxt:
		response = requests.get(nxt).json()
	elif prv:
		response = requests.get(prv).json()
	else:
		response = requests.get(url).json()

	
	context ={
	"response": response,
	}
	return render(request, 'list.html', context)


