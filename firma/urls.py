from django.urls import path
from .views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('add/<str:name>', addPageView, name='add'),
    path('delete/<str:name>/<int:id>', deletePageView, name='delete'),
    path('edit/<str:name>/<int:id>', editPageView, name='edit'),
    path('search/<str:name>', searchPageView, name='search')
]
