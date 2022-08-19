from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import GroupLink, Link

# Register your models here.
@admin.register(GroupLink)
class GroupLinkAdmin(admin.ModelAdmin):
    exclude = ('owner', )
    prepopulated_fields = {'slug': ('name',), }

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('link_short', "link", 'copy_link')
    search_fields = ('link_short', "link", )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.request = request
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super().changelist_view(request, extra_context=extra_context)

    def copy_link(self, obj, *args, **kwargs):
        btn_id = f'copy-helper-{obj.pk}'
        link_short = self.request.build_absolute_uri(f'/{obj.link_short}/')
        return mark_safe(f"""
            <input text="text" id="{btn_id}" value="{link_short}" style="position: absolute; top: -10000px">
            <a href="#" onclick="document.querySelector(\'#{btn_id}\').select(); document.execCommand(\'copy\');" class="addlink">Copiar link</a>
            """
                         )
