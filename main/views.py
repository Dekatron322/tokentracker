from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required




from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

#from .forms import UserForm

from datetime import datetime
from requests import Request, Session
import json
import time
from datetime import datetime, timedelta

#from bs4 import BeautifulSoup
#from selenium import webdriver


#croat
#croeth
#cronaswap
#cronodes
#cronofi-finance
#minotaur
#mad-meerkat-optimizer
#tectonic
#darkcrypto-share
#pendle
#darkness-share
#degen-protocol-token
#lazy-horse-race-club
#pegasusdao
#cro-predict
#single-finance
#cronos-stable-swap
#dna-dollar
#dexpad
#photonswap
#croissant-games
#croblanc
#loot-network
#croking
#cromoon

def NoneView(request):
	if request.method == "POST":
		pass

	else:

		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crypto-com-chain&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		cronos = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crypto-com-chain&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		mad = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mad-meerkat-etf&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		darkcrypto = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=darkcrypto&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		cronosphere = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cronosphere&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		mimas = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mimas&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		cougar_token = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cougar-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		crodex = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crodex&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		darkness = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=darkness-dollar&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		gaur = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=gaur-money&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		vvs = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=vvs-finance&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		mmfinance = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mmfinance&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		meerkat_shares = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=meerkat-shares&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		savanna = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=savanna&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		context = {"cronos":cronos, "data":data, "darkcrypto":darkcrypto, "mad":mad, "cronosphere":cronosphere, "mimas":mimas, "cougar_token":cougar_token, "crodex":crodex, "darkness":darkness, "gaur":gaur, "vvs":vvs, "meerkat_shares":meerkat_shares, "mmfinance":mmfinance, "savanna":savanna}
		return render(request, "main/none.html", context)

def GetUrlViaAddress(address):
		
	if address == "0xb8df27c687c6af9afe845a2afad2d01e199f4878":
		url = "mad"
	
	elif address == "0x83b2ac8642ae46fc2823bc959ffeb3c1742c48b5":
		url = "darkcrypto"

	elif address == "0xc9fde867a14376829ab759f4c4871f67e2d3e441":
		url = "cronosphere"

	elif address == "0x10c9284e6094b71d3ce4e38b8bffc668199da677":
		url = "mimas"

	elif address == "0x4e57e27e4166275eb7f4966b42a201d76e481b03":
		url = "cougar"

	elif address == "0xe243ccab9e66e6cf1215376980811ddf1eb7f689":
		url = "crodex"

	elif address == "0x6582c738660bf0701f05b04dce3c4e5fcfcda47a":
		url = "darkness"
	elif address == "0x046cb616d7a52173e4da9eff1bfd590550aa3228":
		url = "gaur"
	elif address == "0x2d03bece6747adc00e1a131bba1469c15fd11e03":
		url = "vvs"
	elif address == "0x97749c9b61f878a880dfe312d2594ae07aed7656":
		url = "mmfinance"
	elif address == "0xf8b9facb7b4410f5703eb29093302f2933d6e1aa":
		url = "meerkat"
	elif address == "0x654bac3ec77d6db497892478f854cf6e8245dca9":
		url = "savanna"

	elif address == "0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b":
		url = "cronos"
	
	else:
		url = "cronos"


	return url

def GetUrlViaName(name):

	if name == "Mad Meerkat ETF (METF)":
		url = "mad"
	
	elif name == "DarkCrypto (DARK)":
		url = "darkcrypto"
		
	elif name == "Cronosphere (SPHERE)":
	    url = "cronosphere"
		
	elif name == "Mimas (MIMAS)":
	    url = "mima"

	elif name == "Cougar Token (CGS)":
		url = "cougar"

	elif name == "Crodex (CRX)":
		url = "crodex"

	elif name == "Darkness Dollar (DUSD)":
		url = "darkness"

	elif name == "Gaur Money (GAUR)":
		url = "gaur"
	
	elif name == "VVS Finance (VVS)":
		url = "vvs"
	elif name == "MMFinance (MMF)":
		url = "mmfinance"
		
	elif name == "Meerkat Shares (MSHARE)":
		url = "meerkat"

	elif name == "Savanna (SVN)":
		url = "savanna"

	elif name == "Cronos (CRO)":
		url = "cronos"
		
	else:
		url = "cronos"

	return url

