from django.contrib import admin
from django.urls import path
from cases.admin import admin_site  # твой кастомный админ
from cases.views import cases_view, page_404_preview  # <--- добавлено здесь
from cases.views import cases_api
from django.views.generic import TemplateView
# для медиа при DEBUG=True
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', cases_view, name='home'),
    path('cases/', cases_view, name='cases'),
    path('404-preview/', page_404_preview, name='404_preview'),
    path('api/cases/', cases_api, name='cases_api'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
   url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

if settings.DEBUG:
    # Раздаём статику и медиа в режиме разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
else:
    # Раздаём статику и медиа и при DEBUG=False (локальная разработка, без nginx)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'cases.views.custom_404'
