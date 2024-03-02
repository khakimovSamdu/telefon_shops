from django.urls import path
from .views import get_add, get_all, get_brends, brend_item_delete, brend_item_update, brend_all

urlpatterns = [
    path('add/', get_add),
    path('all/', get_all),
    path('brends/', get_brends),
    path('<brend>/<int:id>/delete/', brend_item_delete),
    path('<brend>/<int:id>/update/', brend_item_update),
    path('<brend>/all/', brend_all),
   
]
