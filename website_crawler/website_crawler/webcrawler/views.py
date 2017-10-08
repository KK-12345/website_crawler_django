from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenicated():
        return render()
    else:
        return render(request, 'cover.html')