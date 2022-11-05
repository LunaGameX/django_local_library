from django.urls import path
from . import views
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    path(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
    path('<int:fav_id>/', views.favorite, name='add-favorite-book'),
    path('my-favorite-book/', views.view_favorite_book, name='my-favorite-book'),
]



