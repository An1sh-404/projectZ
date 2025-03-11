from django.urls import path
from .views import (HomePageView,
                    RecordCreateView,
                    RecordDeleteView,
                    RecordDetailView,
                    RecordListView,
                    RecordUpdateView,
                    )

urlpatterns = [
    path("",HomePageView.as_view(),name="home"),
    path("dashboard",RecordListView.as_view(),name="dashboard"),
    path("dashboard/record/new",RecordCreateView.as_view(),name="record_new"),
    path("dashboard/record/<int:pk>",RecordDetailView.as_view(),name="record_detail"),
    path("dashboard/record/<int:pk>/edit",RecordUpdateView.as_view(),name="record_edit"),
    path("dashboard/record/<int:pk>/delete",RecordDeleteView.as_view(),name="record_delete"),
]