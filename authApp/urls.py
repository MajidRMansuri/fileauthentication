from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view
from .form import LoginForm,ChangePasswordForm,ForgetPasswordForm,SetResetPasswordForm

urlpatterns = [
    path('', views.Registration.as_view(),name='index'),
    path('deleteservice/<int:pk>',views.deleteservice,name='deleteservice'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('account/login/', auth_view.LoginView.as_view(template_name='login.html',form_class=LoginForm),name='login'),
    path('Service/', views.ServiceView.as_view(),name='service'),

    # Change PAssword
    path('PasswordChange/',auth_view.PasswordChangeView.as_view(template_name='changePassword.html',form_class=ChangePasswordForm,success_url='/changepassworddone/'),name='PasswordChange'),
    path('changepassworddone/',auth_view.PasswordChangeDoneView.as_view(template_name='done.html'),name='changepassworddone'),
    
    # PAssword Reset
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='forgetPassword.html',form_class=ForgetPasswordForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='resetPassword.html',form_class=SetResetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='done.html'),name='password_reset_complete'),



]
