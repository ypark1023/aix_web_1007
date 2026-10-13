from django.urls import path,include
from . import views

app_name='students'
urlpatterns = [
    path('swrite/', views.swrite, name='swrite'),
    # path('swrite2/<str:name>/', views.swrite2, name='swrite2'),
    # path('swrite3/', views.swrite3, name='swrite3'),
    path('slist/', views.slist, name='slist'),
    path('sview/<int:no>/', views.sview, name='sview'),
    path('supdate/<int:no>/', views.supdate, name='supdate'),
    path('sdelete/<int:no>/', views.sdelete, name='sdelete'),
]