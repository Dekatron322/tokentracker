from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

import requests

from django.utils import timezone
import datetime



def AllStakeView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "stake/all_stakes.html", context)


def MyStakesView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "stake/my_stakes.html", context)

def DepositView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "stake/deposit.html", context)

def StakeView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "stake/stake.html", context)

def DashboardView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "stake/dashboard.html", context)

