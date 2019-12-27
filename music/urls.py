from django.urls import path
from . import views


app_name = 'music'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('<int:pk>/song-add/', views.SongCreate.as_view(), name='song-add'),

    path('all-songs/', views.AllSong.as_view(), name='all-songs'),

    path('<int:pk>/song-delete/', views.SongDelete.as_view(), name='song-delete'),

    path('<int:pk>/song-toggle-favorite/', views.favorite, name='song-toggle-favorite'),

    path('<int:pk>/album-toggle-favorite/', views.favorite_album, name='album-toggle-favorite'),

    path('<int:pk>/', views.DetailView.as_view(), name="detail"),

    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),


]
