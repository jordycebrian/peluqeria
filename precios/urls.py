from django.urls import path
from .views import PreciosListView

urlpatterns = [
    path('', PreciosListView.as_view(), name="precios"),
]