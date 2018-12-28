from django.shortcuts import render

# Create your views here.
from .models import Paste

from django.views.generic.edit import CreateView
class PasteCreate(CreateView):
    model = Paste
    fields = ['text', 'name']

from django.views.generic.detail import DetailView
class PasteDetail(DetailView):
    model = Paste
    template_name = "pastebin/paste_detail.html"

from django.views.generic.list import ListView
class PasteList(ListView):
    model = Paste
    template_name = "pastebin/paste_list.html"
    queryset = Paste.objects.all()
    context_object_name = 'queryset'

from django.views.generic import DeleteView
from django.urls import reverse_lazy
class PasteDelete(DeleteView):
    model = Paste
    success_url = reverse_lazy('pastebin_paste_list')

from django.views.generic.edit import UpdateView
class PasteUpdate(UpdateView):
    model = Paste
    fields = ['text', 'name']
