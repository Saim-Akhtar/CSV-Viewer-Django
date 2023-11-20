from django.urls import path

from main.views import datatable_view, patient_detail

urlpatterns = [
    path('', datatable_view, name='datatable_view'),
    path('<str:patient_id>/', patient_detail, name='patient_detail'),
]