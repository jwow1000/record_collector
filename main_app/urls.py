from django.urls import path
from .views import Home, RecordList, RecordDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('records/', RecordList.as_view(), name='record-list'),
    path('records/<int:id>/', RecordDetail.as_view(), name='record-detail')
]
