from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import  User
from django.contrib import auth, messages
from Receitas.models import Receita

def cadastro(request):
    """Utilizando o method POST, atribui o valor de nome, email e password digitados
    no fumulário e etribui as respectivas variaveis. Depois são feitas algumas 
    validações nos dados. Combinamos as variaveis para forma um objeto user, e por 
    ultimo o user é salvo"""
    if request.method=='POST':
        nome=request.POST['nome']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if not nome.strip():
            messages.error(request, 'Digite um nome válido para o usuário')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'O email não ser espaço em branco')
            return redirect('cadastro')
        if password !=password2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        user=User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect ('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """Utilizando o method POST, o email e password digitados no formulario
    são atribuídos a duas variáveis, depois de validações do dados, o sistema
    verificará se email e password conferem e faz o login"""
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if email=="" or password== "":
            messages.error(request, 'Para fazer Login é necessário digitar seu endereço de email.')
            return redirect ('login')
        if User.objects.filter(email=email).exists():
            nome=User.objects.filter(email=email).values_list('username', flat=True).get()
            user=auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
        else:
            messages.error(request, 'Email e/ou senha incorretos, ou não cadastrados')
            return redirect ('login')
        return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def dashboard(request):
    """Filtra as receitas criadas pelo usuario logado e 
    e exibe no dashboard"""
    if request.user.is_authenticated:
        id=request.user.id
        receitas=Receita.objects.order_by('-date_receita').filter(pessoa=id)

        dados={
            'receitas':receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index' )

def logout(request):
    auth.logout(request)
    return redirect('index')


    
