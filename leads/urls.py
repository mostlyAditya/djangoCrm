from django.urls import path
from .views import (
    lead_list,lead_detail,lead_create,lead_update,lead_delete,
    LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView
    )

app_name='leads'
urlpatterns=[
    path('',LeadListView.as_view(),name='lead-list'),
    path('<int:pk>/',LeadDetailView.as_view(),name='lead-detail'),
    #path('<int:pk>/',lead_detail,name='lead-detail'),#Added int: so that pk indentifies only integer as id
    #path('create/',lead_create,name='lead-create'),
    path('create/',LeadCreateView.as_view(),name='lead-create'),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name='lead-update'),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name='lead-delete')
    #path('<int:pk>/delete/',lead_delete,name='lead-delete')
    ]