from django.urls import path
from .views import Citas


urlpatterns = [
    path('', Citas.as_view(), name="citas")
]