from django.contrib import admin

from crud.models import Blog,Contact

# Register your models here.
admin.site.site_header = "Blog Application"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Blog Adminastrator"

class BlogAdmin(admin.ModelAdmin):
    list_display = "__str__","title","subtitle","description",
    fields = (("title","subtitle",),"description")
    list_editable ="title","subtitle","description",
    search_fields = "title",
admin.site.register(Blog,BlogAdmin),
admin.site.register(Contact) 