from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bendrija, Atliktas_Darbas
from .forms import BendrijaForm

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

    template = 'home/bendrijos_turinys.html'
    context = {
        'bendrija': bendrija,
        'darbai': darbai,
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
