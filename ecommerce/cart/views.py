from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LoginSerializer
import json 
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# import models
from .models import Login, Item, Order

# Create your views here.

class Users(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

@csrf_exempt
def signup(request):
    try:
        if request.method=="POST":
            data = json.loads(request.body)
            username = load_data['username']
            mobile = load_data['mobile']
            password = load_data['password']
            # check whether the give data is empty or not
            if not mobile or not password or not username:
                return response(False, "Please pass the required data")
            
            obj = Users.objects.filter(mobile=mobile)

            if obj.exists():
                return response(False, "User Already exists")
            else:    
                User.objects.create(userName = username,mobile = mobile,password = password,)
                return response(True, "Signup successful new user created")
    except Exception as ex:
        return response(False, "unexpected error occured")

@csrf_exempt
def login(request):
    try:
        if request.method == "POST":
            load_data = json.loads(request.body)
            mobile = load_data['mobile']
            password = load_data['password']
            # check whether the give data is empty or not
            if not mobile or not password:
                return response(False, "Please pass the required data")
            mobile = mobile
            password = password

            obj = Users.objects.filter(mobile=mobile)

            if obj.exists():
                user = obj.first()
                return response(True, "Successfully logged in")
            else:
                return response(False, "User not found try to signin")
        else:
            return response(False, "Unable to fetch the user data")
    except Exception as ex:
        return response(False, "unexpected error occured")

@csrf_exempt
def order_product(request):
    try:
        if request.method=="POST":
            load_data = json.loads(request.body)
            username = load_data['username']
            productName = load_data["productname"]
            quantity = load_data['quantity']
            paymentMethod = load_data['method']
            datetime = load_data['datetime']
            # filter by username
            user = Users.objects.filter(name=data['username'])
            # filter by productname
            product = Item.objects.filter(name=data['productname'])

            if pro and product:
                user=user.first()
                product = product.first()
                Order.objects.create(productName = product, userName = user, quantity = quantity, paymentMethod = paymentMethod, dateOfPurchase = datetime)
                return response(True, "Successfully Purchased")

    except Exception as ex:
        return response(False, "unexpected error occured")

@csrf_exempt
def filter_product(request):
    try:
        if request.method == "POST":
            load_data = json.loads(request.body)
            category = load_data["category"]
            minval = load_data["min_price"]
            maxval = load_data["max_price"]
            # filter by category
            category_list = Item.objects.all().filter(category=category)
            data = {}
            for item in category_list:
                if int(item.price) >= minval and int(item.price) <= maxval:
                    data = { "name":item.name, "Category": item.category,"price": item.price}

                    return response(True, "fetched required data", data)

    except Exception as ex:
        return response(False, "unexpected error occured")

def response(status, msg, data=None):
    result = {}
    # if data is not none
    if data is not None:
        result['data'] = data

    result['status'] = status
    result['msg'] = msg
    
    response = JsonResponse(result, content_type='application/json', status=status)
    return response
    
    
