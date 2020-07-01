from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *


def login(request):
    res = 0
    if request.method == 'POST':
        res = 4
        name = request.POST.get('username')
        pw = request.POST.get('password')
        iden = request.POST.get('identity')
        if iden == 'student':
            if student.objects.filter(username=str(name)):
                if student.objects.get(username=name).password == pw:
                    request.session['user'] = student.objects.get(username=name).id
                    return HttpResponseRedirect('account-student')
                else:
                    res = 2
            else:
                res = 1

        elif iden == 'teacher':
            if teacher.objects.filter(username=name):
                if teacher.objects.get(username=name).password == pw:
                    request.session['user'] = teacher.objects.get(username=name).id
                    return HttpResponseRedirect('account-teacher')
                else:
                    res = 2
            else:
                res = 1
        return render(request, 'login.html', context={"res": res})
    else:
        return render(request, 'login.html', context={"res": res})


def accountStudent(request):
    if request.method == 'POST':
        if 'exit' in request.POST:
            return HttpResponseRedirect('')
    # -----------------------------------------------------------------------------
    # -----------------------------------------------------------------------------
    user = request.session.get('user')
    if user == None:
        return HttpResponseRedirect('')
    else:
        stu = student.objects.get(id=user)
        sch = school.objects.get(id=stu.school_id)
        sub = subject.objects.filter(student=user)
        hw = []
        for s in sub[1:]:
            hom = []
            assi = assigment.objects.filter(subject_id=s.id)
            for a in assi:
                hm = {
                    "assigment": a,
                    "homework": homework.objects.get(assigment_id=a.id, student_id=user),
                    "already": len(homework.objects.filter(assigment_id=a.id, whether_submit=1)),
                    "need": len(homework.objects.filter(assigment_id=a.id))
                }
                hom.append(hm)
            tch = teacher.objects.get(id=s.teacher_id)
            info = {
                "subject": s,
                "teacher": tch,
                "assigment": hom
            }
            hw.append(info)

        sub_0 = sub[0]
        tch_0 = teacher.objects.get(id=sub_0.teacher_id)
        assi_0 = assigment.objects.filter(subject_id=sub_0.id)
        hw_0 = []
        for a in assi_0:
            info = {
                "assigment": a,
                "homework": homework.objects.get(assigment_id=a.id, student_id=user),
                "already": len(homework.objects.filter(assigment_id=a.id, whether_submit=1)),
                "need": len(homework.objects.filter(assigment_id=a.id))
            }
            hw_0.append(info)
        content = {
            "student": stu,
            "school": sch,
            "subject_0": sub_0,
            "homework_0": hw_0,
            "teacher_0": tch_0,
            "info": hw,
        }

        return render(request, 'account-student.html', content)


def accountTeacher(request):
    # if request.method == 'POST':
    #     if 'exit' in request.POST:
    #         return HttpResponseRedirect('')
    #     elif 'add' in request.POST:
    #         sub_id = request.POST.get('add')
    #         request.session['subject'] = sub_id
    #         return HttpResponseRedirect('homework-new')
    #     elif 'check' in request.POST:
    #         assi_id = request.POST.get('check')
    #         request.session['assigment'] = assi_id
    #         return HttpResponseRedirect('homework-detail')
    #     elif 'del' in request.POST:
    #         assi_id = request.POST.get('del')
    #         assigment.objects.get(id=assi_id).delete()
    #         return HttpResponseRedirect('account-teacher')
    # # -----------------------------------------------------------------------------
    # # -----------------------------------------------------------------------------
    # user = request.session.get('user')
    # if user == None:
    #     return HttpResponseRedirect('')
    # else:
    #     tch = teacher.objects.get(id=user)
    #     sch = school.objects.get(id=tch.school_id)
    #     sub = subject.objects.filter(teacher=user)
    #     hw = []
    #     for s in sub[1:]:
    #         hom = []
    #         assi = assigment.objects.filter(subject_id=s.id)
    #         for a in assi:
    #             hm = {
    #                 "assigment": a,
    #                 "already": len(homework.objects.filter(assigment_id=a.id, whether_submit=1)),
    #                 "need": len(homework.objects.filter(assigment_id=a.id))
    #             }
    #             hom.append(hm)
    #         info = {
    #             "subject": s,
    #             "assigment": hom
    #         }
    #         hw.append(info)
    #     sub_0 = sub[0]
    #     assi_0 = assigment.objects.filter(subject_id=sub_0.id)
    #     hw_0 = []
    #     for a in assi_0:
    #         info = {
    #             "assigment": a,
    #             "already": len(homework.objects.filter(assigment_id=a.id, whether_submit=1)),
    #             "need": len(homework.objects.filter(assigment_id=a.id))
    #         }
    #         hw_0.append(info)
    #     content = {
    #         "teacher": tch,
    #         "school": sch,
    #         "subject_0": sub_0,
    #         "assigment_0": hw_0,
    #         "homework": hw,
    #     }
    # return render(request, 'account-teacher.html', content)
    return render(request, 'account-teacher.html')


def accountTest(request):
    return render(request, 'account-test.html')


def homeworkNew(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        stt = timezone.now().strftime("%Y-%m-%d")
        edt = request.POST.get('end_time')
        txt = request.POST.get('text')
        sub_id = request.session.get('subject')
        assi = assigment.objects.create(name=na, start_time=stt, end_time=edt, text=txt, subject_id=sub_id)
        assi.save()
        stu = student.objects.filter(subject__id=sub_id)
        for s in stu:
            hw = homework.objects.create(assigment_id=assi.id, student_id=s.id)
            hw.save()
        return HttpResponseRedirect('account-teacher')

    return render(request, 'homework-new.html')


def homeworkDetail(request):
    assi = request.session.get('assigment')
    if assi == None:
        return HttpResponseRedirect('')
    else:
        hom = homework.objects.filter(assigment_id=assi)
        hw = []
        for h in hom:
            if h.whether_submit:
                info = {
                    "homework": h,
                    "photo": photo.objects.filter(homework_id=h.id),
                    "student": student.objects.get(id=h.student_id)
                }
                hw.append(info)

        content = {
            "homework": hw,
        }
    return render(request, 'homework-detail.html', content)


def homeworkUpload(request):
    return render(request, 'send.html')