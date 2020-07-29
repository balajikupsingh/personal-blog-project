
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
from django.urls import include
#from django.conf.urls.defaults import patterns, include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home , name='home'),
    path('blog/', include('blog.urls'))
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
