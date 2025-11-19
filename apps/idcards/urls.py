from django.urls import path
from . import views

app_name = 'idcards'

urlpatterns = [
    path('', views.idcard_dashboard, name='idcard-dashboard'),
    path('generate/', views.IDCardSearchView.as_view(), name='generate-idcard-search'),  # NEW
    path('generate/<int:student_id>/', views.generate_id_card, name='generate-idcard'),
    path('bulk-generate/', views.bulk_generate_id_cards, name='bulk-generate'),
    path('bulk-generate/class/<int:class_id>/', views.bulk_generate_class_id_cards, name='bulk-generate-class'),
    path('download/<int:student_id>/', views.download_id_card_pdf, name='download-idcard'),
    path('download/bulk/', views.download_bulk_id_cards, name='download-bulk'),
    path('templates/', views.manage_templates, name='manage-templates'),
    path('list/', views.idcard_list, name='idcard-list'),
    path('renew/<int:student_id>/', views.renew_id_card, name='renew-idcard'),
]