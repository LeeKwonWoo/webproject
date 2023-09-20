from django.shortcuts import render
from django.http import HttpResponse
from polls.models import User
# from .forms import LoginForm
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate


from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def login(request):
    # if request.method == "POST":
    #     form = LoginForm(request.POST)
    id = request.POST['id']
    pw = request.POST['password']
    #     user = authenticate(user_id = id, user_pw = pw)
    #     return HttpResponse("성공")
    
    # all()은 쿼리에 맞는 객체 하나
    # filter()는 조건에 맞는 쿼리셋(객체 여러개 반환)
    user_id = User.objects.filter(user_id=id).get().user_id
    user_pw = User.objects.filter(user_id=id).get().user_pw
    
    if id == user_id and pw == user_pw:
        return HttpResponse("%s, Success Login!" % id)
    elif id == user_id and pw != user_pw:
        return HttpResponse("Failed password!")
    elif id != user_id:
        return HttpResponse("Failed Id or password!")
    return HttpResponse("Failed Login!")
