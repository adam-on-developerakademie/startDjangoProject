from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .dummy_date import gadgets, manufacturers
import json
from django.utils.text import slugify

# Create your views here.
def start_page_view(request):
    return HttpResponse("Hej das hat geklappt! Willkommen auf der Startseite.")


def single_gadget_view_json(request, gadget_id=0):
    return HttpResponse(
        json.dumps(gadgets[gadget_id]),
        content_type="application/json",  # festlegen des content types
    )


def single_gadget_view_JsonResponse(request, gadget_id=0):
    return JsonResponse(gadgets[gadget_id])


def single_gadget_your_string(request, yourString=0):
    return HttpResponse(f"Das ist dein String: {yourString}")

def single_gadget_view_slugify(request, yourString=""):
    gadget_find = {"result": "Not Found"}
    
    for gadget in gadgets:
        if slugify(gadget["name"]) ==  slugify(yourString):
            gadget_find = gadget
            break
    return JsonResponse(gadget_find)