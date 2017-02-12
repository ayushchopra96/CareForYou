from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from register.models import MyUser
from .models import Test
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
# Create your views here.
@require_POST
def request_test(request):
	input = request.POST
	response_data = {}
	obj = Test.objects.create(username = input['username'])
	response_data['success'] = '1'

@require_POST
def detect_diabetes(request):
	input = request.POST
	input_data = []
	input_data.append(input['pregencies'])
	input_data.append(input['glucose'])
	input_data.append(input['bloodpressure'])
	input_data.append(input['skin_thickness'])
	input_data.append(input['insulin'])
	input_data.append(input['bmi'])
	input_data.append(input['diabetes_function'])
	input_data.append(input['age'])
	ans = predict_result([input_data])
	ans = int(ans)
	response_data = {}
	response_data["result"] = ans
	return response_data

model = SVC(kernel="linear", C=0.1)

def predict_result(input):
	global model
	return model.predict(input)

def model_train():
	global model 
	fd = open("diabetes.csv")
	fd.readline()
	data = np.loadtxt(f, delimiter=',')
	X = data[:,:-1]
	y = data[:,-1]
	X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=0)
	model = SVC(kernel="linear", C=0.15)
	model.fit(X_train,y_train)
