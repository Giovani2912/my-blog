from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# DEVEMOS PASSAR ESSA LINHA SEMPRE QUE NOSSA APLICAÇÃO FOR DE REACT+DJANGO,
# ELA É EXTRAMAMENTE IMPORTANTE, POIS CONECTA AS ROTAS DO BACK COM AS ROTAS DO FRONT
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]