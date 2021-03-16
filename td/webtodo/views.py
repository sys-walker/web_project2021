from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#CONTROLLER

def home(r):
	return HttpResponse("OK")