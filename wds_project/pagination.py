from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10  # padrão
    page_size_query_param = 'page_size'  # permite ?page_size=...
    max_page_size = 50  # limite máximo
