from email.headerregistry import Group
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
    
class GroupLink(models.Model):
    name = models.CharField("Nome", max_length=50)
    slug = models.SlugField(_("Slug"))
    owner = models.ForeignKey(User, verbose_name=_(
        "Owner"), on_delete=models.CASCADE, null=True, blank=True)
    
    def save_model(self, request, obj, form, change):
        if not obj.owner:
             obj.owner = request.user
        super().save_model(request, obj, form, change)
        
    def __str__(self) -> str:
        return self.name
    
class Link(models.Model):
    name = models.CharField(_("Nome"), max_length=50, null=True)
    link = models.URLField("Link", max_length=255)
    link_short = models.CharField("Link short", max_length=200, unique=True)
    group = models.ForeignKey(GroupLink, verbose_name="Grupo", on_delete=models.CASCADE)
    public = models.BooleanField(_("Public"), default=True)
    def __str__(self):
        return self.link_short