from django.http import JsonResponse
from firstApp.models import Employee


# Create your views here.
def employee_view(request):
    emp = {
        'id': 12,
        'name': 'Bakary',
        'sal': 10000
    }
    data = Employee.objects.all()
    response = {'employees': list(data.values('name', 'sal'))}
    return JsonResponse(response)
