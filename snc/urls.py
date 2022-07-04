from django.contrib import admin
from django.urls import path, include
from homepage.views import IndexView

# Sólo para deploy .........
from django.conf import settings
from django.conf.urls.static import static
#  .........

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('erp/', include('erp.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
