from django.db.models import Q
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.views.generic import ListView, DetailView

from .models import Tree

class TreeListView(LoginRequiredMixin, ListView):
    model = Tree

    context_object_name = 'tree_list'
    template_name = 'trees/tree_list.html'
    login_url = 'account_login'


class TreeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView): # new
    model = Tree
    context_object_name = 'tree'
    template_name = 'trees/tree_detail.html'
    login_url = 'account_login'
    permission_required = 'trees.special_status'

class SearchResultsListView(ListView): # new
    model = Tree
    context_object_name = 'tree_list'
    template_name = 'trees/search_results.html'
    

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Tree.objects.filter(
            Q(title__icontains=query) | Q(farmer__icontains=query)
        )