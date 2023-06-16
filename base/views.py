from django.shortcuts import render, redirect
from base.form import ItemForm
from base.models import Item

# Create your views here.
def principal(request):
    
    itens = Item.objects.all()
    return render(request, 'principal.html', {'itens': itens})

def adicionarItem(request):
    
    form = ItemForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            redirect('/')
    
    context = { 'form': form }
    return render(request, 'adicionar-item.html', context)
