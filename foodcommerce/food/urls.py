from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    #food/home/
    path('home/',views.home,name='home'),
    ##food/1
    path("<int:item_id>/",views.detail,name='detail'),
    path('add',views.create_item,name='create_item'),
    path('update/<int:id>',views.update_item,name='update_item'),
    path('delete/<int:id>',views.delete_item,name='delete_item'),
]


