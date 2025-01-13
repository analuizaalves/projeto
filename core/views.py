from django.shortcuts import render, redirect
from .forms import InformaForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = InformaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Verifique se todos os campos foram preenchidos corretamente')
    else:
        form = InformaForm()
    return render(request, 'index.html', {'form': form})
