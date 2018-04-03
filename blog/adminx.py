import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import Post,Category,Tag,User
# Register your models here.

class PostAdmin(object):
    fields = ('title', 'excerpt', 'content', 'category', 'tag', 'author', 'cover')
    list_display = ('title', 'date_created', 'date_modified', 'category', 'author', 'is_recommended',)
    list_editable = ('category', 'author', 'is_recommended',)

class TagAdmin(object):
    pass

class CategoryAdmin(object):
    pass

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "blog在线"
    menu_style = "accordion"


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
# xadmin.site.register(User) 

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)







