from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'accounts.views.error_404_handler'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('products.urls')),
    path('',include('accounts.urls')),
    path('account/', include('accounts.urls'),name='home')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)