from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    path("", views.index, name="challenges_base_path"),
    path("<int:month>", views.month_by_number, name='month_by_number'),
    path("<str:month>", views.month, name='month_by_string')

]
