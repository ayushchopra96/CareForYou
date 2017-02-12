from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MyUser
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
@require_POST
def loginview(request):
	response_data = {}
	input = request.POST
	try:
		obj = MyUser.objects.get(username=input['username'])
		response_data['success'] = '1'
		reponse_data['new-user'] = '0'
		return JsonResponse(response_data)
	except MyUser.DoesNotExist:
		MyUser.objects.create(uid=input['uid'],username=input['username'],email=input['email'],phone=input['phone'],gender=input['gender'],age=input['age'],city=input['city'])
		response_data['success'] = '1'
		response_data['new-user'] = '0'
		return JsonResponse(response_data)

@csrf_exempt
@require_POST
def update_details(request):
	response_data={}
	input = request.POST
	#updating the age.
	val = input['update']
	try:
		obj = MyUser.objects.get(username=input['username'])
		oldval = obj['age']
		obj['age'] = val
		obj.save()
		response_data['success'] = '1'
		response_data['oldval'] = oldval
		response_data['newval'] = val
		return JsonResponse(response_data)
	except MyUser.DoesNotExist:
		response_data['success'] = '0'
		return JsonResponse(response_data)
