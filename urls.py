
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
    path('browse_cars.html', views.browse_cars, name='browse_cars'),
    path('browse_cars_detailed.html', views.browse_cars_detailed, name='browse_cars_detailed'),
    path('sell_cars.html', views.sell_cars, name='sell_cars'),

    
    path('login.html', views.login, name='login'),
    path('logout.html', views.logout, name='logout'),
    
    path('wallet.html', views.wallet, name='wallet'),
    path('reserve.html', views.reserve, name='reserve'),
    path('confirm.html', views.confirm, name='confirm_purchase'),
    path('inventory.html', views.inventory, name = 'inventory'),
    path('about_us.html', views.about_us, name = "about_us"),
    path('test_sell.html', views.test_sell, name = "test_sell"),
    path('upload.html', views.upload, name = "upload"),

    path('view_profile.html', views.view_profile, name = "view_profile"),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(PATH, document_root=ROOT)
    
