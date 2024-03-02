from django.shortcuts import render
from .models import Smartphone
import json
from django.http import HttpRequest, HttpResponse, JsonResponse
# Create your views here.


def get_add(request: HttpRequest):
    if request.method=='POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)
        ram = ''
        rom = ''
        for i in data['RAM']:
            if i.isdigit():
                ram += i
            else:
                break
        for i in data['memory']:
            if i.isdigit() or i=="+":
                rom += i
            else:
                break
        rom = eval(rom)
        create = Smartphone.objects.create(
            name = data['name'],
            company = data['company'],
            color = data['color'],
            RAM = int(ram),
            memory = int(rom),
            price = data['price'], 
            img_url = data['img_url'], 
        )
        return JsonResponse({"statust":"OK"})
    else:
        return JsonResponse({"Method":"Error"})

def get_all(request: HttpRequest):
    data = Smartphone.objects.all()
    ruyxat = []
    for item in data:
        ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_brends(request: HttpRequest):
    data = Smartphone.objects.all()
    ruyxat = []
    for item in data:
        brend = item.to_dict()
        if brend['company'] not in ruyxat and brend['company']!="Xiaomi" and brend['company']!="Mi":
            ruyxat.append(brend['company'])
    return JsonResponse({"Smarphones": ruyxat}, safe=False)

def brend_item_delete(request: HttpRequest, id: int, brend: str):
    try:
        data = Smartphone.objects.filter(id=id).delete()
        data = Smartphone.objects.filter(name__contains=brend)
        ruyxat = []
        for item in data:
            ruyxat.append(item.to_dict())
        return JsonResponse(ruyxat, safe=False)
    except:
        return HttpResponse("Server error or id error")
    
def brend_item_update(request: HttpRequest, id: int, brend: str):
    try:
        item = Smartphone.objects.filter(id=id) 
        item.update(
            name = "Infinix Hot 11 Play"
        )
        data = Smartphone.objects.filter(name__contains=brend, company__contains=brend)
        ruyxat = []
        for item in data:
            ruyxat.append(item.to_dict())
        return JsonResponse(ruyxat, safe=False)
    except:
        return HttpResponse("Server error or id error")

def brend_all(request: HttpRequest, brend: str):
    data = Smartphone.objects.filter(name__contains=brend, company__contains=brend)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

