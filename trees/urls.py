from django.urls import path

from .views import TreeListView, TreeDetailView, SearchResultsListView

urlpatterns = [
    path('', TreeListView.as_view(), name='tree_list'),
    path('<uuid:pk>', TreeDetailView.as_view(), name='tree_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]