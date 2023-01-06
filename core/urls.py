from django.urls import path
from . import views


#rutas
urlpatterns = [
    path('', views.HomePageView, name="home"),
    path('sobre_nosotros/', views.SobreNosotrosView, name="sobre_nosotros"),
    path('cortes/', views.CortesView, name="cortes"),
]