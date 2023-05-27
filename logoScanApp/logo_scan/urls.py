from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_logo, name='scan_logo'),
    path('review/<int:logo_id>/', views.add_review, name='add_review'),
]
