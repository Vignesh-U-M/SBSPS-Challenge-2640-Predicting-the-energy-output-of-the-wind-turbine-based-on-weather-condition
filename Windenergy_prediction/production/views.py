from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User
import folium
from .models import wind_details,location_details
from django.views.decorators.cache import cache_control
# Create your views here.
def main(request):
    username = User.objects.get(username=request.user.username)
    return render(request, "user_home.html", {"username": username})

def map(request):
    return render(request,"map.html")

def add_location_map(request):
    username = User.objects.get(username=request.user.username)
    lat = request.POST['lot']
    lon = request.POST['log']
    ld = location_details()
    ld.user_name = username
    ld.lattitude = lat
    ld.longtitude = lon
    ld.save()

    #map = folium.Map(location=[lat,lon], zoom_start=6,tiles="Stamen Terrain")
    map = folium.Map()
    fg = folium.FeatureGroup(name="test")
    fg.add_child(folium.Marker(location=[lat, lon], popup="Location Name", icon=folium.Icon(color='green')))
    map.add_child(fg)
    map.save("Templates/map.html")
    return render(request, "Wind farm Location.html", {"username": username})

def update_profile(request):
    un = User.objects.get(username=request.user.username)
    fn = request.POST['fname']
    ln = request.POST['lname']
    phone = request.POST['phone']
    pincode = request.POST['pincode']
    location = request.POST['location']
    orgname = request.POST['orgname']
    orgemail = request.POST['orgemail']
    country = request.POST['country']
    state = request.POST['state']
    no_of_wind = request.POST['no_of_wind']
    wd = wind_details()
    wd.username = un
    wd.first_name = fn
    wd.last_name = ln
    wd.phone = phone
    wd.pincode = pincode
    wd.location = location
    wd.orgname = orgname
    wd.orgemail = orgemail
    wd.country = country
    wd.state = state
    wd.no_of_wind = no_of_wind
    wd.save()
    return render(request, "My-home.html")

def comp_analysis(request):
    return render(request, "comparative analysis.html")

def windform_location(request):
    return render(request, "Wind farm Location.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


