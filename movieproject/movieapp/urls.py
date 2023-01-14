from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = 'movieapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('movie/<int:movie_id>/', views.detail, name='detail'),
  path('add/',  views.add_movie, name='add_movie'),
  path('update/<int:mov_id>/', views.update, name='update'),
  path('Delete/<int:id>/', views.Delete, name='Delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
