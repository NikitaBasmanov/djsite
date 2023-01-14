from django.urls import path, include
from .views import user_login, register
from django.contrib.auth import views as authViews

urlpatterns = [
    path('login/', user_login, name='exist'),
    path('register/', register, name='register'),
    path('logout/', authViews.LogoutView.as_view(next_page='/'), name='logout'),
    path('password-reset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]