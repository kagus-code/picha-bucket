from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [

  re_path(r'^$', views.landing,name='landingPage'),
  re_path(r'^search/', views.search_results, name='search_results'),
  re_path(r'^location/(?P<location_id>\d+)', views.location_image, name='location_image'),



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  