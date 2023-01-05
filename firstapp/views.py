from django.shortcuts import render,redirect,HttpResponse
import random
from authentication_app.models import UserInfo
from django.contrib import messages

def index(request):
    uid=request.session.get("uid")
    if uid is not None:
        return redirect('/home')
    return render(request,'index.html')

def home(request):
    uid=request.session.get("uid")
    obj=UserInfo.objects.get(id=uid)
    d={'name':obj.fullname,'money':obj.money}
    return render(request,'home.html',d)


def play(request):
    uid=request.session.get("uid")
    qno=request.POST.get('qno')
    qno=int(qno)
    print(qno)
    if qno==10:
        obj=UserInfo.objects.get(id=uid)
        obj.money=int(obj.money)+10000000
        obj.save()
        obj1=UserInfo.objects.get(id=uid)
        d={'name':obj1.fullname,'money':obj1.money}
        return render(request,'gamecomplete.html',d)
    elif qno<=10:
        op=("+","-","*")
        question=str(random.randint(0,9))+random.choice(op)+str(random.randint(0,9))+random.choice(op)+str(random.randint(0,9))
        ans=eval(question)  
        options=[ans,ans+random.randint(1,100),ans+random.randint(1,100),ans+random.randint(1,100)]
        random.shuffle(options)    
        if qno==0:
            qno=qno+1    
            d={'question':question,'opta':options[0],'optb':options[1],'optc':options[2],'optd':options[3],'qno':qno}
            return render(request,'play.html',d)
        qno=qno+1    
        d={'question':question,'opta':options[0],'optb':options[1],'optc':options[2],'optd':options[3],'qno':qno}
        qcheck=request.POST.get('question')
        acheck=int(request.POST.get('answer'))
        if eval(qcheck)==acheck:
            return render(request,'play.html',d)
        else:
            print(qno)
            qno=qno-2
            money=[0,1000,10000,25000,50000,160000,320000,640000,1250000,5000000,10000000]
            obj=UserInfo.objects.get(id=uid)
            obj.money=int(obj.money)+money[qno]
            obj.save()
            obj1=UserInfo.objects.get(id=uid)
            d={'name':obj1.fullname,'money':obj1.money}
            return render(request,'wronganswer.html',d)


def transfer(request):
    uid=request.session.get("uid")
    obj=UserInfo.objects.get(id=uid)
    d={'name':obj.fullname,'money':obj.money}
    return render(request,'transfer.html',d)

def transferkbc(request):
    uid=request.session.get("uid")
    receiver=request.POST.get('receiver')
    amount=request.POST.get('amount')
    amount=int(amount)
    obj1=UserInfo.objects.get(id=uid)
    try:
        obj2=UserInfo.objects.get(username=receiver)
    except:
        messages.success(request,"Invalid Details")
        return redirect('/transfer')
    if amount>(int(obj1.money)):
        messages.success(request,"Invalid Details")
        return redirect('/transfer')
    obj1.money=(int(obj1.money))-(amount)
    obj2.money=(int(obj2.money))+(amount)
    obj1.save()
    obj2.save()
    messages.success(request,"Transfer Successfull")
    return redirect('/home')

def transferbp(request):
    uid=request.session.get("uid")
    receiver=request.POST.get('receiver')
    amount=request.POST.get('amount')
    amount=int(amount)
    obj1=UserInfo.objects.get(id=uid)
    if amount>(int(obj1.money)):
        messages.success(request,"Invalid Details")
        return redirect('/transfer')
    return redirect(f'https://vedantbusinessportal.pythonanywhere.com/transfer?receiver={receiver}&amount={amount}&kbcid={uid}')

def transferconfirm(request):
    uid=request.GET.get('kbcid')
    amount=request.GET.get('amount')
    amount=int(amount)
    status=request.GET.get('status')
    if status=='success':
        obj1=UserInfo.objects.get(id=uid)
        obj1.money=(int(obj1.money))-(amount)
        obj1.save()
        messages.success(request,"Transfer Successfull")
        return redirect('/home')
    elif status=='failed':
        messages.success(request,"Invalid Details")
        return redirect('/transfer')

#http://127.0.0.1:8000/transferconfirm?kbcid=4&amount=100&status=success