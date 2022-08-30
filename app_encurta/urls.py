from django.urls import path, include

from .views import encurta_link, home, periodos

urlpatterns = [
    path('periodos/<str:periodo>/', periodos),
    path('groups/<str:group>/', home),
    path('<str:link_short>/', encurta_link)
]