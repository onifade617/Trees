from django.views.generic import ListView, DetailView

from .models import Tree

class TreeListView(ListView):
    model = Tree

    context_object_name = 'tree_list'
    template_name = 'trees/tree_list.html'


class TreeDetailView(DetailView): # new
    model = Tree
    context_object_name = 'tree'
    template_name = 'trees/tree_detail.html'