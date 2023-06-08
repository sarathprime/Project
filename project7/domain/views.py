from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from user.models import *
from administarator.models import *
import random
import base64

def final_domain_index(request):
    return render(request, 'domian/domain_index.html')



def domian_login_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            emp = process_register.objects.get(email=email, password=password)
            request.session['domain'] = emp.email
            print('hi')
            messages.info(request, "SESSION LOGIN SUCCESSFULL")
            return redirect('/final_domain_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'domian/domian_login.html')


def domian_register_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        process_register(username=username, email=email, password=password, contact=contact, address=address
                      ).save()
        messages.info(request, "SUCCESSFULLY REGISTERED READY FOR LOGIN")
        return redirect('/domian_login_form/')
    return render(request, 'domian/domain_register.html')





def domain_logout(request):
    if 'domain' in request.session:
        request.session.pop('domain',None)
        messages.success(request,'SEESION LOGOUT SUCCESSFULLY')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin/')


def domain_payment(request):
    datas = admin_payslip.objects.all()
    return render(request, 'domian/payment.html', {'datas': datas})



def domain_access_1(request):
        if request.method == 'POST':
            user_email = request.POST['user_email']
            purpose = request.POST['purpose']
            domain_1_access(user_email=user_email, purpose=purpose).save()
            messages.info(request, "ACCESS REQUEST SUCCESSFULLY FORWARDED TO ADMIN!")
            return redirect('/domain_accept_1/')
        return render(request, 'domian/request1.html')



def domain_accept_1(request):
    if request.method == 'POST':
        accessid = request.POST['accessid']
        if int(accessid) == int(9723):
            messages.info(request, "WELCOME DOMAIN USER ")
            print('hi')
            return redirect('/view_user_details/')
        else:

            messages.error(request, "please enter correct wallet id ")
            print('no')
            return redirect('/domain_access_1/')
    return render(request, 'domian/request1.html')


def domain_access_2(request):
    if request.method == 'POST':
        accessid = request.POST['accessid']
        if int(accessid) == int(9723):
            messages.info(request, "WELCOME DOMAIN USER ")
            print('hi')
            return redirect('/view_file/')
        else:

            messages.error(request, "please enter correct wallet id ")
            print('no')
            return redirect('/domain_access_2/')
    return render(request, 'domian/request2.html')

def view_user_details(request):
    datas = user_credential_details.objects.all()
    return render(request, 'domian/view_user_credential.html', {'datas': datas})



def domain_id_encrytion_id(request):
    if request.method == 'POST':
        email = request.POST['email']
        cipher_team_id(email=email).save()
        messages.info(request,'ID REQUEST SUCCESSFULLY FORWARDED TO ENCRYPTION TEAM!')
        return redirect('/cipher_index/')
    return render(request, 'cipher/cipher_process_id.html')


def domain_request_id(request):
    if request.method == 'POST':
        user_email = request.POST['user_email']
        decryption_Requst(user_email=user_email).save()
        messages.info(request,'Successfully Sent ID Request')
        return redirect('/view_user_details/')
    return render(request, 'domian/domain_request_id.html')


def domain_decrypt_enter(request):
    if request.method == 'POST':
        accessid = request.POST['accessid']
        if int(accessid) == int(5421):

            messages.info(request, "YOU CAN DECRYPT NOW!! ")
            print('hi')
            return redirect('/final_decrypt/')
        else:

            messages.error(request, "please enter correct Access id ")
            print('no')
            return redirect('/domain_request_id/')
    return render(request, 'cipher/cipher_id_1.html')



def final_decrypt(request):
    datas = user_credential_details.objects.all()
    return render(request, 'domian/final_decrypt.html', {'datas': datas})


def dec11(request,id):
    get = user_credential_details.objects.get(id=id)

    r = get.id
    inputvar = []
    get.save()

    a = get.username
    b = get.email
    c = get.city
    d = get.state
    e = get.url
    f = get.country
    # print(a)
    # print(b)
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(f)
    print(f'input : {inputvar}')

    de = []
    # for i in inputvar:
    # decoded_value= base64.b64decode(inputvar[0].decode("ascii", "strict"))
    print(inputvar[0])
    k = inputvar[0].lstrip('b')
    a = inputvar[1].lstrip('b')
    t = inputvar[2].lstrip('b')
    n = inputvar[3].lstrip('b')
    sa = inputvar[4].lstrip('b')
    sn = inputvar[5].lstrip('b')

    m =[k,a,t,n,sa,sn]
    l =k
    print(l)
    for i in m:

        msg = base64.b64decode(i)
        print('hello',msg)
        decoded_value = msg.decode("ascii", "strict")
        print('hi',decoded_value)
        de.append(decoded_value)
        print(de)

    # print()

        # print('l',de)
    # print(decoded_value)
    # print(enc)
    a = de[0]
    b = de[1]
    c = de[2]
    d = de[3]
    e = de[4]
    f = de[5]
    st = user_credential_details.objects.filter(id=r).update(username=a, email=b, city=c, state=d,url=e,country=f)
    print(a, b, c, d, e ,f)
    messages.info(request, "DATA DECRYPTED SUCCESSFULLY YOU CAN VIEW NOW!!")
    return redirect('/final_decrypt/')


def final_final_decrypt(request):
    datas = user_credential_details.objects.all()
    return render(request, 'domian/final_final_Decrypt.html', {'datas': datas})


def view_file(request):
    datas = user_credential_details.objects.all()
    return render(request, 'domian/view_file.html', {'datas': datas})

def domain_request_id_2(request):
    if request.method == 'POST':
        user_email = request.POST['user_email']
        decryption_Requst_2(user_email=user_email).save()
        messages.info(request,'Successfully Sent ID Request')
        return redirect('/view_file/')
    return render(request, 'domian/domain_request_id_2.html')



def domain_file_enter(request):
    if request.method == 'POST':
        accessid = request.POST['accessid']
        if int(accessid) == int(1721):

            messages.info(request, "YOU CAN VIEW DATA!! ")
            print('hi')
            return redirect('/final_final_decrypt/')
        else:

            messages.error(request, "please enter correct wallet id ")
            print('no')
            return redirect('/view_file/')
    return render(request, 'domain/view_file.html')