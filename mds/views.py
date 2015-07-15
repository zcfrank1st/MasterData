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
    if request.method == 'POST':
        req = json.loads(request.body)
        new_column_description = []
        column_description = eval(ItemTable.objects.get(table_id=req['id']).column_description)
        column_info_array = req['column']

        for index,one_column_description in enumerate(column_description):
            one_column_description['info'] = column_info_array[index]
            new_column_description.append(one_column_description)
        try:
            ItemTable.objects.filter(table_id=req['id']).update(column_description=new_column_description)
        except :
            return HttpResponse(json.dumps({"info": "no"}))
        return HttpResponse(json.dumps({"info": "yes"}))
    else:
        return HttpResponse(json.dumps({"info": "no"}))
    pass

def get_column_number(request, id):
    result = ItemTable.objects.get(table_id=id)
    array = eval(result.column_description)
    return HttpResponse(json.dumps({"number": str(len(array))}))

# GET
def get_all_tables(request):
    alls = ItemTable.objects.all()
    results = []
    for obj in alls:
        ele = {"name": obj.table_name, "id": str(obj.table_id)}
        results.append(ele)
    return HttpResponse(json.dumps(results))

# GET  eval转换
def get_peculiar_table_info(request, id):
    result = ItemTable.objects.get(table_id=id)
    values = {"name": result.table_name, "description": result.description, "create_table": result.create_table_info, "blood": result.blood_relation, "columns": eval(result.column_description)}
    return render(request, 'detail.html', values)
