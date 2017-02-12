from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from register.models import MyUser
from .models import Test
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@require_POST
def request_test(request):
	input = request.POST