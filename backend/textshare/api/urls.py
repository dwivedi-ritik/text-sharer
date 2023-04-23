from django.urls import path
from .views import textshare_view, textshare_update_delete

urlpatterns = [
    path("", textshare_view),
    path("/<int:id>", textshare_update_delete)
]
