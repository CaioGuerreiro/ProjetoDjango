from django.shortcuts import render, redirect
from usuarios.forms import loginForms, cadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request):
    form = loginForms()

    if request.method == 'POST':
        form = loginForms(request.POST)
    
        if form.is_valid():
            nome = form['nomeLogin'].value()
            senha = form['senhaLogin'].value()
    
            usuario = auth.authenticate(request, username=nome, password=senha)

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, "usuário logado com sucesso")
                return redirect('index')
                
            else:
                messages.error(request, "falha ao logar usuário")
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})
def cadastro(request):


    form = cadastroForms

    if request.method == 'POST':
        form = cadastroForms(request.POST)

       
        
        if form.is_valid():
             
             
             nome = form["nomeCadastro"].value()
             email = form["emailCadastro"].value()
             senha = form["senhaCadastro"].value()

             if User.objects.filter(username= nome).exists():
                 messages.error(request, 'Nome de usuário já existe')
                 return redirect('cadastro')
             
             usuario = User.objects.create_user(
                 username=nome,
                 email=email,
                 password=senha
             )
             messages.success(request, 'Usuário cadastrado com sucesso')
             usuario.save()
             return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})
def logout(request):
    auth.logout(request)
    messages.success(request,"Logout efetuado com sucesso")
    return redirect('login')