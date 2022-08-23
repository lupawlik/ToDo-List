from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new_e/', views.add_new_e, name='add_new_e'),
    path('employee/<int:id_e>', views.employee, name='employee'),
    path('task/update/<int:id_t>/', views.update_task, name='update_task'),
    path('export_csv/<int:id_e>/', views.export_csv, name='export_csv'),
]