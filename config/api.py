from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from ninja import NinjaAPI

api = (
    NinjaAPI(title=f"{settings.PROJECT_NAME}", docs_url="/docs/")
    if settings.ENV in {"dev"}
    else NinjaAPI(title=f"{settings.PROJECT_NAME}", docs_url="/docs/", docs_decorator=staff_member_required)
)

api.add_router("/sample/", "sample.api.router")
