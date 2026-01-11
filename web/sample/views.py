from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import SampleModel
from .schema import SampleModelSchema


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
