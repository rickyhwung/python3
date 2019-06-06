from django.contrib import admin
from .models import Bbsuser
from .models import Bbspost
from .models import Comment
from .models import Section

# Register your models here.
class BbsuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','isadmin',)
class BbspostAdmin(admin.ModelAdmin):
    list_display = ('postname', 'content','secid','uid',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'postid','pcid','uid',)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('secname', 'detail',)

admin.site.register(Bbsuser, BbsuserAdmin)
admin.site.register(Bbspost, BbspostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Section, SectionAdmin)