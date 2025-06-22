from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from .models import Case

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'tags')
    search_fields = ('title',)

for model in (Group, User):
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass

admin.site.site_header = "caramel"
admin.site.site_title = "caramel"
admin.site.index_title = "Добро пожаловать в админку"

class MyAdminSite(AdminSite):
    site_header = "Название твоего сайта"
    site_title = "Название твоего сайта"
    index_title = "Добро пожаловать в админку"

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        # Можно добавить свои урлы, если нужно
        return urls

    def each_context(self, request):
        context = super().each_context(request)
        # Подключаем кастомный CSS к админке
        if 'custom_admin_css' not in context:
            context['custom_admin_css'] = 'admin_css/custom_admin.css'
        return context

admin_site = MyAdminSite(name='myadmin')

# Регистрация моделей для нового админсайта (пример)
from .models import Case
admin_site.register(Case)