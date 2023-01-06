from django.urls import path
from .views import Citas


#rutas
urlpatterns = [
    path('', Citas.as_view(), name="citas")
]