# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


# --- Password reset views ---
def password_reset_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # Later, you will implement sending reset link here
        messages.success(request, f"If {email} is registered, a reset link has been sent.")
        return redirect('password_reset')  # reload same page with success message

    return render(request, "accounts/password_reset.html")


def set_new_password_view(request):
    return render(request, 'accounts/set_new_password.html')


def confirmation_view(request):
    return render(request, 'accounts/confirmation.html')


# --- Logout views ---

# This one just shows your logout page template
def logout(request):
    return render(request, 'accounts/logout.html')


# This one actually logs out the user and redirects to login
def logout_user(request):
    auth_logout(request)  # clears the session
    return redirect('password_reset')  # make sure you have a URL named 'login' TO BE CHANGED WHEN LOG IN IS DONE


# --- Dashboard view ---
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
