from django.urls import path

from . import views
app_name = 'encuesta'


urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetalleVista.as_view(), name = 'detalle'),
    path ('<int:pk>/resultados', views.ResultadoVista.as_view(), name = 'resultado'),
]