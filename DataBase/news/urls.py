from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ObjectsDetailView.as_view(), name='object-detail'),
    path('<int:pk>/update', views.ObjectsUpdateView.as_view(), name='object-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)