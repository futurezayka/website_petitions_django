from django.shortcuts import render, redirect
from .models import Peticions
from .forms import PeticionsForm
from django.views.generic import DetailView, UpdateView
from mainapp.models import User



def petitions(request):
    petition = Peticions.objects.order_by("-date")
    return render(request, 'peticions/peticions_home.html', {"peticions": petition})


class PeticionsDetailView(DetailView):
    model = Peticions
    template_name = 'peticions/details_view.html'
    context_object_name = 'peticion'


class PeticionUpdateView(UpdateView):
    model = Peticions
    template_name = 'peticions/create.html'
    form_class = PeticionsForm


def deleteItem(request, id):
    item = Peticions.objects.get(id=id)
    item.delete()
    return redirect('/petitions')

def get_absolute_url(self):
    return '{self.path}'

def create(request):
    error = ""
    if request.method == 'POST':
        form = PeticionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/petitions')
        else:
            error = "Form was incorrect"

    form = PeticionsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'peticions/create.html', data)
