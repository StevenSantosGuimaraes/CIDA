from django.urls import path
from . import views


urlpatterns = [
    path('sankey/', views.sankey, name='sankey'),
]
