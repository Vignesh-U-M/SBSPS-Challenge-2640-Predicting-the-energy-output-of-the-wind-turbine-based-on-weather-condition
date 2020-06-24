from django.shortcuts import render
from django.contrib.auth.models import auth, User
import folium
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
    map = folium.Map(location=[lat,lon], zoom_start=6,tiles="Stamen Terrain")
    fg = folium.FeatureGroup(name="test")
    fg.add_child(folium.Marker(location=[lat, lon], popup="Location Name", icon=folium.Icon(color='green')))
    map.add_child(fg)
    map.save("Templates/map.html")
    return render(request, "user_home.html", {"username": username})
