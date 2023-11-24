"""
URL configuration for room_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from room.views import RoomAPIList, RoomViewSet, BookingViewSet, UserRegistrationView, RoomViewSetTimeStamp, UserBookingsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/room_list/', RoomAPIList.as_view()),
    path('api/room/', RoomViewSet.as_view({'get': 'list'})),
    path('register/', UserRegistrationView.as_view()),
    path('bookings/', BookingViewSet.as_view({'post': 'create'})),
    path('api/rooms/', RoomViewSetTimeStamp.as_view({'get': 'list'})),
    path('users/<int:user_id>/bookings/', UserBookingsView.as_view())

]
