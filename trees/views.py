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