from django.shortcuts import render
from django.http import request,HttpResponse
from .models import reg,cars,carbook,booked
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    return render(request,'b.html')

def home1(request):
    username= request.session['username']
    return render(request,'home1.html',{'username':username})

def login(request):
    return render(request,'login.html')

def about1(request):
    username= request.session['username']
    return render(request,'about1.html',{'username':username})

def logout(request):
    try:

        del request.session['username'] 
        del request.session['gmail'] 
        del request.session['phone'] 
        del request.session['gender'] 
        del request.session['fname'] 
        del request.session['lname'] 
        del request.session['typeo']
    except:
        pass
    return render(request,'b.html')

def profile(request):
    username= request.session['username']
    objs=reg.objects.get(uname=username)
    return render(request,'profile.html',{'objs':objs})

def home(request):
    return render(request,'b.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def contact1(request):
    username= request.session['username']
    return render(request,'contact1.html',{'username':username})

def cars0(request):
    return render(request,'cars.html')

def cars1(request):
    username= request.session['username']
    objs=cars.objects.all()
    return render(request,'cars1.html',{'objs':objs,'username':username})

def registration(request):
    return render(request,'registration.html')

def addcard(request):
    username=request.session['username']
    return render(request,'addcard.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def success2(request):
    username=request.session['username']


    
    obj=carbook.objects.filter(username=username).update(status='booked')
    return render(request,'success2.html')

def booked(request):
    username= request.session['username']
    if carbook.objects.filter(username=username).exists():

        objs=carbook.objects.get(username=username)
        a=cars.objects.get(name=objs.carname)
        return render(request,'booked.html',{'a':a})
    else:
        return render(request,'nobooked.html')


def regi(request):
    fname=request.POST['fname']
    lname=request.POST['lastname']
    uname=request.POST['username']
    phone=request.POST['phone']
    gender=request.POST['gender']
    answer=request.POST['answer']
    password=request.POST['password']
    email=request.POST['gmail']
    image=request.POST['image1']
    typeo="USER"
    
    ins=reg(image=image,fname=fname,lname=lname,uname=uname,phone=phone,gender=gender,answer=answer,password=password,email=email,typeo=typeo)
    ins.save()
    subject="no-rply"
    email=email
    email=EmailMessage(subject,"Congratulations, Account created successfully",to=[email])  #to will take list of email IDs
    email.send()

    return render(request,'success.html')

def logincheck(request):
    username=request.POST['username']
    pwd=request.POST['password']
    print(username,pwd)
    objs=reg.objects.all()
    for o in objs:
        if (o.uname == username):
            if ( o.password == pwd):
                request.session['username'] =o.uname
                request.session['gmail'] =o.email
                request.session['phone'] =o.phone
                request.session['gender'] =o.gender
                request.session['typeo'] =o.typeo
                request.session['fname'] =o.fname
                request.session['lname'] =o.lname
                return render (request,'home1.html',{'username':username})
            
    else:
        return render (request,'login.html')
        

def confirmcar(request):
    username= request.session['username']
    k=carbook.objects.filter(username=username).exists()
    if (k):

        return render(request,'booked.html')
    else:
        name=request.GET['name']
        request.session['name'] =name
    
        objs=cars.objects.get(name=name)
        return render(request,'confirmcar.html',{'objs':objs,'username':username})
        

def delete(request):
    username=request.session['username']
    if carbook.objects.filter(username=username).exists():

        objs=carbook.objects.get(username=username)
        objs.delete()
        return render(request,'nobooked.html')





def confirmcar1(request):
    username= request.session['username']
    fname=request.POST['fname']
    lname=request.POST['lname']
    licence=request.POST['licence']
    image1=request.POST['image1']
    date=request.POST['pickup']
    
    name=request.session['name']
    ins=carbook(pickdate=date,carname=name,username=username,fname=fname,lname=lname,licence=licence,image=image1)
    ins.save()
    
    f=cars.objects.get(name=name)
    s=f.start_price
    subject="no-rply"
    email=request.session['gmail']
    email=EmailMessage(subject,"Congratulations, you have successfully booked",to=[email])  #to will take list of email IDs
    email.send()
    return render(request,'book.html',{'name':name,'f':f})


def sendmail(request):
    subject="mail vachindhi"
    email='pinkuchigurupati@gmail.com'
    email=EmailMessage(subject,"All The Best",to=[email])  #to will take list of email IDs
    email.send()
    return HttpResponse("Success")