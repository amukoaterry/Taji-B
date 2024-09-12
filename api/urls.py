from django.urls import path

from.views import ScanEventDetailView
from .views import ScanEventListView
urlpatterns =[
    path('scan-events/', ScanEventListView.as_view(), name='scan_event_list_view'),
    path('scan-events/<int:id>/', ScanEventDetailView.as_view(), name='scan_event_detail_view'),
]