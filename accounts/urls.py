from django.urls import path
from .views import SignUpview
urlpatterns = [
    path('accounts/',SignUpview.as_view(),name='signup'),
]