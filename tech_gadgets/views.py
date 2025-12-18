from django.shortcuts import render
from django.http import HttpResponse
from .dummy_date import gadgets, manufacturers


# Create your views here.
def start_page_view(request):
    return HttpResponse("Hej das hat geklappt! Willkommen auf der Startseite.")


def single_gadget_view(request, gadget_id=0):
    return HttpResponse(f"dein Gadget ist: {gadgets[gadget_id]}.")
