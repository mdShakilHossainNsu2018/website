from django.http import JsonResponse
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SongFrom
from .models import Album, Song
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    template_name = 'music/detail.html'
    model = Album


class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    # def get(self, request, *args, **kwargs):
    #     self.user = request.user
    #     return super(AlbumCreate, self).get(self, request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form.instance.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('music:index')


class AlbumUpdate(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class SongCreate(LoginRequiredMixin, CreateView):
    form_class = SongFrom
    model = Song

    def get_success_url(self):
        return reverse_lazy('music:song-add', kwargs={'pk': self.object.album.pk})

    def form_valid(self, form):
        album = get_object_or_404(Album, pk=self.kwargs['pk'])
        form.instance.album = album
        return super(SongCreate, self).form_valid(form)


class SongDelete(LoginRequiredMixin, DeleteView):
    model = Song

    def get_success_url(self, **kwargs):

        return reverse_lazy('music:detail', kwargs={'pk': self.object.album.pk})

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(pk=self.kwargs['pk'])


def favorite(request, pk):
    song = get_object_or_404(Song, pk=pk)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return redirect('music:detail', pk=song.album.id)


def favorite_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return redirect('music:index')


class AllSong(ListView):
    model = Song
    template_name = 'music/all_song.html'

#
# def songToggleFavorite(request, pk):
#     print(pk)
#     song = get_object_or_404(Song, pk=pk)
#     # song = song.save(commit=False)
#     per_fev = song.is_favorite
#     # print(per_fev)
#     # song = song.save(commit=False)
#     song.is_favorite = not per_fev
#     song.save()
#     print(song.album.id)
#     return reverse_lazy('music:detail', kwargs={'pk': song.album.id})
#
#
# class SongToggleFavorite(LoginRequiredMixin, UpdateView):
#     model = Song
#     # template_name = 'music/detail.html'
#
#     fields = ('is_favorite', )
#
#     def form_valid(self, form):
#         song = form.save(commit=False)
#         pre_fev = self.object.is_favorite
#         # print(pre_fev)
#         song.is_favorite = pre_fev
#         song.save()
#         return super(SongToggleFavorite, self).form_valid(form)
#
#     def get_success_url(self, **kwargs):
#
#         return reverse_lazy('music:detail', kwargs={'pk': self.object.album.pk})
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(pk=self.kwargs['pk'])







