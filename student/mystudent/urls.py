from django.urls import path
from .views import StudentCreateView, StudentListView, StudentDetailView, StudentUpdateView, StudentDeleteView
urlpatterns = [
    path('form/', StudentCreateView.as_view(), name='student-form'),
    path('', StudentListView.as_view(), name='student-list'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete-student'),
]
