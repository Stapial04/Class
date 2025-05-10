from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from core.models import Doctor
def home(request):
    data = {
        'title': 'App Medica',
        'description': 'Gesion de citas medicas',
        'author': 'Daniel Vera',
        'year': 2025,
    }
    # doctores = Doctor.objects.all()
    # data["doctores"]=doctores
    #return HttpResponse("<h1>Hello,Mi primer pagina con django</h1>")
    #return JsonResponse(data)  
    return render(request, 'home.html', data)

def doctor_list(request):
    # doctors = Doctor.objects.all()
    # print("doctors: ",doctors)
    # print("doctores: ",doctors.values())
    # print("metodo: ",request.method)
    # print("valor de get: ",request.GET,request.GET.get('q'))
    # return JsonResponse(list(doctors.values()), safe=False)
    query= request.GET.get('q',None)
    print(query)
    if query: doctors = Doctor.objects.filter(name__icontains=query)
    else: doctors = Doctor.objects.all()
    context = {'doctors': doctors, 'title': 'Listado de doctores'} 
    return render(request, 'doctor/list.html', context)
    # pass
def doctor_create(request):
    pass
def doctor_update(request):
    pass
def doctor_delete(request):
    pass