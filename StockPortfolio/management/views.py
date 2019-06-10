from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404
import json
import datetime
from .alphaLogic import *
from management.models import *

class PortfolioList(ListView):
    model = Portfolio

class PortfolioView(DetailView):
    model = Portfolio

class PortfolioCreate(CreateView):
    model = Portfolio
    fields = ['name', 'user',]
    success_url = reverse_lazy('portfolios')

class PortfolioUpdate(UpdateView):
    model = Portfolio
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')

class PortfolioDelete(DeleteView):
    model = Portfolio
    success_url = reverse_lazy('book_list')

def index(request):
    allPortfolios = Portfolio.objects.all()
    context = {
        "webTitle" : " ",
        "allPortfolios" : allPortfolios,
    }
    return render(request,"management/index.html",context)

def portfolios(request):
    context = {
        "webTitle" : "My Portfolios all together",
    }
    return render(request,"management/portfolios.html",context)

def find(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        toFind = request.POST.get('toFind')
        #Business layer, call some function
        context = {
        "webTitle" : " ",
        "toFind" : JsonResponse(getInfo(toFind)),
        }
    return JsonResponse(getInfo(toFind))

def calculator(request):
    context = {
        "webTitle" : "Bond Princing Calculator",
    }
    return render(request,"management/calculator.html",context)

def buy(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        selectedPortfolio = request.POST.get('selectedPortfolio')
        quantityf = request.POST.get('quantity')
        pricef = request.POST.get('price')
        symbolf = request.POST.get('symbol')
        datef = request.POST.get('refreshed')
        portfoliObj = Portfolio.objects.get(pk=selectedPortfolio)
        #Create investment Object
        investmentObj = Investment(portfolio=portfoliObj,symbol=symbolf,quantity=quantityf,price=pricef)
        investmentObj.save()
        print(f'Investment: {investmentObj}')
        #Create transaction Object
        transactionObj = Transaction(investment=investmentObj,type=True,quantity=quantityf,TransactionPrice=pricef)
        transactionObj.save()
        print(f'transactionObj: {transactionObj}')

    redirectUrl = f'/management/watch/{selectedPortfolio}'
    return redirect(redirectUrl)


def watch(request, pk):
    try:
        currentPortfolio = Portfolio.objects.get(pk=pk)
        allInvest = Investment.objects.all().filter(portfolio=currentPortfolio.id)
    except Portfolio.DoesNotExist:
        raise Http404("Portfolio does not exist")

    context = {
        "portfolios": "portfolios",
        "controller" : "management",
        "currentPortfolio": currentPortfolio,
        "allInvest":allInvest,
        "webTitle" : " ",
    }
    return render(request, 'management/watchPortFolio.html', context)

def investmentdetail(request, num):
    try:
        allTransacions = Transaction.objects.all().filter(investment=num)
    except Transaction.DoesNotExist:
        raise Http404("Transaction does not exist")
    context = {
        "allTransacions":allTransacions,
        "webTitle" : " ",
    }
    return render(request, 'management/watchPortFolioDetail.html', context)
