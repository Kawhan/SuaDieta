from dietas.models import Dieta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from dietas.forms import dietaform


# Create your views here.
def index(request):
    dietas = Dieta.objects.all()
    
    paginator = Paginator(dietas, 3)
    page = request.GET.get('page')
    dietas_per_page = paginator.get_page(page)

    dados = {}
    
    dados['dietas'] = dietas_per_page
    dados["title"] = "Home"
    
    return render(request, 'dietas/index.html', dados)

def teste(request):
    
    return render(request, 'dietas/teste.html')


    
@login_required
def forms(request):
    context = {}

    user  = get_object_or_404(User, pk=request.user.id)
    form = dietaform(request.POST or None, initial={'pessoa': user})


    if form.is_valid():
        form.save()
        return redirect('index')

    context["form"] = form  
    context["user"] = user
    context["title"] = "Criar Dietas"

    return render(request, "dietas/forms.html", context)  

@login_required
def change_dieta(request, dieta_id):
    nome = request.user
    
    context ={}
    dieta = get_object_or_404(Dieta, pk=dieta_id) 
    
    if dieta.pessoa !=  nome:
        messages.error(request,"Você não pode realizar essa operação!")
        return redirect("index")
    
    form = dietaform(request.POST or None, instance= dieta)
    
    if form.is_valid():
        # print(form.id)
        form.save()
        messages.success(request, "Dieta alterada com sucesso!")
        return redirect('minhas_receitas')
    
    context["form"] = form
    context["title"] = "Alterar Dieta"
    
    return render(request, "dietas/forms.html", context) 

@login_required
def delete_dieta(request, dieta_id):
    nome = request.user
    
    context ={}
    dieta = get_object_or_404(Dieta, pk=dieta_id) 
    
    if dieta.pessoa !=  nome:
        messages.error(request,"Você não pode realizar essa operação!")
        return redirect("index")
    
    context['dieta'] = dieta
    context["title"] = "Deletar Dieta"
    
    if request.method =="POST":
        # delete object
        dieta.delete()
        # after deleting redirect to
        # home page
        messages.success(request, "Dieta apagada com sucesso!")
        return redirect("minhas_receitas")
 
    return render(request, "dietas/delete.html", context)
     
@login_required
def view_dieta(request, dieta_id):
    context ={}
    dieta = get_object_or_404(Dieta, pk=dieta_id) 
    
    context['dieta'] = dieta
    context["title"] = "Visualizar Dieta"
    
    return render(request, "dietas/views.html", context)

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        dietas = Dieta.objects.order_by('-data_inicio').filter(pessoa=id)
        
        dados = {}
        
        dados['dietas'] = dietas
        dados["title"] = "Minhas Dietas"

        return render(request, 'dietas/dashboard.html', dados)
    else:
        return redirect('index')
    
def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect("index")
