from django.shortcuts import redirect, render
from .models import Customers, Transfer
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def users(request):
    customer=Customers.objects.all()
    return render(request,'users.html',{'customer':customer})

def profile(request, acc):
    profile=Customers.objects.filter(id=acc)
    history=Transfer.objects.filter(sender=acc, status="Success")
    return render(request, 'profile.html',{'profile': profile, 'transferhistory':history})

def search(request):
    query = request.GET.get('search')
    profile = "/profile/"+query
    print(profile)
    return redirect(profile)

def transfer(request):
    customer=Customers.objects.all()
    return render(request, 'transfer.html',{'customer':customer})

def handletransfer(request):
    if request.method=="POST":
        sender = request.POST['sender']
        receiver = request.POST['receiver']
        bal=request.POST['bal']
        comment=request.POST['comment']
        if comment=="":
            comment=" - "
        if sender==receiver:
            messages.error(request,"Sender's and Receiver Account No. cannot be the same")
        elif int(bal)<=0:
            messages.error(request, "Invalid Amount")
        else:
            if Customers.objects.filter(id=sender) and Customers.objects.filter(id=receiver):
                x = Customers.objects.get(id=sender)
                y = Customers.objects.get(id=receiver)
                if int(bal)<=x.cust_balance:
                    x.cust_balance = int(x.cust_balance)-int(bal)
                    y.cust_balance = int(y.cust_balance)+int(bal)
                    x.save()
                    y.save()
                    transfer=Transfer(sender=sender, receiver=receiver, bal=bal, comment=comment, status="Success")
                    transfer.save()
                    messages.success(request, "Successfully Transfered")
                else:
                    transfer=Transfer(sender=sender, receiver=receiver, bal=bal, comment=comment, status="Failed")
                    transfer.save()
                    messages.error(request,"Insufficient Balance")
        return redirect('Transfer')

