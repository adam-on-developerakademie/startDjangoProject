from django.urls import path
from tech_gadgets.views import start_page_view, single_gadget_view_json, single_gadget_view_JsonResponse, single_gadget_your_string, single_gadget_view_slugify

urlpatterns = [
    path("", start_page_view, name="start-page"),  # Beispiel für eine Startseiten-URL
    path("gadgets-jason/<int:gadget_id>/", single_gadget_view_json),
    path("gadgets-jsonresponse/<int:gadget_id>/", single_gadget_view_JsonResponse),
    path("your-string/<str:yourString>/", single_gadget_your_string),
    path("find/<str:yourString>/", single_gadget_view_slugify),
]
