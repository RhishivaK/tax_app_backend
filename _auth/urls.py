from django.urls import path

from _auth.views import AuthViewSet

urlpatterns = [
    path('login/', AuthViewSet.as_view({'post': 'login'})),
    path('logout/', AuthViewSet.as_view({'delete': 'logout'})),
    path('signup/', AuthViewSet.as_view({'post': 'signup'})),
    path('me/', AuthViewSet.as_view({'get': 'me'}))
]

