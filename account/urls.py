from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'account'

urlpatterns = [
	# path('login/', views.user_login, name='login'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('', views.dashboard, name='dashboard'),
	# change password urls
	path('password_change/',
					auth_views.PasswordChangeView.as_view(),
					name='password_change'),
	path('passwrod_change/done/', 
					auth_views.PasswordChangeDoneView.as_view(),
					name='password_change_done'),
	# resetting password urls
	path('passwrod_reset',
						auth_views.PasswordResetView.as_view(),
						name='password_reset'),
	path('passwrod_reset/done/',
						auth_views.PasswordResetDoneView.as_view(),
						name='password_reset_done'),
	path('reset/<uidb64>/<token>',
						auth_views.PasswordResetConfirmView.as_view(),
						name='password_reset_confirm'),
	path('reset/done/',
				auth_views.PasswordResetCompleteView.as_view(),
				name='password_reset_complete'),
	# path('', include('django.contrib.auth.urls')), with this url we 
	# do not need to create a url for password change or reset manually.
	path('register/', views.register, name='register'),
	path('edit/', views.edit, name='edit'),
]