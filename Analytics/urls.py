from django.urls import path
from Analytics import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('data',views.Analytics,name="Data_Anyaltics"),
    path('refresh-data/', views.refresh_data, name='refresh_data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
