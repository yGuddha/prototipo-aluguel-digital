from django.shortcuts import render

# Create your views here.
def LoginView(request):
    return render(request, 'login.html')

def ImovelDescView(request):
    return render(request, 'imovel-desc.html')

def RegisterView(request):
    return render(request, 'register.html')

def ImoveisDisponiveisView(request):
    return render(request, 'imoveis.html', {'pagina':'disponiveis'})

def ImoveisAlugadosView(request):
    return render(request, 'imoveis.html', {'pagina':'alugados'})

def ProfileView(request):
    return render(request, 'profile.html')

def ForgotPassView(request):
    return render(request, 'forgot-pass.html')

def ForgotPassCodeView(request):
    return render(request, 'forgot-pass-code.html')

def ForgotPassRedefineView(request):
    return render(request, 'forgot-pass-redefine.html')