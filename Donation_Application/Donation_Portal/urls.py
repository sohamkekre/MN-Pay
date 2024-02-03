from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordResetForm,MySetPasswordForm
from django.views.decorators.csrf import csrf_exempt
# MyPasswordChangeForm,MySetPasswordForm

urlpatterns = [
    path('', views.home, name='home'),
    
    path('portal/', views.portal, name = 'portal'),
    path('successful/',views.successful,name='successful'),
    path('cancelled/',views.cancelled,name='cancelled'),

    # path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    # path('NGO_Registration/login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('login/',views.CustomLoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),

    # added to resolve unexpected redirect to this path after login 
    path('accounts/profile/', views.home,name='home'),
    # path('profile/', views.home,name='home'),

    path('signup/',views.SignupView.as_view(),name='signup'),
    # path('NGO_Registration/',views.NGO_Registration,name='NGO_Registration'),
    path('NGP_Registration/',views.NGO_RegistrationView.as_view(),name="NGO_Registration"),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('transaction/', views.TransactionView.as_view(), name='transaction'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    ]
# ngo registration
#     path('ngo_registration/',views.ngo_registration,name='ngo_registration'),

# ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)