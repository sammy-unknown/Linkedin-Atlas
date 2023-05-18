from django.urls import path
from Crunchbase import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('crunchbase',views.Collect,name="Data_Anyaltics"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
