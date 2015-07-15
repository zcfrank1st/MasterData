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
    pass
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
    values = {"name": result.table_name, "description": result.description}
    return render(request, 'detail.html', values)
