from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import requests
import json
from django.http import JsonResponse
import heapq
from django.views.decorators.csrf import csrf_exempt
from .models import Member

def supervisors(request):
	data = requests.get("https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers")
	# heap sort supervisors
	heap = []
	heapq.heapify(heap)
	for s in data.json():
		j, ln, fn = s["jurisdiction"], s["lastName"], s["firstName"]
		if j.isalpha():
			heapq.heappush(heap, (j, ln, fn))

	supervisorList = []
	while heap:
		j, ln, fn = heapq.heappop(heap)
		supervisorList.append(ln + ", " + fn)

	# return supervisorList as json object
	return JsonResponse({i :s for i, s in enumerate(supervisorList)})

@csrf_exempt
def submit(request):
	if request.method == "POST":
		member = Member(
			first_name=request.POST["First Name"],
			last_name=request.POST["Last Name"],
			email=request.POST["Email"],
			phone_number=request.POST["Phone Number"],
			preference=request.POST["Preferred"],
			supervisor=request.POST["Supervisor"],
		)

		member.save()
		return HttpResponse(member)
