from django.urls import path, include

from.views import encurta_link

urlpatterns = [
    path('<str:link_short>', encurta_link)
]