def IndexView(request):
	if request.method == "POST":
		address_db = [
		"0xb8df27c687c6af9afe845a2afad2d01e199f4878", "0x83b2ac8642ae46fc2823bc959ffeb3c1742c48b5", 
		"0xc9fde867a14376829ab759f4c4871f67e2d3e441", "0x654bac3ec77d6db497892478f854cf6e8245dca9",
		"0x10c9284e6094b71d3ce4e38b8bffc668199da677", "0x4e57e27e4166275eb7f4966b42a201d76e481b03",
		"0xe243ccab9e66e6cf1215376980811ddf1eb7f689", "0x6582c738660bf0701f05b04dce3c4e5fcfcda47a",
		"0x046cb616d7a52173e4da9eff1bfd590550aa3228", "0x2d03bece6747adc00e1a131bba1469c15fd11e03",
		"0x97749c9b61f878a880dfe312d2594ae07aed7656", "0xf8b9facb7b4410f5703eb29093302f2933d6e1aa",
		"0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b"
		]

		name_db = ["Mad Meerkat ETF (METF)", "DarkCrypto (DARK)", "Mimas (MIMAS)", "Cougar Token (CGS)", "Crodex (CRX)",
		"Darkness Dollar (DUSD)", "Gaur Money (GAUR)", "VVS Finance (VVS)", "MMFinance (MMF)", "MMFinance (MMF)", "Meerkat Shares (MSHARE)", "Savanna (SVN)","Cronos (CRO)",]

		status = False
		result = None
		url = "none"

		query = request.POST.get("query")

		if query[0]+query[1] == "0x":
			for item in address_db:
				if query == item:
					result = item
					url = GetUrlViaAddress(result)


		for item in name_db:
			if query == item or query in item:
				result = item

				url = GetUrlViaName(result)


		return HttpResponseRedirect(reverse("main:%s" % (url)))
		


	else:
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		cronos = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crypto-com-chain&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		mad = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mad-meerkat-etf&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		darkcrypto = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=darkcrypto&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		cronosphere = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cronosphere&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		mimas = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mimas&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		cougar_token = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cougar-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		crodex = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crodex&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		darkness = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=darkness-dollar&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		gaur = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=gaur-money&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		vvs = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=vvs-finance&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		mmfinance = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mmfinance&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		meerkat_shares = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=meerkat-shares&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		savanna = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=savanna&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		context = {"cronos":cronos, "data":data, "darkcrypto":darkcrypto, "mad":mad, "cronosphere":cronosphere, "mimas":mimas, "cougar_token":cougar_token, "crodex":crodex, "darkness":darkness, "gaur":gaur, "vvs":vvs, "meerkat_shares":meerkat_shares, "mmfinance":mmfinance, "savanna":savanna}
		return render(request, "main/index.html", context )

