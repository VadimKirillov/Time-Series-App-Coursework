from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('oceans/', dataset_size, name='dataset_size'),
    path('datasets/', dataset_list, name='dataset_list'),
    #path('datasets/create/', views.create_dataset, name='create_dataset'),
    path('datasets/create', DatasetCreate.as_view(),
         name='create_dataset_url'),
    #path('', views.upload_dataframe, name='upload_dataframe'),
]