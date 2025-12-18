from django.urls import path
from tech_gadgets.views import (
    single_gadget_int,
    single_gadget_string,
    start_page_view,
    single_gadget_view_json,
    single_gadget_view_JsonResponse,
    single_gadget_your_string,
    single_gadget_view_slugify,
    single_gadget_view_slugify_url,
)

urlpatterns = [
    path("", start_page_view, name="start-page"),  # Beispiel für eine Startseiten-URL
    path("gadgets-jason/<int:gadget_id>/", single_gadget_view_json),
    path("gadgets-jsonresponse/<int:gadget_id>/", single_gadget_view_JsonResponse),
    path("your-string/<str:yourString>/", single_gadget_your_string),
    path("slugify/<str:yourString>/", single_gadget_view_slugify),
    
    path("gadget/<int:gadget_id>/", single_gadget_int),
    path("gadget/<str:gadget_slug>/", single_gadget_string, name="single_gadget_url"),
    path("slugify-url/<int:gadget_id>/", single_gadget_view_slugify_url),
]
