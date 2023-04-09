
from django.contrib import admin
from django.urls import path

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib.auth import views as auth_views
# from django.conf.urls.static import static
# from django.conf import settings



from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


from connectify import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),

    path('login.html', views.sign_in, name='sign_in'),
    path('logout.html', views.logout, name='logout'),
    path('register.html', views.register, name='register'),
    path('about_us.html', views.about_us, name='about_us'),

    path('browse.html', views.browse, name='browse'),
    path('create.html', views.create, name='create'),

    path('my_profile.html', views.my_profile, name='my_profile'),

    path('edit_post.html', views.edit_post, name='edit_post'),
    path('edit_profile.html', views.edit_profile, name='edit_profile'),
    path('like_post', views.like_post, name= 'like_post'),

    path('post_detailed.html', views.post_detailed, name='post_detailed'),



    path('blogs.html', views.blogs, name='blogs'),
    path('blog_detailed.html', views.blog_detailed, name='blog_detailed'),


    path('view_profile.html', views.view_profile, name='view_profile'),

    path('new_login.html', views.new_login, name='new_login'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(PATH, document_root=ROOT)
    
