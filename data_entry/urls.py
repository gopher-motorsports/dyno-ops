from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collectdata', views.collectData, name='collectdata'),
    path('view_data', views.viewData, name='view_data'),
]
