from django.urls import path, include

from .views import encurta_link, home

urlpatterns = [
    path('groups/<str:group>/', home),
    path('<str:link_short>/', encurta_link)
]