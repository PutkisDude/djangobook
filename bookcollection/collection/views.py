from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from collection.models import Book


class CollectionCreateView(CreateView):
	model = Book
	fields = ["name", "author", "year"]

class CollectionListView(ListView):
	paginate_by = 10
	model = Book

	def get_context_data(self, **kwargs):
		context = super(CollectionListView, self).get_context_data(**kwargs)
		context['book_moderator'] = self.request.user.groups.filter(name__in=['book_mod']).exists()
		return context
	
class CollectionDetailView(DetailView):
	model = Book

class CollectionUpdateView(UpdateView):
	model = Book
	fields = ["name", "author", "year"]
	success_url = reverse_lazy("book_collection")

class CollectionDeleteView(DeleteView):
	model = Book
	success_url = reverse_lazy("book_collection")
