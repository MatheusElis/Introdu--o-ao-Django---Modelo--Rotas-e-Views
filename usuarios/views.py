from django.shortcuts import render

def cadastro(request):
    if request.method == 'POST':
        print('Usuario Cadastrado com Sucesso')
    return render(request, 'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    pass