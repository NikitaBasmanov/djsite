from django.http import HttpResponse
from django.shortcuts import render

menu = [
    {'title': "Главня страница",'url_name':'home'},
    {'title': "О сайте",'url_name':'prosto'},
    {'title': "Добавить", 'url_name': 'addpage'},
    {'title': "Обратная связь", 'url_name': 'conact'},

]

def index(request):
    return render(request, 'profession/index.html', { 'menu' : menu, 'title':'Главная страница'})
def prosto(request):
    return render(request, 'profession/prosto.html', {'menu' : menu,'title':'О сайте'})
def addpage(request):
    return render(request, 'profession/addpage.html', {'menu' : menu,'title':'Добваить'})
def conact(request):
    return render(request, 'profession/conact.html', {'menu' : menu,'title':'Обратная связь'})
