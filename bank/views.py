from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Customers, Transfer
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


def users(request):
    customer=Customers.objects.all()
    return render(request,'users.html',{'customer':customer})

def profile(request, acc):
    profile=Customers.objects.filter(id=acc)
    history=Transfer.objects.filter(acc1=acc, status="Success")
    return render(request, 'profile.html',{'profile': profile, 'transferhistory':history})

def search(request):
    query = request.GET.get('search')
    profile = "/profile/"+query
    print(profile)
    return redirect(profile)

def transfer(request):
    return render(request, 'transfer.html')

def handletransfer(request):
    if request.method=="POST":
        sname=request.POST['sname']
        acc1=request.POST['acc1']
        bal=request.POST['bal']
        rname=request.POST['rname']
        acc2=request.POST['acc2']
        comment=request.POST['comment']
        if acc1==acc2:
            messages.error(request,"Sender's and Receiver Account No. cannot be the same")
        else:
            if Customers.objects.filter(id=acc1) and Customers.objects.filter(id=acc2):
                x = Customers.objects.get(id=acc1)
                y = Customers.objects.get(id=acc2)
                if int(bal)<=x.cust_balance:
                    x.cust_balance = int(x.cust_balance)-int(bal)
                    y.cust_balance = int(y.cust_balance)+int(bal)
                    x.save()
                    y.save()
                    transfer=Transfer(sname=sname, acc1=acc1, bal=bal, rname=rname, acc2=acc2, comment=comment, status="Success")
                    transfer.save()
                    messages.success(request, "Successfully Transfered")
                else:
                    transfer=Transfer(sname=sname, acc1=acc1, bal=bal, rname=rname, acc2=acc2, comment=comment, status="Failed")
                    transfer.save()
                    messages.error(request,"Insufficient Balance")
            else:
                transfer=Transfer(sname=sname, acc1=acc1, bal=bal, rname=rname, acc2=acc2, comment=comment, status="Failed")
                transfer.save()
                messages.error(request,"Wrong Account No.")
        return redirect('Transfer')

