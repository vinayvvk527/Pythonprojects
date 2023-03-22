
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Journal
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.
def home_view(request):
    return HttpResponse("journal/journal_list.html")

class JournalListView(ListView):
    model = Journal
    template_name = "journal/journal_list.html"
    context_object_name = "journal_list"
class JournalCreateView(CreateView):
    model = Journal
    template_name = 'journal/create_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journallist')
class JournalUpdateView(UpdateView):
    model = Journal
    template_name = 'journal/update_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journallist')
    
class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'journal/delete_journal_form.html'
    success_url = reverse_lazy('journallist')