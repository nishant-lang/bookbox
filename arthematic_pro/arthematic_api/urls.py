
from django.urls import path
from arthematic_api import views

urlpatterns = [
  
   path('',views.api_overview,name='overview'),
   path('add/<int:num1>/<int:num2>',views.add,name='mul'),
   path('sub/<int:num1>/<int:num2>',views.sub,name='mul'),
   path('mul/<int:num1>/<int:num2>',views.mul,name='mul'),
   path('div/<int:num1>/<int:num2>',views.div,name='mul'),
  
]