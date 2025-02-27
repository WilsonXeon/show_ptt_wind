from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime

from .mysql_select_from_ptt import ptt_user_name
from .mysql_select_from_ptt import ptt_user_name_and_msg
from .mysql_select_from_ptt import ptt_msg_search

def user_name_page(request):

    if 'user_name' in request.GET and 'msg_like' not in request.GET :
        return render(request, 'user_name_page.html', {
        'msg_list': ptt_user_name(request.GET['user_name']),
        })
        
    elif 'user_name' in request.GET and 'msg_like' in request.GET and request.GET['msg_like'] == "":
        return render(request, 'user_name_page.html', {
        'msg_list': ptt_user_name(request.GET['user_name']),
        })
        
    elif 'user_name' in request.GET and 'msg_like' in request.GET :
        return render(request, 'user_name_page.html', {
        'msg_list': ptt_user_name_and_msg(request.GET['user_name'],request.GET['msg_like']),
        })
        
    else:
        return render(request, 'user_name_page.html')
    

def ptt_msg_search_engine_page(request):
    
    if 'msg_like' in request.GET :
        return render(request, 'msg_search_engine.html', {
        'msg_list': ptt_msg_search(request.GET['msg_like']),
        'msg_like' : request.GET['msg_like'],
        })
        
    else:
        return render(request, 'msg_search_engine.html')

from .mysql_select_from_ptt import count_keyword
from django.http import JsonResponse
def ptt_count_keyword_api(request) -> JsonResponse:
    c1 = 0
    start_date = "2019/10/1 00:00:00"
    end_date = "2019/11/1 00:00:00"
    msg_over_count = 1

    if 'msg_like' in request.GET and request.GET['msg_like'] !="":
        c1 = count_keyword(request.GET['msg_like'], start_date, end_date, msg_over_count)
        
    return JsonResponse({'count':c1})

from .mysql_select_from_ptt import count_eachUser_keyword
def count_eachUser_keyword_page(request):
    start_date = "2019/1/1 00:00:00"
    end_date = "2019/12/31 00:00:00"
    msg_over_count = 1

    if 'msg_like' in request.GET and request.GET['msg_like'] !="":
        user_and_count = count_eachUser_keyword(request.GET['msg_like'], start_date, end_date, msg_over_count)
        return render(request, 'msg_count.html', {
        'msg_list': user_and_count,
        'msg_like' : request.GET['msg_like'],
        })
    else:
        return render(request, 'msg_count.html')
    
