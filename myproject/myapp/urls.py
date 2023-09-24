from django.urls import path
from . import views

urlpatterns = [
    path('api/lessonlist',views.LessonApiView.as_view()),
    path('api/productlessons/<int:product_id>/',views.ProductLessonList.as_view(),name='productlessonlist'),
    
]


