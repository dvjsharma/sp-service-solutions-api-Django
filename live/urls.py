"""
Brief: Django urls.py file.

Description: This file contains the URL patterns for the Django live app.

Author: Divij Sharma <divijs75@gmail.com>
"""

from django.urls import path, re_path
from .views import InstanceListCreateView, InstanceRetrieveUpdateDestroyView, InstanceTypeStatusView
from .views import InstanceCSVView, InstanceJSONView
from .views import InstanceOrganizationView
from .views import SocialUserTokenObtainPairView
from .views import ProviderAuthView
from .views import GoogleOAuthCallbackView

urlpatterns = [
    path('instance/info', InstanceTypeStatusView.as_view(), name='instance-status'),
    path('instance/', InstanceListCreateView.as_view(), name='instance-list-create'),
    path('instance/<str:hash>/', InstanceRetrieveUpdateDestroyView.as_view(), name='instance-detail'),
    path('instance/<str:hash>/login', SocialUserTokenObtainPairView.as_view(), name='instance-login'),
    path('instance/CSV/<str:hash>/', InstanceCSVView.as_view(), name='instance-csv-post'),
    path('instance/CSV/<str:hash>/<str:username>', InstanceCSVView.as_view(), name='instance-csv'),
    path('instance/JSON/<str:hash>/', InstanceJSONView.as_view(), name='instance-json-post'),
    path('instance/JSON/<str:hash>/<str:username>', InstanceJSONView.as_view(), name='instance-json'),
    path('instance/ORG/<str:hash>/', InstanceOrganizationView.as_view(), name='instance-orgs'),
    path('instance/ORG/<str:hash>/<str:username>', InstanceOrganizationView.as_view(), name='instance-orgs'),
    re_path(r"^(?P<hash>\w+)/(?P<provider>\S+)/$", ProviderAuthView.as_view(), name="provider-auth"),
    path('google-oauth2/callback/', GoogleOAuthCallbackView.as_view(), name='google-oauth2-callback'),
]
