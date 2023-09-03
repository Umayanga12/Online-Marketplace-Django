from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import core.urls

urlpatterns = [
                  # add all the urls at the core/ urls
                  path('', include('core.urls')),
                  # all the urls will be there which are in the item/url.py file
                  path('items/', include('item.url')),
                  # add the all the urls at the dashboard
                  path('dashboard/',include('dashboard.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
