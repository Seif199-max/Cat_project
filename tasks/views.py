from .models import Category,Task
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import  generics,filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .permission import IsManagerOrReadOnly
from .serializers import CategorySerializer,TaskSerializer
# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'perpage'
    max_page_size = 10
    page_size = 2


class CategoryDetail(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # authentication_classes = [TokenAuthentication]
    pagination_class = CustomPagination
    #permission_classes = [ IsManagerOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class TasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    pagination_class = CustomPagination
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [ IsManagerOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['status']
    search_fields = ['title']
    ordering_fields = ['priority',  ]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    serializer_class = TaskSerializer


class TaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #authentication_classes = [TokenAuthentication]
    pagination_class = CustomPagination
    #permission_classes = [ IsManagerOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
