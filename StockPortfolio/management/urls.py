from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('portfolios', views.portfolios, name='portfolios'),
    path('find', views.find, name='find'),
    path('calculator', views.calculator, name='calculator'),    #
    path('portfolios', views.PortfolioList.as_view(), name='portfolios_list'),
    path('portfolio/create', views.PortfolioCreate.as_view(success_url=('portfolios')), name='portfolio_create'),
    path('watch/<int:pk>/', views.watch, name='watch'),
    path('buy', views.buy, name='watch'),
    path('investmentdetail/<int:num>/', views.investmentdetail, name='investmentdetail'),
]
