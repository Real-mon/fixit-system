
LOGOUT IN TECHNICIAN (WAITING FOR LOGIN PAGE AND DASHBOARD PAGE, THE FUNCTION IS WORKING with temporary LOGOUT BUTTON)
-logout.html(templates/accounts)
-logout.css(static/accounts)
-logout.js(static/accounts)

when clicked it will appear a box "are you sure you want to logout"
with buttons yes and no
once clicked yes it will redirect to log in else it will stay on the current page

PASSWORD RESET (BACKEND, WAITING FOR THE DB OF THE ACCOUNT SO THAT IT WILL BE UPDATED)
DONE Password Reset Front End (password_rest.html)
⦁	Password Reset Backend maybe finding the email in the DB then verify then the user can change the password, the password in the DB will be updated.



BACKEND OF LOGIN IN TECHNICIAN (ALREADY HAVE CODE WAITING FOR THE LOG IN PAGE AND DASHBOARD TO REDIRECT)

!!!ADD THIS TO THE VIEWS.PY FOR BACKEND OF LOGIN IN TECHNICIAN!!!

----------------------------------------------------------------------------------------
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Technician login handler
def technician_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")  # must match your frontend input names
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and getattr(user, "is_technician", False):
            login(request, user)  # logs the technician in
            return redirect("technician_dashboard")  # protected page
        else:
            messages.error(request, "Invalid credentials or not a technician")
            return redirect("technician_login")  # redirect back to frontend login page

    # Optional: redirect GET requests to login page
    return redirect("technician_login")


# Technician dashboard (protected)
@login_required
def technician_dashboard(request):
    if not getattr(request.user, "is_technician", False):
        return redirect("technician_login")
    return redirect("technician_dashboard_frontend_url")  # replace with the frontend page URL


# Technician logout
@login_required
def technician_logout(request):
    logout(request)
    return redirect("technician_login")
----------------------------------------------------------------------------------------
!!!ADD THIS IN THE URLS.PY !!!
from django.urls import path
from . import views

urlpatterns = [
    path('technician/login/', views.technician_login_view, name='technician_login'),
    path('technician/dashboard/', views.technician_dashboard, name='technician_dashboard'),
    path('technician/logout/', views.technician_logout, name='technician_logout'),
]
----------------------------------------------------------------------------------------