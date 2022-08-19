from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from .models import GroupLink, Link

# Create your views here.
def encurta_link(request, link_short):
    link =  get_object_or_404(Link, link_short=link_short)
    return redirect(link.link)

def home(request, group):
    group = get_object_or_404(GroupLink, slug=group)
    return render(request, 'home.html',{'group':group})