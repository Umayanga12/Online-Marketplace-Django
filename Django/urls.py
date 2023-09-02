from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, contact

urlpatterns = [
                  path('', index, name='index'),
                  # all the urls will be there which are in the item/url.py file
                  path('items/', include('item.url')),
                  path('contact/', contact, name='contact'),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
