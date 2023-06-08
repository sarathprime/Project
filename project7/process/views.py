from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from user.models import *
from domain.models import *
from django.core.mail import send_mail


import pandas as pd
import numpy as np
import random
import warnings
warnings.filterwarnings('ignore')



# Machine Learning Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
urls_data = pd.read_csv("adata.csv")












# Create your views here.
def process_index(request):
    return render(request, 'process/process_index.html')




def process_login_form(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            emp = process_register.objects.get(email=email, password=password)
            request.session['process'] = emp.email
            print('hi')
            messages.info(request, "SUCCESSFULLY LOGIN")
            return redirect('/process_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'process/process_login.html')


def process_register_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        process_register(username=username, email=email, password=password, contact=contact, address=address
                      ).save()
        messages.info(request, "SUCCESSFULLY REGISTER READY FOR LOGIN!!")
        return redirect('/process_login_form/')
    return render(request, 'process/process_register.html')



def process_id(request):
    if request.method == 'POST':
        email = request.POST['email']
        process_team_id(email=email).save()
        messages.info(request,'REQUEST ID FORWARDED TO ADMIN')
        return redirect('/process_index/')
    return render(request, 'process/process_id.html')



def process_id_1(request):
    if request.method == 'POST':
        accessid = request.POST['accessid']
        if int(accessid) == int(1124):

            messages.info(request, "WELCOME PROCESS TEAM ")
            print('hi')
            return redirect('/view_domain_user_detail/')
        else:

            messages.error(request, "PLEASE ENTER CORRECT WALLET ID ")
            print('no')
            return redirect('/process_id_1/')
    return render(request, 'process/process_id_1.html')



def process_id_2(request):
    if request.method == 'POST':
        accessid = request.POST['accessid']
        if int(accessid) == int(1124):

            messages.info(request, "WELCOME PROCESS TEAM ")
            print('hi')
            return redirect('/view_domain_user_purpose/')
        else:

            messages.error(request, "please enter correct wallet id ")
            print('no')
            return redirect('/process_id_2/')
    return render(request, 'process/process_id_2.html')


def process_id_3(request):
    if request.method == 'POST':
        accessid = request.POST['accessid']
        if int(accessid) == int(1124):

            messages.info(request, "WELCOME PROCESS TEAM ")
            print('hi')
            return redirect('/view_domain_user_final/')
        else:

            messages.error(request, "please enter correct wallet id ")
            print('no')
            return redirect('/process_id_3/')
    return render(request, 'process/process_id_3.html')





def view_domain_user_detail(request):
    datas=user_detail.objects.all()
    return render(request, 'process/view_user.html',{'datas':datas})



def view_domain_user_purpose(request):
    datas=user_credential_details.objects.all()
    return render(request, 'process/view_user_credential.html',{'datas':datas})




def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')	# make tokens after splitting by slash
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')	# make tokens after splitting by dash
        tkns_ByDot = []
        for j in range(0,len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')	# make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))	#remove redundant tokens
    if 'com' in total_Tokens:
        total_Tokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
    return total_Tokens



def predection(request,id):
    datas=user_credential_details.objects.get(id=id)
    x=datas.url
    print(x)
    r=datas.id
    datas.save()
    y = urls_data["label"]
    url_list = urls_data["url"]
    vectorizer = TfidfVectorizer(tokenizer=makeTokens)
    X = vectorizer.fit_transform(url_list)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logit = LogisticRegression()
    logit.fit(X_train, y_train)
    print("Accuracy ", logit.score(X_test, y_test))
    X_predict = [x]
    X_predict = vectorizer.transform(X_predict)
    New_predict = logit.predict(X_predict)
    print(New_predict)
    x=str(New_predict)
    x.lstrip("'['")
    x.rstrip("']")
    k = New_predict[0]
    print(k)
    print(x)
    st = user_credential_details.objects.filter(id=r).update(predict=k)
    messages.info(request, "PREDICTION SUCCESSFULL NOW YOU CAN VIEW DATA!!")
    return redirect('/view_domain_user_purpose/')









def view_domain_user_final(request):
    datas=user_credential_details.objects.filter(bollean=False)
    return render(request, 'process/user_credential_final.html',{'datas':datas})



def send_technical_team(request,id):
    datas = user_credential_details.objects.get(id=id)
    datas.bollean=True
    datas.save()
    print('hi')
    messages.info(request, "INFORMATION FORWARDED TECHNICAL TEAM")
    return redirect('/view_domain_user_final/')





def domian_send_id_key_file(request, id):
    datas = decryption_Requst_2.objects.get(id=id)
    # datas2 = client_purpose.objects.get(id=id)
    # y= datas2.yourname
    t = datas.user_email
    send_mail(
        'Subject here',
        f'welcome Domain User!!! , your team wallet id  is 1721  ',
        'sarath@gmail.com',
        [datas.user_email],
        fail_silently=False,

    )
    messages.info(request, "id successfully sent to technical email id")
    # datas.save()
    return redirect('/a_index/')


def process_logout(request):
    if 'process' in request.session:
        request.session.pop('process',None)
        messages.success(request,'SESSION LOGOUT SUCCESSFULLY')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin/')


def view_domains_request(request):
    datas = decryption_Requst_2.objects.all()
    return render(request, 'process/view_request.html', {'datas': datas})





def view_dmoin_Request(request):
    datas=decryption_Requst_2.objects.all()
    return render(request, 'process/domain_file_request.html',{'datas':datas})




