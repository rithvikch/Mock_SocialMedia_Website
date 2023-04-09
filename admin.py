from django.contrib import admin

# Register your models here.
from connectify.models import Post

from connectify.models import UserProfile

from connectify.models import Blog

from connectify.models import Comment
from connectify.models import LikePost

admin.site.register(LikePost)

admin.site.register(Post)

admin.site.register(UserProfile)


admin.site.register(Blog)


admin.site.register(Comment)

