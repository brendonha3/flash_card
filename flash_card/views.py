from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Card

class IndexView(generic.ListView):
    template_name = 'flash_card/index.html'
    context_object_name = 'query'

    def get_queryset(self): 
        return Card.objects.all()

class DetailView(generic.DetailView):
    model = Card
    template_name = 'flash_card/detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class AddCardView(generic.DetailView):
    model = Card
    template_name = 'flash_card/editcard.html' 