def SavannaView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=savanna&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=savanna&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["savanna"]["usd"])
        market_cap = int(response["savanna"]["usd_market_cap"])
        hr_vol = str(response["savanna"]["usd_24h_vol"])
        hr_chg = str(response["savanna"]["usd_24h_change"])
        last_updated = str(response["savanna"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/savanna.html", context)

def MeerkatView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=meerkat-shares&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=meerkat-shares&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["meerkat-shares"]["usd"])
        market_cap = int(response["meerkat-shares"]["usd_market_cap"])
        hr_vol = str(response["meerkat-shares"]["usd_24h_vol"])
        hr_chg = str(response["meerkat-shares"]["usd_24h_change"])
        last_updated = str(response["meerkat-shares"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/meerkat.html", context)

def MmfinanceView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=mmfinance&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mmfinance&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["mmfinance"]["usd"])
        market_cap = int(response["mmfinance"]["usd_market_cap"])
        hr_vol = str(response["mmfinance"]["usd_24h_vol"])
        hr_chg = str(response["mmfinance"]["usd_24h_change"])
        last_updated = str(response["mmfinance"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/mmfinance.html", context)

def GaurView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=gaur-money&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=gaur-money&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["gaur-money"]["usd"])
        market_cap = int(response["gaur-money"]["usd_market_cap"])
        hr_vol = str(response["gaur-money"]["usd_24h_vol"])
        hr_chg = str(response["gaur-money"]["usd_24h_change"])
        last_updated = str(response["gaur-money"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/gaur.html", context)

def DarknessView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=darkness-dollar&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=darkness-dollar&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["darkness-dollar"]["usd"])
        market_cap = int(response["darkness-dollar"]["usd_market_cap"])
        hr_vol = str(response["darkness-dollar"]["usd_24h_vol"])
        hr_chg = str(response["darkness-dollar"]["usd_24h_change"])
        last_updated = str(response["darkness-dollar"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/darkness.html", context)

def CrodexView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=crodex&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crodex&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["crodex"]["usd"])
        market_cap = int(response["crodex"]["usd_market_cap"])
        hr_vol = str(response["crodex"]["usd_24h_vol"])
        hr_chg = str(response["crodex"]["usd_24h_change"])
        last_updated = str(response["crodex"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/crodex.html", context)

def CougarView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cougar-token&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cougar-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["cougar-token"]["usd"])
        market_cap = int(response["cougar-token"]["usd_market_cap"])
        hr_vol = str(response["cougar-token"]["usd_24h_vol"])
        hr_chg = str(response["cougar-token"]["usd_24h_change"])
        last_updated = str(response["cougar-token"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/cougar.html", context)

def MimasView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=mimas&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mimas&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["mimas"]["usd"])
        market_cap = int(response["mimas"]["usd_market_cap"])
        hr_vol = str(response["mimas"]["usd_24h_vol"])
        hr_chg = str(response["mimas"]["usd_24h_change"])
        last_updated = str(response["mimas"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/mimas.html", context)

def CronosphereView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cronosphere&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cronosphere&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["cronosphere"]["usd"])
        market_cap = int(response["cronosphere"]["usd_market_cap"])
        hr_vol = str(response["cronosphere"]["usd_24h_vol"])
        hr_chg = str(response["cronosphere"]["usd_24h_change"])
        last_updated = str(response["cronosphere"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/cronosphere.html", context)

def DarkcryptoView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=darkcrypto&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=darkcrypto&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["darkcrypto"]["usd"])
        market_cap = int(response["darkcrypto"]["usd_market_cap"])
        hr_vol = str(response["darkcrypto"]["usd_24h_vol"])
        hr_chg = str(response["darkcrypto"]["usd_24h_change"])
        last_updated = str(response["darkcrypto"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/darkcrypto.html", context)


def CronosView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=crypto-com-chain&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=crypto-com-chain&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["crypto-com-chain"]["usd"])
        market_cap = int(response["crypto-com-chain"]["usd_market_cap"])
        hr_vol = str(response["crypto-com-chain"]["usd_24h_vol"])
        hr_chg = str(response["crypto-com-chain"]["usd_24h_change"])
        last_updated = str(response["crypto-com-chain"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/cronos.html", context)


def MadView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=mad-meerkat-etf&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mad-meerkat-etf&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["mad-meerkat-etf"]["usd"])
        market_cap = int(response["mad-meerkat-etf"]["usd_market_cap"])
        hr_vol = str(response["mad-meerkat-etf"]["usd_24h_vol"])
        hr_chg = str(response["mad-meerkat-etf"]["usd_24h_change"])
        last_updated = str(response["mad-meerkat-etf"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/mad.html", context)

def VvsView(request):
    if request.method == "POST":
        pass
    else:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=vvs-finance&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
        data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=vvs-finance&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
        price = str(response["vvs-finance"]["usd"])
        market_cap = int(response["vvs-finance"]["usd_market_cap"])
        hr_vol = str(response["vvs-finance"]["usd_24h_vol"])
        hr_chg = str(response["vvs-finance"]["usd_24h_change"])
        last_updated = str(response["vvs-finance"]["last_updated_at"])
        context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated,}
        return render(request, "main/vvf.html", context)


def BannerView(request):
	form = BannerForm(request.POST, request.FILES)
	context = {'form': form}
	if request.method == "POST":
		if form.is_valid():
			title = form.cleaned_data.get('title')
			text = form.cleaned_data.get('text')
			link = form.cleaned_data.get('link')
			company_name = form.cleaned_data.get('company_name')
			image = request.FILES['image']
			interest = form.cleaned_data.get('interest')
			budget = form.cleaned_data.get('budget')
			proof_of_payment = form.cleaned_data.get('proof_of_payment')
			about_project = form.cleaned_data.get('about_project')

			try:
				form = Banner()
				form.title = title
				form.text  = text 
				form.link = link
				form.company_name = company_name
				form.image = image
				form.interest = interest
				form.budget = budget
				form.proof_of_payment = proof_of_payment
				form.about_project = about_project
				form.save()
				messages.success(request, "Submitted Successfully")
				return render(request, "main/index.html", context)
			except Exception as e:
				messages.error(request, 'Could Not Add ' + str(e))

		else:
			messages.error(request, 'Fill Form Properly ')
	return render(request, "main/banner.html", context )


def unvetted(request):
	form = UnvettedForm(request.POST, request.FILES)
	context = {'form': form}
	if request.method == 'POST':
		if form.is_valid():
			token_address = form.cleaned_data.get('token_address')
			telegram_url = form.cleaned_data.get('telegram_url')
			#proof_of_payment = form.cleaned_data.get("proof_of_payment")
			image = request.FILES['image']

			try:
				form = Unvetted()
				form.token_address = token_address
				form.telegram_url = telegram_url
				#proof_of_payment = proof_of_payment
				form.image = image
				form.save()
				messages.success(request, "Submitted Successfully")
				return render(request, "main/index.html", context)

			except Exception as e:
				messages.error(request, 'Could Not Add ' + str(e))

		else:
			messages.error(request, 'Fill Form Properly ')

	return render(request, "main/token.html", context)
