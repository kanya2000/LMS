from django.urls import path
from . import views

urlpatterns = [

    #enquiry API endpoints
    path('api/enquiries/', views.EnquiryListCreateView.as_view(), name='enquiry-create-list'),
    path('api/enquiries/<int:pk>/', views.EnquiryDetailView.as_view(), name='enquiry-retrieve-update-destroy'),

    path('api/courses/', views.CourseListCreateView.as_view(), name='course-create-list'),
    path('api/courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-retrieve-update-destroy'),

    #certfication API endpoints
    path('api/certfications/', views.CertficationListCreateView.as_view(), name='certfication-create-list'),



]