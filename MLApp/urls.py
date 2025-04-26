from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MLApp', views.DiagnosisView)
urlpatterns = [
    path('form/', views.main_form, name='mainform'),
    path('api/', include(router.urls)),
    path('status/',views.diagnose),

]
