from django.urls import path 

from . import views
from rider.models import ride
app_name = 'driver'


urlpatterns = [
	path('' , views.driverHome , name = "driverHome"),
    path('drive_or_ride.html/', views.drive_or_ride, name='drive_or_ride'),
    path('driver/index.html', views.index_view, name='driverIndex'),
	path('driverInfo' , views.driverInfo , name = "driverInfo"),
	path('driveProcess' ,views.searchRider , name = "searchRider"),
	path('accept' ,views.acceptRider , name = "acceptRider" ),
	path('end', views.endRide , name ="endRide"),
]

