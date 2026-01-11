from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LocationForm
from .models import SampleModel
from .schema import SampleModelSchema

INITIAL_LATITUDE = 35.6812
INITIAL_LONGITUDE = 139.7671


@login_required
def index(request):
    samples = [
        SampleModelSchema.model_validate(sample)
        for sample in SampleModel.objects.order_by("-created_at").all()
    ]
    return render(request, "sample/index.html", {"samples": samples})


@login_required
def clicked(request):
    context = {"message": "Button clicked!"}
    return render(request, "sample/clicked.html", context)


@login_required
def map_view(request):
    context = {
        "initial_latitude": INITIAL_LATITUDE,
        "initial_longitude": INITIAL_LONGITUDE,
        "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, "sample/map.html", context)


@login_required
def validate_pin(request):
    if request.method == "POST":
        form = LocationForm(data=request.POST)
        if form.is_valid():
            return HttpResponse("", status=204)
        else:
            # ステータスコード200を返すことで、HTMXがhx-targetに従ってDOMを更新できるようにする
            return render(
                request,
                "sample/_pin_error.html",
                {"form": form},
            )
    return HttpResponse("", status=400)


@login_required
def submit_location(request):
    if request.method == "POST":
        form = LocationForm(data=request.POST)
        if form.is_valid():
            return render(
                request,
                "sample/_pin_success.html",
                {
                    "latitude": form.cleaned_data["latitude"],
                    "longitude": form.cleaned_data["longitude"],
                },
            )
        else:
            # ステータスコード200を返すことで、HTMXがhx-targetに従ってDOMを更新できるようにする
            return render(
                request,
                "sample/_pin_error.html",
                {"form": form},
            )
    return HttpResponse("", status=400)
