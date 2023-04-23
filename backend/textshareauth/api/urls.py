from django.urls import path
import textshareauth.api.views as views

urlpatterns = [
    path('', views.textshare_view),
    path('<int:id>', views.textshare_update_delete)
]
