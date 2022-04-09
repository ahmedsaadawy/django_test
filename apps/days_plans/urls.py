from django.urls import path
from apps.days_plans import views

urlpatterns = [
    # static routes
    path('static/saturday/', views.saturday),
    path('static/sunday/', views.sunday),
    path('static/monday/', views.monday),
    path('static/tuesday/', views.tuesday),
    path('static/wednesday/', views.wednesday),
    path('static/thursday/', views.thursday),
    path('static/friday/', views.friday),
    # dynamic routes
    # ordering the urls has effect
    # int must come before str. cus int can be parsed as string
    path('dynamic/', views.days_list),
    path('dynamic/<int:order>/', views.day_order, name="plans-dynamic-order"),
    path('dynamic/<str:name>/', views.day_name, name="plans-dynamic-name"),
]
