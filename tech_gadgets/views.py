from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.urls import reverse
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
    gadget_slugify = {"result": "Not Found"}

    for gadget in gadgets:
        if slugify(gadget["name"]) == slugify(yourString):
            gadget_slugify = gadget
            break
    return JsonResponse(gadget_slugify)


def single_gadget_int(request, gadget_id=0):
    if gadget_id <= len(gadgets):
        return JsonResponse(gadgets[gadget_id])
    else:
        return HttpResponseNotFound("Gadget not found")


def single_gadget_string(request, gadget_slug=""):
    # gadget_data = {"result": "Not Found"}    # Alternative Methode zu Http404
    gadget_data = None

    for gadget in gadgets:
        if slugify(gadget["name"]) == slugify(gadget_slug):
            gadget_data = gadget
            break
    if gadget_data is not None:
        return JsonResponse(gadget_data)
    raise Http404()


def single_gadget_view_slugify_url(request, gadget_id=0):
    if gadget_id <= len(gadgets):
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("single_gadget_url", args=[new_slug])
        return redirect(new_url)
    else:
        return HttpResponseNotFound("Gadget not found")


#####################################################################
# POST Method Example
#####################################################################
def single_gadget_post(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"Received data: {data}  Type: {type(data)}")
            gadget_id = data.get("gadget_id", None)
            if gadget_id is not None and 0 <= gadget_id < len(gadgets):
                return JsonResponse(gadgets[gadget_id])
            else:
                return HttpResponseNotFound("Gadget not found")
        except json.JSONDecodeError:
            return HttpResponse("Das war kein gültiges JSON", status=400)