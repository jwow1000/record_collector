from django.urls import path
from .views import Home, RecordList, RecordDetail, SpinListCreate, SpinDetail, SpinList, DjList, DjDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('records/', RecordList.as_view(), name='record-list'),
    path('records/<int:id>/', RecordDetail.as_view(), name='record-detail'),
    path('records/<int:record_id>/spins/', SpinListCreate.as_view(), name='spin-list'),
    path('records/<int:record_id>/spins/<int:id>', SpinDetail.as_view(), name='spin-detail'),
    path('spins/', SpinList.as_view(), name='spins-all'),
    path('djs/', DjList.as_view(), name='djs-all'),
    path('djs/<int:id>/', DjDetail.as_view(), name='dj-detail'),
]
