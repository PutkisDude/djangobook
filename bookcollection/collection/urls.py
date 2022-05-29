from django.urls import path
from . import views

urlpatterns = [
    path('', views.CollectionListView.as_view(), name="book_collection"),
	path('new/', views.CollectionCreateView.as_view(), name="new_book"),
	path('<int:pk>', views.CollectionDetailView.as_view(), name="book_detail"),
	path('<int:pk>/update', views.CollectionUpdateView.as_view(), name="book_update"),
	path('<int:pk>/delete', views.CollectionDeleteView.as_view(), name="book_delete"),
	
]
