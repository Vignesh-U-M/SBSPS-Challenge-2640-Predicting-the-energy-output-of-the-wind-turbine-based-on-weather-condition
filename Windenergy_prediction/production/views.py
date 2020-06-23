from django.shortcuts import render
from django.contrib.auth.models import auth, User
# Create your views here.
def main(request):
    username = User.objects.get(username=request.user.username)
    return render(request, "user_home.html", {"username": username})