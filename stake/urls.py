from django.urls import path
from . import views

app_name = "stake"

urlpatterns = [
	path("all-stake/", views.AllStakeView, name="all_stake"),
	path("stake/", views.StakeView, name="stake"),
	path("my-stakes/", views.MyStakesView, name="my_stakes"),
	path("deposit/", views.DepositView, name="deposit"),
	path("dashboard/", views.DashboardView, name="dashboard"),

	#path("make-payment/<int:staking_id>/", views.MakePaymentView, name="make_payment"),
	#path("confirm-payment/<int:staking_id>/", views.ConfirmPaymentView, name="confirm_payment"),

	#path("request_payment/<int:staking_id>/", views.RequestPaymentView, name="request_payment"),

]