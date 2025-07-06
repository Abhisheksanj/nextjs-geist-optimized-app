from django.urls import path
from .views import MobileNumberLookupView

urlpatterns = [
    path('lookup/', MobileNumberLookupView.as_view(), name='mobile-number-lookup'),
]
