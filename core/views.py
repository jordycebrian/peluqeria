from django.shortcuts import render


# Create your views here.
def HomePageView(request):
    return render(request,"home.html")

def SobreNosotrosView(request):
    return render(request, "sobre_nosotros.html")

def CortesView(request):
    return render(request, "cortes.html")

