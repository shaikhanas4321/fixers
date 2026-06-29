from django.urls import path
from . import views

app_name='services'

urlpatterns = [
    path('', views.index , name="index"),
    path('completion/' , views.completion ,name="completion"),
    path('provider/' , views.provider ,name="provider"),
    path('listing/',views.listing ,name="listing"),
    path('calling/<str:provider>' , views.calling ,name="calling"),
    path('jobs/<str:provider>',views.jobs,name="jobs"),
   path('status_update/<int:j_id>' ,views.status_update)

]