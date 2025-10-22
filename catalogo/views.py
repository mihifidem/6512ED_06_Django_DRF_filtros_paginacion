from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer

    # Habilitamos backends ya definidos por defecto en settings,
    # pero también podemos declararlos aquí explícitamente:
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtros exactos por campo
    filterset_fields = {
        # exactos:
        "genero": ["exact"],
        "autor": ["exact"],
        "stock": ["exact", "gte", "lte"],
        "rating": ["exact", "gte", "lte"],
        "publicado": ["exact", "gte", "lte"],  # rango por fecha
        "precio": ["exact", "gte", "lte"],     # rango por precio
        # búsquedas parciales (icontains) solo se soportan con un FilterSet personalizado (ver opción B)
    }

    # Búsqueda de texto (LIKE) en varios campos
    search_fields = ["titulo", "autor", "genero"]

    # Ordenación permitida
    ordering_fields = ["precio", "publicado", "rating", "titulo", "stock"]
    ordering = ["id"]  # orden por defecto
