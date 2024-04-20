from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from FakesUsers import Fu

# Create your views here.

def main(request):
    return render(request, 'index.html')

@api_view(['GET'])
def fake_name(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        gender = str(request.query_params.get('gender'))
        fu = Fu(lang)
        name = fu.fake_name(gender)  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_lastname(request):  
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        gender = str(request.query_params.get('gender'))
        fu = Fu(lang)
        name = fu.fake_lastname(gender)  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_number(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_number()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_addres(request):
    lang = str(request.query_params.get('lang'))
    full = str(request.query_params.get('full'))
    fu = Fu(lang)
    if request.method == 'GET':
        if full == 'True' or full == 'true':
            name = fu.fake_addres(True)  # используйте значение переменной gender
            return Response(name)
        else:
            name = fu.fake_addres(False)  # используйте значение переменной gender
            return Response(name)

@api_view(['GET'])
def fake_email(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_email()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_pass(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_pass()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_dob(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_dob()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_city(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_city()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_banknumber(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_banknumber()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_login(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_login()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_link(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_link()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_autonum(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_autonum()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_text(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_text()  # используйте значение переменной gender
        return Response(name)

@api_view(['GET'])
def fake_job(request):
    if request.method == 'GET':
        lang = str(request.query_params.get('lang'))
        fu = Fu(lang)
        name = fu.fake_job()  # используйте значение переменной gender
        return Response(name)