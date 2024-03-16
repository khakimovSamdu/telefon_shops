from django.urls import path
from .views import get_add, get_all, get_brends, brend_item_delete, brend_item_update, brend_all, get_smartphone_id
from .views import Homepage

urlpatterns = [
    path('add/', get_add),
    path('all/', get_all),
    path('brends/', get_brends),
    path('delete/<int:id>/', brend_item_delete),
    path('update/<int:id>/', brend_item_update),
    path('<brend>/all/', brend_all),
    path('get/<int:id>/', get_smartphone_id),
    path('', Homepage.as_view(), name='home'),
   
]
 