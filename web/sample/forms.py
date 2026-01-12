from django import forms
from django.core.exceptions import ValidationError

# 座標比較のしきい値（約0.1メートルに相当）
COORDINATE_THRESHOLD = 1e-6


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
                # floatの厳密な等価比較を避け、しきい値を使った比較を行う
                lat_diff = abs(lat - initial_lat)
                lng_diff = abs(lng - initial_lng)
                if (
                    lat_diff < COORDINATE_THRESHOLD
                    and lng_diff < self.COORDINATE_THRESHOLD
                ):
                    raise ValidationError("ピンを動かしてください")

        return cleaned_data
