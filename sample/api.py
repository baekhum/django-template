from django.http import HttpResponse
from ninja import Router

from sample.apps import SampleConfig

router = Router(tags=[SampleConfig.name])


@router.get("/health/")
def health(request, *args, **kwargs):
    return HttpResponse("OK")
