from django.urls import path
from tech_gadgets.views import start_page_view

urlpatterns = [
    path('', start_page_view, name='start-page'),  # Beispiel für eine Startseiten-URL
    ]
