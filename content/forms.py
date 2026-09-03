"""ModelForm used to add and edit catalogue titles.

Author: kawas8516 <https://github.com/kawas8516>
"""

from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
