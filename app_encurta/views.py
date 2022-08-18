from django.shortcuts import redirect, get_object_or_404
from .models import Link

# Create your views here.
def encurta_link(request, link_short):
    link =  get_object_or_404(Link, link_short=link_short)
    return redirect(link.link)