from django import forms
from .models import Song


class SongFrom(forms.ModelForm):
    # is_favorite = forms.RadioSelect()

    class Meta:
        model = Song
        fields = ['file_type', 'song_title', 'song_file', 'is_favorite']

