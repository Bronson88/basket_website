from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class BasketListView(ListView):
    model = models.Basket
    context_object_name = 'baskets'


class BasketDetailView(DetailView):
    model = models.Basket
