from django.shortcuts import render
from django.http import HttpResponse

def shoppinglistView(request):
    return HttpResponse('Einkaufszettel')