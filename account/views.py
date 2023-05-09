from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from account.forms import LoginUserForm, NewUserForm, newPasswordChange
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib import messages
# Create your views here.

def user_login(request):
    # if request.user.is_authenticated:
    #     return redirect("index")
   
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                nextUrl = request.GET.get("next", None)
                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else:
                return render(request, 'account/login.html', {"form": form, "error": "username ya da paralo yanlış"})
        else:
            return render(request, 'account/login.html',{"form": form, "error": "username ya da paralo yanlış"})
    else:
        form = LoginUserForm()
        return render(request, 'account/login.html', {"form": form})


def user_register(request):
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(request, username=username , password=password) 
            login(request,user)
            return redirect ("index")
        else:
            return render(request,"account/register.html",{"form":form})

    else:
       form=NewUserForm()
       return render(request,"account/register.html",{"form":form})
  
def user_logout(request):
   logout(request)
   return redirect("index")
def change_password(request):
    if request.method == "POST":
        form = newPasswordChange(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user) # note the change here
            messages.success(request, 'Your password has been changed successfully!')
            return redirect("index")
    else:
        form = newPasswordChange(request.user)
    return render(request, "account/change-password.html", {"form": form})
