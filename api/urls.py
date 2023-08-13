from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListUpdateDelete, BookListView

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r"books", views.BookViewSet, basename="book")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("books/", BookListView.as_view()),  # get, post request handle korbe
    path(
        "books/<int:pk>/", BookListUpdateDelete.as_view()
    ),  # update, delete request handle korbe
    # path('books/', views.BookListCreateAPIView.as_view()), # get, post request handle korbe
    # path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()), # update, delete request handle korbe
    path("", include(router.urls)),
]
