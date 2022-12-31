from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bendrija, Atliktas_Darbas, Ataskaita
from .forms import BendrijaForm, Atliktas_DarbasForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def bendrijos_view(request):
    """ A view to show all Bendrijos """

    bendrijos = Bendrija.objects.all()

    template = 'home/bendrijos.html'
    context = {
        'bendrijos': bendrijos,
    }

    return render(request, template, context)


def bendrijos_turinys_view(request, bendrija_id):
    """ A view to show Bendrijos Turini """

    bendrija = get_object_or_404(Bendrija, pk=bendrija_id)
    darbai = bendrija.atliktas_darbas.all
    ataskaitos = bendrija.ataskaita.all

    template = 'home/bendrijos_turinys.html'
    context = {
        'bendrija': bendrija,
        'darbai': darbai,
        'ataskaitos': ataskaitos,
    }

    return render(request, template, context)


@login_required
def add_bendrija_view(request):

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    form = BendrijaForm

    if request.method == 'POST':
        form = BendrijaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('bendrijos'))

    template = 'home/add_bendrija.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_darbas_view(request, bendrija_id):

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    bendrija = get_object_or_404(Bendrija, pk=bendrija_id)

    form = Atliktas_DarbasForm

    if request.method == 'POST':
        form = Atliktas_DarbasForm(request.POST)
        if form.is_valid():
            form.bendirja = bendrija
            form.save()
            return redirect(reverse('bendrijos'))

    template = 'home/darbas_form.html'
    context = {
        'bendrija': bendrija,
        'form': form,
    }

    return render(request, template, context)
