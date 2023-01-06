from django.urls import path
from .views import PreciosListView


#rutas
urlpatterns = [
    path('', PreciosListView.as_view(), name="precios"),
]