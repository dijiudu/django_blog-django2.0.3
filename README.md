# django_blog-django2.0.3+ python3.6

# 修改点

## setting.py
```
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'notifications'))

DEBUG = True
```
## url.py 
```

# url(r'^robots\.txt$', include('robots.urls')),
```
## __init__.py
```
"""
import pymysql
pymysql.install_as_MySQLdb()
"""
```

## blog/admin.py
```
"""
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User)
"""
```

## blog/view.py
```
"""
import logging

logger = logging.getLogger('blog.views')
Create your views here.
"""
```

## blog\templatetags\blog_tags.py
```
"""
if not owner:
    from blog.models import User
    # user = User.objects.get(id=1)
    user = User.objects.get()
    post_num = len(user.post_set.all())
    view_num = 0
    for post in user.post_set.all():
        view_num += post.click_count
    owner = {'name': user.username, 'post_num': post_num, 'view_num': view_num, 'avatar': user.avatar.url}
    cache.set('owner', owner, timeout=24*60*60)
"""
```

## easy_comment\admin.py
```
"""
admin.site.register(Comment, MPTTModelAdmin)
admin.site.register(Favour)
"""
```

## notifications/modles.py
```
ForeignKey(on_delete=models.CASCADE)
```


## redis
```
redis-server.exe redis.conf 
redis-cli.exe -h 127.0.0.1 -p 6379
```

## django 自带admin 丢失样式，找不到css, 替换为xadmin

## 所有的 request.user.is_authenticated() 修改为 request.user.is_authenticated