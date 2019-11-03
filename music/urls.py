from django.urls import path
import music.views
urlpatterns = [
    path('',music.views.alltracks,name = 'alltracks'),
] 
