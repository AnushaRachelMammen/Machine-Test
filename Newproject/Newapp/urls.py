from django.urls import path
from Newapp import views
urlpatterns=[
    path('product_page/',views.product_page,name="product_page"),
    path('savedata/',views.savedata,name="savedata"),
    path('display_product/',views.display_product,name="display_product"),
    path('delete_product/<int:dataid>/',views.delete_product,name="delete_product"),
    path('edit_product/<int:dataid>/',views.edit_product,name="edit_product"),
    path('update_product/<int:dataid>/',views.update_product,name="update_product"),
    path('orderpage/',views.orderpage,name="orderpage"),
    path('saveorderdata/',views.saveorderdata,name="saveorderdata")
]