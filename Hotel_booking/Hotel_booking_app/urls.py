from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
app_name='hotel'
urlpatterns = [
    path('',views.Home,name='home'),
    path('signin/',views.Sign_up,name='signin'),
    path('login/',views.Log_in,name='login'),
    
    path('profile/<int:id>/',views.Profile,name='profile'),
    path('logout/',views.log_out,name='logout'),
    path('userhome/',views.userhome,name='userhome'),
    path('update_profile/<int:id>/',views.ProfileUpdate.as_view(),name='update_profile'),
    path('search/',views.search_view.as_view(),name='search'),
    path('room/<str:hotel>/',views.Room_view,name='rooms')





] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
