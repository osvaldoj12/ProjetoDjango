from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SugestoesForm

def get_name(request):
    if request.method == 'POST':
        form = SugestoesForm(request.POST)
        if form.is_valid():
            SugestoesForm = form.save(commit=False)
            SugestoesForm.save()
            return HttpResponseRedirect('/ouvidoria/')

    else:
        form = SugestoesForm()

    return render(request, 'Sugestao.html', {'form': form})