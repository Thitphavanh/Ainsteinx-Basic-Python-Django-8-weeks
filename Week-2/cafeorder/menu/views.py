from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu_list(request):
    return HttpResponse("ສະບາຍດີ ນີ້ແມ່ນໜ້າເມນູ")