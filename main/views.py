from django.shortcuts import render, redirect
from .models import Goals, CompletedGoals, CanseledGoals
from .forms import GoalsForm, CreateUserForm, LoginForm
from django.views.generic import UpdateView, DeleteView, CreateView
from datetime import date
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    ip = ''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    err1, err2 = '', ''
    if request.method == 'POST':
        if 'goal' in request.POST:
            form = Goals(
                goal = request.POST.get('goal'),
                dateend = request.POST.get('dateend') if request.POST.get('dateend')!='' else date.today(),
                username = request.user
            )
            # if form.is_valid():
            form.save()
            return redirect('home')
        if 'logusername' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username = cd['logusername'], password = cd['logpassword'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('home')
                    else:
                        disable = 'disable accaunt'
        # if 'username' in request.POST:
        #     regform = CreateUserForm(request.POST)
        #     if regform.is_valid():
        #         regform.save()
        #         return redirect('home')
        #     else:
        #         err1 = regform.errors.get('username') if regform.errors.get('username') else ''
        #         err2 = regform.errors.get('password2') if regform.errors.get('password2') else ''
        else:
            g = Goals.objects.get(id=request.POST['id'])
            g.delete()
            com = CompletedGoals(
                goal = g.goal,
                timespend = (date.today() - g.datestart).days,
                enddate = date.today(),
                user = request.user
                )
            com.save()
            return redirect('home')

    # goals = Goals.objects.all()
    goals = Goals.objects.filter(username=request.user)
    allpercents = []
    goalsandpercents = []

    # вычисление сколько процентов осталось до завершения цели в случае указания прошедшей даты цель будет считаться бесконечной
    for goal in goals:
        try:
            daysleft = goal.dateend - date.today()
            interval = goal.dateend - goal.datestart
            percent = 100 - (daysleft/interval) * 100
            if percent>=0:
                allpercents.append({'percent':int(percent), 'daysleft':daysleft.days})
            else:
                allpercents.append({'percent':200, 'daysleft':-1})
        except:
            allpercents.append({'percent':200, 'daysleft':-1})
         
    # запаковывание и распаковывание переменных в новый список для дальнейшей распаковки их на странице,
    # причина такого поступка в том что сама по себе распаковка сразу двух элементов через zip в jinja не работает
    for z,c in zip(goals, allpercents):
        goalsandpercents.append([z,c])

    goalsandpercents.reverse()
    create = CreateUserForm
    data = {
        'goals': goals,
        'completedgoals': CompletedGoals.objects.filter(user=request.user).order_by('-enddate'),
        'form': GoalsForm,
        'allpercents': allpercents,
        'goalsandpercents': goalsandpercents,
        'create': create,
        'err1': err1,
        'err2': err2,
        'log': LoginForm,
        'user': request.user,
        'ip': ip
    }

    return render(request, 'main/home.html', data)


class Update(UpdateView):
    model = Goals
    form_class = GoalsForm

class Delete(DeleteView):
    model =  Goals
    success_url = '/'

class DeleteCom(DeleteView):
    model = CompletedGoals
    success_url = '/'



def reg(request):
    regform = CreateUserForm(request.GET)
    if regform.is_valid():
        regform.save()
    data = {'reg': regform.errors}
    return JsonResponse(data)

@login_required
def userlogout(request):
    logout(request)
    return redirect('home')

def validate(request):
    username = request.GET.get('username', None)
    data = {'is_taken': User.objects.filter(username__iexact=username).exists()}
    return JsonResponse(data)
