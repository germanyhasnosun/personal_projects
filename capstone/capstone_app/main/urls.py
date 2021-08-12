
from django.urls import path
from main.views import homepage, risk_group, get_risk_data, about_us,cancer_screening
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', homepage),
    path('risk_group/', risk_group),
    path('get_data/<data_type>', get_risk_data),
    path('about_us/', about_us),
    path('cancer_screening/', cancer_screening),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)