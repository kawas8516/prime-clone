"""ModelForm used to add and edit catalogue titles.

Author: kawas8516 <https://github.com/kawas8516>
"""

from django import forms
from django.utils import timezone

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            # Matches the model's MinValueValidator/MaxValueValidator so the
            # browser blocks an out-of-range year before the form is even
            # submitted; the model validators still enforce it server-side.
            "releaseYear": forms.NumberInput(
                attrs={
                    "min": 1888,
                    "max": timezone.now().year + 1,
                    "placeholder": "e.g. 2016",
                }
            ),
        }
