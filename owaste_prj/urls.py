from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owaste/', include("owaste.urls")),
    # common
    path('common/', include('common.urls')),
    # pybo
    path('pybo/', include('pybo.urls')),
    # chat
    path("chat/", include("chat.urls")),
    
    path('', RedirectView.as_view(url='/owaste/index'), name="root"),

]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
