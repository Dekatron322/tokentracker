from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),

	path("banner/", views.BannerView, name="banner"),

	path("unvetted/", views.unvetted, name="unvetted"),
	#path('verify/banner/<int:pk>/', views.VerifyBannerView, name="verify_banner"),
	#path('verify/vetted/<int:pk>/', views.VerifyVettedView, name="verify_vetted"),

	#path("signup/", views.signup, name='signup'),
    #path("signin/", views.signin, name='signin'),
	#path('all-banner/', views.AllBannerView, name="all_banner"),

	#path('all-vetted/', views.AllVettedView, name="all_vetted"),


	#coin urls 
	#path("api/get-iotex-chart/", views.GetIotexJson, name="get_iotex_json"),
	path("cronos/", views.CronosView, name="cronos"),
	path("mad/", views.MadView, name="mad"),
	path("vvs/", views.VvsView, name="vvs"),
	path("darkcrypto/", views.DarkcryptoView, name="darkcrypto"),
	path("cronosphere/", views.CronosphereView, name="cronosphere"),
	path("mimas/", views.MimasView, name="mimas"),
	path("cougar/", views.CougarView, name="cougar"),
	path("crodex/", views.CrodexView, name="crodex"),
	path("darkness/", views.DarknessView, name="darkness"),
	path("mmfinance/", views.MmfinanceView, name="mmfinance"),
	path("gaur/", views.GaurView, name="gaur"),
	path("meerkat/", views.MeerkatView, name="meerkat"),
	path("savanna/", views.SavannaView, name="savanna"),
	path("sorry-no-result-found/", views.NoneView, name="none"),
	#mmfinance
	#savanna

]