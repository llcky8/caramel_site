from django.contrib import admin
from django.urls import path
from cases.admin import admin_site  # твой кастомный админ
from cases.views import cases_view, page_404_preview  # <--- добавлено здесь
from cases.views import cases_api
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin_site.urls),
    path('', cases_view, name='home'),
    path('cases/', cases_view, name='cases'),
    path('404-preview/', page_404_preview, name='404_preview'),
    path('api/cases/', cases_api, name='cases_api'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

# для медиа при DEBUG=True
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
