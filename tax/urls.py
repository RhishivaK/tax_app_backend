from django.urls import path

from tax.views import (
    IncomeTaxPolicyListAPIView, IncomeTaxListAPIView, IncomeTaxPolicyViewset
)

urlpatterns = [
    path('policy/', IncomeTaxPolicyViewset.as_view({'post': 'create'})),
    path('policy/list/', IncomeTaxPolicyListAPIView.as_view()),
    path('record/list/', IncomeTaxListAPIView.as_view())
]

