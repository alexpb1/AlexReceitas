from django.shortcuts import redirect, render
from django.contrib.auth.models import  User
from django.contrib import auth

def cadastro(request):
    if request.method=='POST':
        nome=request.POST['nome']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if not nome.strip():
            print('O nome não ser espaço em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O email não ser espaço em branco')
            return redirect('cadastro')
        if password !=password2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print("Usuário já cadastrado")
            return redirect('cadastro')
        user=User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect ('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if email=="" or password=="":
            print('Os campos email e senha não pode ficar em branco')
            return redirect ('login')
        print(email, password)
        if User.objects.filter(email=email).exists():
            nome=User.objects.filter(email=email).values_list('username', flat=True).get()
            user=auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
                print('Login realizado')
        return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index' )

def logout(request):
    auth.logout(request)
    return redirect('index')
