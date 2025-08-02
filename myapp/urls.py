from django.urls import path
from . import views

urlpatterns = [
    path('', views.myview)
    ]
# Create your views here.
def myview(request):
    return render(request, "index.html")