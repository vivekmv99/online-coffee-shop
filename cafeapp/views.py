# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from cafeapp.models import *
from cafeapp.forms import *

def hello(request):
    return render(request, "index.html", {})
def hello1(request):
    return render(request, "log.html", {})
def hello2(request):
    return render(request, "userhome.html", {})


def hello4(request,proid):
    r=''
    if request.session.has_key('username'):
            b = request.session['username']
    e = items.objects.all()

    for i in e:
        if i.id == int(proid):
            proid = i.id
            name = i.item_name
            price = i.item_price

    if request.method == "POST":
        ordi = order1(request.POST)
        if ordi.is_valid():
            it_quantity = ordi.cleaned_data['it_quantity']
            totprice = it_quantity * price
            a = order(usname = b,it_name = name ,it_price = price,it_quantity =it_quantity,it_totl = totprice )
            a.save()
            return render(request,'buy.html',{'username': b,'id': proid,'itemname':name,'itemprice':price,'quantity':it_quantity,'total':totprice})
    # return render(request, "buy.html", {'username': b,'id': proid,'itemname':name})
    # d = order.objects.all()
    # return HttpResponse(totprice)







def hello3(request,id):
    d = items.objects.all()
    for i in d:
        if i.id == int(id):
            id = i.id
            pic = i.path
            name = i.item_name
            price = i.item_price
            disc = i.item_dis
            if request.session.has_key('username'):
                n = request.session['username']


    return render(request, "order.html", {'id':id,'itemname':name,'itemprice':price ,'pic':pic,'discrip':disc,'username': n})
    # return HttpResponse(pic)
def reg(request):
    username="error"
    if request.method == "POST":
        username="enterd"
        regi = register1(request.POST)
        if regi.is_valid():

            firstname= regi.cleaned_data['firstname']
            lastname= regi.cleaned_data['lastname']
            username = regi.cleaned_data['username']
            password = regi.cleaned_data['password']
            phone = regi.cleaned_data['phone']
            email = regi.cleaned_data['email']
            address = regi.cleaned_data['address']
            a =register(firstname=firstname,lastname=lastname,username=username,address=address,password=password,email=email,phone=phone)
            a.save()
            return render(request,'log.html',{})
    else:
        return HttpResponse(username)

    return HttpResponse(username)
def show(request):
    x = register.objects.all()
    s = ''
    for i in x:
        s += i.username + '<br>'

    return HttpResponse(s)
def log(request):
    username = "not logged in"
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = login(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            password = MyLoginForm.cleaned_data['password']
            c = register.objects.all()
            for i in c:
                if i.username==username and i.password==password:
                    request.session['username'] = i.username
                    a = items.objects.all()
                    return render(request,'userhome.html',{'products': a,'username': username})

            else:
                return HttpResponse("not")
    else:
         MyLoginForm = login()
    return render(request, 'log.html', {"username": username})




