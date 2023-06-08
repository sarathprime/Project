import gettext
import test.seq_tests

from .models import *
from django.shortcuts import render,redirect
from user.models import *
from cipher.models import *
from django.core.mail import send_mail
from process.models import *
from domain.models import *
from .models import *

from django.contrib import messages


# Create your views here.
def a_index(request):
    return render(request, 'admin/admin_index.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == "admin@gmail.com" and password == "admin":
            request.session['admin'] = 'admin@gmail.com'
            messages.info(request, "LOGIN SUCCESSFULL")
            return redirect('/a_index/')
        elif username != "admin@gmail.com":
            messages.error(request, "Wrong Admin Email")
            return redirect('/admin_login/')
        elif password != "admin":
            messages.error(request, "Wrong Admin Password")
            return render(request, 'admin/admin_login.html')
    return render(request, 'admin/admin_login.html')


def view_domain(request):
    datas=domain_register.objects.all()
    return render(request, 'admin/view_domain.html',{'datas':datas})



def GENERATE_ID(request):
    datas = domain_register.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        id_donor = request.POST['id_donor']
        domain_id_generate(email=email, id_donor=id_donor).save()
        messages.info(request, "ACCESS ID STORED IN DATABASE ")
        return redirect('/GENERATE_ID/')
    return render(request, 'admin/D_id.html',{'datas':datas})





def domain_send_mail(request,id):
    datas=domain_id_generate.objects.get(id=id)
    t= datas.id_donor
    send_mail(
        'Subject here',
        f'CONGRATS FOLK!!! , You have been Approved for accessing our wallet, your wallet id  is {t}   ',
        'sarath@gmail.com',
        [datas.email],
        fail_silently=False,
    )
    messages.info(request, "ACCESS ID SUCCESSFULLY FORWARDED TO DOMAIN")

    # datas.save()
    return redirect('/a_index/')



def view_donor_generated_id(request):
    datas=domain_id_generate.objects.all()
    return render(request, 'admin/send_id_to_domain.html',{'datas':datas})



def view_donor_purpose(request):
    datas=domain_purpose_register.objects.filter(boo3=False)
    return render(request, 'admin/view_domain_purpose.html',{'datas':datas})


def create_virtual_box(request,id):
    datas = domain_purpose_register.objects.get(id=id)
    datas.boo3=True
    datas.save()
    print('hi')
    messages.info(request, "VIRTUAL BOX SUCCESSFULLY CREATED NOW USER CAN LOGIN!!")
    return redirect('/view_donor_purpose/')

def access_procee_team(request):
    datas=process_team_id.objects.all()
    return render(request, 'admin/vire_process_id.html',{'datas':datas})


def access_cipher_team(request):
    datas=cipher_team_id.objects.all()
    return render(request, 'admin/vire_cipher_id.html',{'datas':datas})

def access_domain_team(request):
    datas=domain_1_access.objects.all()
    return render(request, 'admin/view_domain_id.html',{'datas':datas})


def virtual_loading(request):
    return render(request, 'admin/virtual_loading.html')



def cipher_team_mail(request, id):
    datas = cipher_team_id.objects.get(id=id)
    # datas2 = client_purpose.objects.get(id=id)
    # y= datas2.yourname
    t = datas.email
    send_mail(
        'Subject here',
        f'welcome Technical team!!! , your team wallet id  is 3546  ',
        'sarath@gmail.com',
        [datas.email],
        fail_silently=False,

    )
    messages.info(request, "TECHNICAL TEAM ID SUCCESSFULLY FORWARD TO THEIR MAIL ID!")
    # datas.save()
    return redirect('/a_index/')



def domain_team_mail(request, id):
    datas = domain_1_access.objects.get(id=id)
    # datas2 = client_purpose.objects.get(id=id)
    # y= datas2.yourname
    t = datas.user_email
    send_mail(
        'Subject here',
        f'welcome Domain User!!! , your team wallet id  is 9723  ',
        'sarath@gmail.com',
        [datas.user_email],
        fail_silently=False,

    )
    messages.info(request, "ID SUCCESSFULLY FORWARDED DOMAIN")
    # datas.save()
    return redirect('/a_index/')



def process_team_mail(request, id):
    datas = process_team_id.objects.get(id=id)
    # datas2 = client_purpose.objects.get(id=id)
    # y= datas2.yourname
    t = datas.email
    send_mail(
        'Subject here',
        f'welcome Process team!!! , your team wallet id  is 1124   ',
        'sarath@gmail.com',
        [datas.email],
        fail_silently=False,

    )
    messages.info(request, "ACCESS ID SUCCESSFULLY FORWARDED TO PROCESS TEAM MAIL")
    # datas.save()
    return redirect('/a_index/')




def A_logout(request):
    if 'admin' in request.session:
        request.session.pop('admin',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'SESSION LOGOUT ALREADY')
        return redirect('/admin/')


def admin_payslip_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        access_id = request.POST['access_id']
        admin_payslip(email=email, access_id=access_id).save()
        messages.success(request, 'PAYSLIP PROVIDED TO DOMAIN')
    return render(request, 'admin/admin_payslip.html')




def tokens():
    class token():
        serializers = models.enums_all
        document= models.constraints_all
        def attribute(self):
            token=test.seq_tests.Sequence
            gettext.install(



            )
        authorazation = models.expressions

    return redirect










