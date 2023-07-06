from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Bendrija, Atliktas_Darbas, Ataskaita
from .forms import BendrijaForm, Atliktas_DarbasForm, AtaskaitaForm

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


@login_required
def add_ataskaita_view(request, bendrija_id):

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    bendrija = get_object_or_404(Bendrija, pk=bendrija_id)

    form = AtaskaitaForm

    if request.method == 'POST':
        form = AtaskaitaForm(request.POST)
        if form.is_valid():
            form.bendirja = bendrija
            form.save()
            return redirect(reverse('bendrijos'))

    template = 'home/ataskaita_form.html'
    context = {
        'bendrija': bendrija,
        'form': form,
    }

    return render(request, template, context)


def edit_bendrija_view(request, ataskaita_id):
    """ A view to edit Bendrijos name """

    ataskiata = get_object_or_404(Ataskaita, id=ataskaita_id)

    if request.method == 'POST':
        existing_ataskaita = AtaskaitaForm(request.POST, instance=ataskiata)
        if existing_ataskaita.is_valid():
            existing_ataskaita.save()
            return redirect(reverse('bendrijos'))
    else:
        existing_ataskiata = AtaskaitaForm(instance=ataskiata)

    context = {
        'existing_bendrija': existing_bendrija,
        "bendrija": bendrija,
    }
    return render(request, 'home/edit_bendrija.html', context)


def edit_ataskaita_view(request, ataskaita_id):
    """ A view to edit Ataskaitos model """

    ataskaita = get_object_or_404(Ataskaita, id=ataskaita_id)

    if request.method == 'POST':
        existing_ataskaita = AtaskaitaForm(request.POST, instance=ataskaita)
        if existing_ataskaita.is_valid():
            existing_ataskaita.save()
            return redirect(reverse('bendrijos'))
    else:
        existing_ataskaita = AtaskaitaForm(instance=ataskaita)

    context = {
        'existing_ataskaita': existing_ataskaita,
        "ataskaita": ataskaita,
    }
    return render(request, 'home/edit_ataskaita.html', context)


def edit_atliktas_darbas_view(request, darbas_id):
    """ A view to edit Atliktas_Darbas model """

    atliktas_darbas = get_object_or_404(Atliktas_Darbas, id=darbas_id)

    if request.method == 'POST':
        existing_atliktas_darbas = Atliktas_DarbasForm(request.POST, instance=atliktas_darbas)
        if existing_atliktas_darbas.is_valid():
            existing_atliktas_darbas.save()
            return redirect(reverse('bendrijos'))
    else:
        existing_atliktas_darbas = Atliktas_DarbasForm(instance=atliktas_darbas)

    context = {
        'existing_atliktas_darbas': existing_atliktas_darbas,
        "atliktas_darbas": atliktas_darbas,
    }
    return render(request, 'home/edit_atliktas_darbas.html', context)


def bendrijos_turinys_darbas_view(request, bendrija_id):
    """ A view to show Bendrijos Turini """

    bendrija = get_object_or_404(Bendrija, pk=bendrija_id)
    darbai = bendrija.atliktas_darbas.all

    template = 'home/bendrijos_turinys_darbas.html'
    context = {
        'bendrija': bendrija,
        'darbai': darbai,
    }

    return render(request, template, context)


def bendrijos_turinys_ataskaita_view(request, bendrija_id):
    """ A view to show Bendrijos Turini """

    bendrija = get_object_or_404(Bendrija, pk=bendrija_id)
    ataskaitos = bendrija.ataskaita.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']

        queries = Q(mėnesis__icontains=query)
        ataskaitos = ataskaitos.filter(queries)

    template = 'home/bendrijos_turinys_ataskaita.html'
    context = {
        'bendrija': bendrija,
        'ataskaitos': ataskaitos,
        'search_term': query,
    }

    return render(request, template, context)
