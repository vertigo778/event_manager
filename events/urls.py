from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.create_event, name='create_event'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('entry/<int:entry_id>/update/<str:status>/', views.update_entry_status, name='update_entry_status'),
    path('entry/<int:entry_id>/delete/', views.delete_entry, name='delete_entry'),
    path('', views.home, name='home'),
    path('logout/', views.custom_logout, name='logout'),
]