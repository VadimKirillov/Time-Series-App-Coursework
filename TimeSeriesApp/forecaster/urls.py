from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataset_size, name='dataset_size'),
    #path('', views.upload_dataframe, name='upload_dataframe'),
]