from rest_framework import generics,permissions
from .models import *
from .serializers import *


class LessonApiView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ProductLessonList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductLessonSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(products__id=product_id)
    





        



