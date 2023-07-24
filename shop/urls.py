from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shop_site.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('shop/', shop, name="shop"),
    path('contactsSend/', contactSaveFunc, name="contactsSend"),
    path('cloth/<int:id>/', shopSingle, name = 'shopSingle')
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)