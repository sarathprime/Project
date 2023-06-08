from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
from user.models import *
from domain.models import *
from django.core.mail import send_mail
import string,random,hmac
# from crypto.publickey import RSA
# from Crypto.Util.asn1 import rsa
import rsa

import random
import base64


# Create your views here.
def cipher_index(request):
    return render(request, 'cipher/cipher_index.html')


def cipher_register_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        cipher_register(username=username, email=email, password=password, contact=contact, address=address
                      ).save()
        messages.info(request, "SUCCESSFULLY REGISTERED READY FOR LOGIN!!")
        return redirect('/cipher_login/')
    return render(request, 'cipher/cipher_register.html')



def cipher_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            emp = cipher_register.objects.get(email=email, password=password)
            request.session['cipher'] = emp.email
            print('hi')
            messages.info(request, "SUCCESSFULLY LOGIN")
            return redirect('/cipher_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'cipher/cipher_login.html')


def cipher_id(request):
    if request.method == 'POST':
        email = request.POST['email']
        cipher_team_id(email=email).save()
        messages.info(request,'REQUEST ID SUUCESSFULLY UPDATED!!')
        return redirect('/cipher_index/')
    return render(request, 'cipher/cipher_process_id.html')




def view_user_datas_from_domain(request):
    datas=user_credential_details.objects.filter(bollean=True)
    return render(request, 'cipher/domain_user_final.html',{'datas':datas})




def cipher_id_1(request):
    if request.method == 'POST':
        accessid = request.POST['accessid']
        if int(accessid) == int(3546):

            messages.info(request, "WELCOME TECHNICAL TEAM ")
            print('hi')
            return redirect('/view_user_datas_from_domain/')
        else:

            messages.error(request, "please enter correct wallet id ")
            print('no')
            return redirect('/cipher_id_1/')
    return render(request, 'cipher/cipher_id_1.html')


def cipher_id_2(request):
    if request.method == 'POST':
        accessid = request.POST['accessid']
        if int(accessid) == int(3546):

            messages.info(request, "WELCOME TECHNICAL TEAM ")
            print('hi')
            return redirect('/view_encrypted/')
        else:

            messages.error(request, "please enter correct wallet id ")
            print('no')
            return redirect('/cipher_id_1/')
    return render(request, 'cipher/cipher_id_2.html')


def view_encrypted(request):
    datas = user_credential_details.objects.all()
    return render(request, 'cipher/view_encrypted.html',{'datas':datas})


def enc(request,id):
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
    print(a)
    print(b)
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(f)
    enc=[]
    for i in inputvar:
        encoded_value = base64.b64encode(i.encode("ascii", "strict"))
        enc.append(encoded_value)
    print(enc)
    a = enc[0]
    b = enc[1]
    c = enc[2]
    d = enc[3]
    e = enc[4]
    f = enc[5]
    st = user_credential_details.objects.filter(id=r).update(username=a, email=b,city=c,state=d,url=e,country=f )
    print(a, b,c,d,e,f)
    messages.info(request, "RANDOM ENCRYPTION APPLIED ON THE FOLLOWING DATA")

    return redirect('/view_encrypted/')


def enc1(request,id):
    get = user_credential_details.objects.get(id=id)
    publicKey, privateKey = rsa.newkeys(512)
    r = get.id
    inputvar = []
    get.save()

    get.save()
    a = get.username
    b = get.email
    c = get.city
    d = get.state
    e = get.url
    f = get.country
    print(a)
    print(b)
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(e)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(f)
    x = []
    for i in inputvar:
        encMessage = rsa.encrypt(i.encode(), publicKey)
        # print("original string: ", i)
        # print("encrypted string: ", encMessage)
        x.append(encMessage)

        # print(a)

        # decMessage = rsa.decrypt(encMessage, privateKey).decode()
        # print("decrypted string: ", decMessage)
    #     datas = mechanical_analysis.objects.get(id=id)
    #     datas.car_encrypt = a
    #     datas.save()
    print(x)
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    e = x[4]
    f = x[5]
    st = user_credential_details.objects.filter(id=r).update(username=a, email=b,city=c,state=d,url=e,country=f)
    print(a, b,c,d,e,f)
    messages.info(request, "data encrypted successfully")

    return redirect('/view_encrypted/')


def dec(request,id):
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
    messages.info(request, "data encrypted successfully , ready for hashing...")
    return redirect('/view_decrypted/')




def view_decrypted(request):
    datas = user_credential_details.objects.all()
    return render(request, 'cipher/view_decrypted.html',{'datas':datas})


def cipher_logout(request):
    if 'cipher' in request.session:
        request.session.pop('cipher',None)
        messages.success(request,'SESSION LOGOUT SUCCESSFULLY!!')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin/')





def generate_random(request):
    s=[enc(),enc1()]
    y=random.choice(s)
    print(y)
    return redirect('/view_decrypted/')



def send_id(request):
    datas = decryption_Requst.objects.all()
    return render(request, 'cipher/domain_key_request.html',{'datas':datas})


def domin_send_id_key(request, id):
    datas = decryption_Requst.objects.get(id=id)
    # datas2 = client_purpose.objects.get(id=id)
    # y= datas2.yourname
    t = datas.user_email
    send_mail(
        'Subject here',
        f'welcome Domain User!!! , your team wallet id  is 5421  ',
        'sarath@gmail.com',
        [datas.user_email],
        fail_silently=False,

    )
    messages.info(request, "ID SUUCESSFULLY FORWARDED TO DOMAIN USER")
    # datas.save()
    return redirect('/send_id/')



def send_enc_domin(request,id):
    datas = user_credential_details.objects.get(id=id)
    datas.bollean=False
    datas.save()
    print('hi')
    messages.info(request, "ENCRYPTED DATA FORWARDED TO DOMIAN")
    return redirect('/send_domin/')



