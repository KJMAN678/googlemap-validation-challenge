from django import forms
from django.core.exceptions import ValidationError


class LocationForm(forms.Form):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())
    initial_latitude = forms.FloatField(widget=forms.HiddenInput())
    initial_longitude = forms.FloatField(widget=forms.HiddenInput())

    def clean(self) -> dict[str, float]:
        cleaned_data = super().clean()
        if cleaned_data is None:
            return {}
        lat = cleaned_data.get("latitude")
        lng = cleaned_data.get("longitude")
        initial_lat = cleaned_data.get("initial_latitude")
        initial_lng = cleaned_data.get("initial_longitude")

        if lat is not None and lng is not None:
            if initial_lat is not None and initial_lng is not None:
                if lat == initial_lat and lng == initial_lng:
                    raise ValidationError("ピンを動かしてください")
        return cleaned_data
