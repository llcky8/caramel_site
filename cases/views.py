from django.shortcuts import render
from django.http import JsonResponse
from .models import Case
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User

def cases_view(request):
    cases = Case.objects.all()
    return render(request, 'cases/index.html', {'cases': cases})

def page_404_preview(request):
    return render(request, 'cases/404.html')

def cases_api(request):
    cases = Case.objects.all()
    data = {
        "cases": [
            {
                "title": c.title,
                "description": c.description,
                "tags": c.tags,
                "image_url": c.image.url if c.image else "",
            } for c in cases
        ]
    }
    return JsonResponse(data)

def delete_user(request, user_id):
    if request.user.is_staff:  # Проверка прав администратора
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return redirect('admin_panel')
    else:
        return redirect('login')
