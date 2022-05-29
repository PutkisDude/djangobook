from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		print(request)
		if form.is_valid():
			user = form.save()
			login(request, user)
			print(form, request,user)
			return redirect("book_collection")
		else:
			return render (request=request, template_name="register/register.html", context={"form":form})

	else:
		form = RegisterForm()
		return render (request=request, template_name="register/register.html", context={"form":form})
