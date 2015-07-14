# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# index 页面
def index(request):
    return render(request, 'index.html')

# restful 方法
# POST
def change_table_description(request):
    return HttpResponse("hahahah")
# POST
def change_table_column_description(request):
    pass
# GET
def get_all_tables(request):
    pass

# GET
def get_peculiar_table_info(request):
    pass