from django.shortcuts import render, redirect


from django.shortcuts import render
from django.contrib import messages
from .models import *


# Create your views here.
def user_index(request):
    return render(request, 'users/user_index.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            emp = user_register.objects.get(email=email, password=password)
            request.session['user'] = emp.email
            print('hi')
            messages.info(request, "successfully login")
            return redirect('/user_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'users/user_new_login.html')


def submit(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        user_register(username=username, email=email, password=password, contact=contact, address=address
                      ).save()
        messages.info(request, "SUCCESSFULLY REGISTERED !! READY FOR LOGIN")
        return redirect('/user_login/')
    return render(request, 'users/user_register.html')



def domain_register_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        purpose = request.POST['purpose']
        email = request.POST['email']
        type = request.POST['type']
        password = request.POST['password']
        domain_register(name=name, purpose=purpose, email=email, type=type, password=password
                      ).save()
        messages.info(request, "DETAILS UPDATED SUCCESSFULLY NEXT PLEASE ENTER YOUR PURPOSE!")
        return redirect('/user_index/')
    return render(request, 'users/domain_register.html')


def domain_purpose_form(request):
    datas = domain_register.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        organisation = request.POST['organisation']
        email = request.POST['email']
        purpose = request.POST['purpose']
        enquiry = request.POST['enquiry']
        domain_purpose_register(name=name, organisation=organisation, email=email, purpose=purpose, enquiry=enquiry
                        ).save()
        messages.info(request, "Successfully updated Please wait for admin approval for virtual box!")
        return redirect('/user_index/')
    return render(request, 'users/domain_purpose.html',{datas:'datas'})




def user_virtual(request):
    datas= domain_purpose_register.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']
        enquiry = request.POST['enquiry']
        address = request.POST['address']
        user_detail(name=name, email=email, password=password, gender=gender, address=address,
                         enquiry=enquiry
                         ).save()
        messages.info(request, "USER DETAILS UPDATED SUUCESSFULLY!!")
        return redirect('/user_index/')
    return render(request, 'users/user_login_form.html',{'datas':datas})



def domin_user_p(request):
    datas = domain_purpose_register.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        country = request.POST['country']
        url= request.POST['url']
        file = request.FILES['file']
        user_credential_details(url=url,username=username, email=email, street=street, city=city, state=state,pincode=pincode,country=country,
        file=file
        ).save()
        messages.info(request, "USER CREDENTIAL DETAILS UPDATED SUCCESSFULLY")
        return redirect('/user_index/')

    return render(request, 'users/user_purpose_form.html')



def user_logout(request):
    if 'user' in request.session:
        request.session.pop('user',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin/')







