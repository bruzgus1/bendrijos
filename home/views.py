from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Bendrija
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
