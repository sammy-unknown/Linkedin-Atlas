from django.urls import path
from Analytics import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('data',views.Analytics,name="Data_Anyaltics"),
    path('company/<str:pk>/', views.company_website, name='company_website'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
