from rest_framework.pagination import LimitOffsetPagination


class MyPageNumberPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param='lim'
    offset_query_param='off'
    max_limit=6
    
