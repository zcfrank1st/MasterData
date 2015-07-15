# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from models import ItemTable

# Create your views here.
# index 页面
def index(request):
    return render(request, 'index.html')

# restful 方法
# POST
def change_table_description(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        try:
            ItemTable.objects.filter(table_id=req['id']).update(description=req['description'])
        except :
            return HttpResponse(json.dumps({"info": "no"}))
        return HttpResponse(json.dumps({"info": "yes"}))
    else:
        return HttpResponse(json.dumps({"info": "no"}))


# POST
def change_table_column_description(request):
    pass


# GET
def get_all_tables(request):
    alls = ItemTable.objects.all()
    results = []
    for obj in alls:
        ele = {"name": obj.table_name, "id": str(obj.table_id)}
        results.append(ele)
    return HttpResponse(json.dumps(results))

# GET
def get_peculiar_table_info(request, id):
    result = ItemTable.objects.get(table_id=id)
    values = {"name": result.table_name, "description": result.description, "create_table": result.create_table_info, "blood": result.blood_relation}
    return render(request, 'detail.html', values)
