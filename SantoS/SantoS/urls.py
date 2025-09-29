from django.contrib import admin
# from django.conf.urls.static import static
from django.urls import path
from Machinery import views
# from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search_results'),
]

# Serve media files during development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# check the imports also
