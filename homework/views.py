from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

def login(request):
    res = 0
    if request.method == 'POST':
        res=4
        name = request.POST.get('username')
        pw = request.POST.get('password')
        iden=request.POST.get('identity')
        if iden=='student':
            if student.objects.filter(username=str(name)):
                if student.objects.get(username=name).password == pw:
                    request.session['user'] = student.objects.get(username=name).id
                    return HttpResponseRedirect('account')
                else:
                    res=2
            else:
                res=1

        elif iden=='teacher':
            if teacher.objects.filter(username=name):
                if teacher.objects.get(username=name).password == pw:
                    request.session['user'] = teacher.objects.get(username=name).id
                    return HttpResponseRedirect('account')
                else:
                    res=2
            else:
                res=1
        return render(request, 'login.html', context={"res": res,
                                                      "name":name,
                                                      "pw":pw,
                                                      "iden":iden})
    else:
        return render(request, 'login.html', context={"res": res})


def account(request):
    return render(request, 'account-student.html')
