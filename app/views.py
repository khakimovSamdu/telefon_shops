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
    return JsonResponse({"smartphones":ruyxat})

def get_brends(request: HttpRequest):
    data = Smartphone.objects.all()
    ls = ['Apple', 'Huawei', 'Oppo', 'Redmi', 'Nokia', 'Vivo', 'Samsung']
    ruyxat = []
    for item in data:
        brend = item.to_dict()
        if brend['company'] in ls and brend['company'] not in ruyxat:
            ruyxat.append(brend['company'])
    return JsonResponse(data=ruyxat, safe=False)

def brend_item_delete(request: HttpRequest, id: int):
    try:
        data = Smartphone.objects.filter(id=id).delete()
        data = Smartphone.objects.all()
        ruyxat = []
        for item in data:
            ruyxat.append(item.to_dict())
        return JsonResponse({"data":ruyxat})
    except:
        return HttpResponse("Server error or id error")
    
def brend_item_update(request: HttpRequest, id: int):
        if request.method == "POST":
            data = request.body.decode('utf-8')
            data = json.loads(data)
            item = Smartphone.objects.filter(id=id) 
            item.update(
                name = data['name'],
                company = data['company'],
                color = data['color'],
                RAM = int(data['RAM']),
                memory = int(data['memory']),
                price = float(data['price']), 
                img_url = data['img_url'], 
            )
            obj = Smartphone.objects.get(id=id)
            return JsonResponse(obj.to_dict(), safe=False)
            # ruyxat = []
            # for item in obj:
            #     ruyxat.append(item.to_dict())
            # return JsonResponse({"smartphes":ruyxat}, safe=False)
        else :
            return JsonResponse({"statust":"error"})

def brend_all(request: HttpRequest, brend: str):
    data = Smartphone.objects.filter(name__contains=brend, company__contains=brend)
    ruyxat = []
    for item in data:
            ruyxat.append(item.to_dict())
    return JsonResponse(ruyxat, safe=False)

def get_smartphone_id(request: HttpRequest, id: int):
    data = Smartphone.objects.get(id=id)
    return JsonResponse(data.to_dict())

