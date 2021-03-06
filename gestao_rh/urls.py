from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('funcoes/', include('apps.funcoes.urls')),
    path('eventos/', include('apps.eventos.urls')),
    path('beneficios/', include('apps.beneficios.urls')),
    path('horarios/', include('apps.horarios.urls')),
    path('contratos/', include('apps.contratos.urls')),
    path('movimentacoes/', include('apps.movimentacoes.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('dependentes_func/', include('apps.dependentes_func.urls')),
    path('beneficios_func/', include('apps.beneficios_func.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)