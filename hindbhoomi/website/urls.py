from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("SignUp/", views.Signup_view, name="signup"),
    path('login/', views.Login_view, name="login"),
    path('logout/', views.Logout_view, name="logout"),
    path('rail/', views.rail, name="rail"),
    path('bus/', views.Bus, name="bus"),
    path('Flight/', views.Flight, name="flight"),
    path('Booking/<int:id>/', views.Booking, name="booking"),
    path('Bus_Booking/<int:id>/', views.Bus_Bookings, name="bus_booking"),
    path('Flight_Booking/<int:id>/', views.Flight_Bookings, name="flight_booking"),

    
    path('tour-guide/', views.TourGuide, name="tour-guide"),
    path('state-wise-tour-guide/<int:state_id>/', views.state_wise_tourism, name="state-wise-tourism"),
    
    
    # path('find_train/<train_id>,', views.find_train_btw_station, name="find_train")
]