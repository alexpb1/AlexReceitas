from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import  User
from django.contrib import auth, messages
from Receitas.models import Receita

def cadastro(request):
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

def cria_receita(request):
    if request.method =='POST':
        nome_receita=request.POST['nome_receita']
        ingredientes=request.POST['ingredientes']
        modo_preparo=request.POST['modo_preparo']
        tempo_preparo=request.POST['tempo_preparo']
        rendimento=request.POST['rendimento']
        categoria=request.POST['categoria']
        foto_receita=request.FILES['foto_receita']
        user=get_object_or_404(User, pk=request.user.id)
        receita=Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,
        tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)
        user.save()
        return redirect('dashboard')
    else:
         return render(request, 'usuarios/cria_receita.html')

def deleta_receita(request, receita_id):
    receita=get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):
    receita=get_object_or_404(Receita, pk=receita_id)
    receita_a_editar={'receita':receita}
    return render(request, 'usuarios/edita_receita.html', receita_a_editar)

def atualiza_receita(request):
    if request.method =='POST':
        receita_id=request.POST['receita_id']
        r=Receita.objects.get(pk=receita_id)
        r.nome_receita=request.POST['nome_receita']
        r.ingredientes=request.POST['ingredientes']
        r.modo_preparo=request.POST['modo_preparo']
        r.tempo_preparo=request.POST['tempo_preparo']
        r.rendimento=request.POST['rendimento']
        r.categoria=request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita=request.FILES['foto_receita']
        r.save()
        return redirect('dashboard')
    
