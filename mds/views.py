# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from models import ItemTable

# Create your views here.


def index(request):  # GET
    return render(request, 'index.html')


def change_table_description(request):  # POST
    if request.method == 'POST':
        req = json.loads(request.body)
        try:
            ItemTable.objects.filter(table_id=req['id']).update(description=req['description'])
        except :
            return HttpResponse(json.dumps({"info": "no"}))
        return HttpResponse(json.dumps({"info": "yes"}))
    else:
        return HttpResponse(json.dumps({"info": "no"}))


def change_table_column_description(request):  # POST
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


def get_column_number(request, id):  # GET
    result = ItemTable.objects.get(table_id=id)
    array = eval(result.column_description)
    return HttpResponse(json.dumps({"number": str(len(array))}))


def get_all_tables(request):  # GET
    alls = ItemTable.objects.all()
    results = []
    for obj in alls:
        ele = {"name": obj.table_name, "id": str(obj.table_id)}
        results.append(ele)
    return HttpResponse(json.dumps(results))


def get_peculiar_table_info(request, id):  # GET
    result = ItemTable.objects.get(table_id=id)
    values = {"name": result.table_name, "description": result.description, "create_table": result.create_table_info, "blood": result.blood_relation, "columns": eval(result.column_description)}
    return render(request, 'detail.html', values)


def set_meta_info(request):  # POST && API
    if request.method == 'POST':
        req = json.loads(request.body)
        try:
            instance = ItemTable(table_name=req['table_name'], table_type=req['table_type'], description=req['description'], create_table_info=req['create_table_info'], column_description=req['column_description'], blood_relation=req['blood_relation'])
            instance.save()
            return HttpResponse(json.dumps({'info': 'yes'}))
        except Exception, e:
            print e
            return HttpResponse(json.dumps({'info': 'no'}))
    else:
        return HttpResponse(json.dumps({'info': 'no'}))


def set_part_meta_info(request):  # POST && API
    # 更新数据格式json
    # {
    #       "table_name": "xxx",
    #       "blood_relation": "xxx"
    # }
    if request.method == 'POST':
        req = json.loads(request.body)
        try:
            ItemTable.objects.filter(table_name=req['table_name']).update(blood_relation=req['blood_relation'])
            return HttpResponse(json.dumps({'info': 'yes'}))
        except Exception, e:
            print e
            return HttpResponse(json.dumps({'info': 'no'}))
    else:
        return HttpResponse(json.dumps({'info': 'no'}))
