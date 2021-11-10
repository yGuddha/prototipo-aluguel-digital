from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LoginView,name='login'),
    path('imovel/',views.ImovelDescView,name='info-imovel'),
    path('register/',views.RegisterView,name='register'),
    path('disponiveis/',views.ImoveisDisponiveisView,name='imoveis-disponiveis'),
    path('home/',views.ImoveisAlugadosView,name='imoveis-alugados'),
    path('profile/',views.ProfileView,name='profile'),
    path('forgot/',views.ForgotPassView,name='forgot-pass'),
    path('forgot/code',views.ForgotPassCodeView,name='forgot-pass-code'),
    path('forgot/redefine',views.ForgotPassRedefineView,name='forgot-pass-redefine'),
]