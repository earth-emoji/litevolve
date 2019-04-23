from django.urls import include, path

from .views import accounts, profile

urlpatterns = [
    path('logout/', accounts.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', accounts.UserSignUpView.as_view(), name='user_signup'),
    path('accounts/signup/success/', accounts.signup_success, name='success'),
    path('workspace/', include(([
        path('<int:pk>/', profile.user_profile, name='index'),
    ], 'accounts'), namespace='profile')),
]