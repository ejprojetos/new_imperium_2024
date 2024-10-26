from django.contrib import admin
from django.urls import path, include

from .views import ClinicAdminViewSet


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     PatientViewSet,
#     DoctorViewSet,
#     ReceptionistViewSet,
#     ClinicAdminViewSet
# )

router = DefaultRouter()
router.register(r'patients', ClinicAdminViewSet)
# router.register(r'doctors', DoctorViewSet)
# router.register(r'receptionists', ReceptionistViewSet)
# router.register(r'clinic-admins', ClinicAdminViewSet)


urlpatterns = [
    # path('users/admin-clinic', ClinicAdminViewSet.as_view(), name='create-admin-clinic'),
    path('', include(router.urls)),  # Use the router's URLs

]

# urlpatterns = [
#     path('users/', UserView.as_view()),
#     path('patients', PatientViewSet.as_view()),
#     path('doctors', DoctorViewSet.as_view()),
#     path('', include(router.urls)),  # Use the router's URLs
# ]
