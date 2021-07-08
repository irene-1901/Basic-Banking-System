from django.shortcuts import render
# Create your views here.
# from .forms import TransactionsForm
# from django.http import HttpResponseRedirect
from .models import *


# def home_view(request):
# logic of view will be implemented here
#    print(request.GET)
#    return render(request, "ViewOne.html")


def index(request):
    return render(request, "index.html")


def transactions(request):
    object2 = Transaction.objects.all()
    object3 = User.objects.all()
    context = {
        'object2':object2,
        'object3':object3,
    }
    if request.method == "POST":
        senderemail = request.POST['sender']
        amount = request.POST['amount']
        receiveremail = request.POST['receiver']
        print(senderemail, amount, receiveremail)
        ins = TransactionsForm(sender=senderemail, amount=amount, receiver=receiveremail)
        ins.save()
        try:
            amount = int(amount)
        except:
            print("enter amount")
        for i in object3:
            print(receiveremail)
            if i.email == receiveremail:
                j = i
                id = i.id
                break
        for i in object3:
            print(i.email, i.balance, senderemail)
            if i.email == senderemail and amount < i.balance and amount > 0:
                avail_bal = i.balance - amount
                avail_bal2 = j.balance + amount
                try:
                    query1 = Transaction(name=i.name, email=i.email, deb_amt=amount, cr_amt=0, acc_bal=avail_bal)
                    query2 = User(id=i.id,img=i.img , name=i.name, age=i.age, gender = i.gender, address = i.address, city = i.city, pincode = i.pincode, country = i.country, phone=i.phone,  email=i.email, balance=avail_bal)
                    query3 = Transaction(name=j.name, email=j.email, deb_amt=0, cr_amt=amount, acc_bal=avail_bal2)
                    query4 = User(id=id,img=i.img , name=j.name , age=j.age, gender = j.gender, address = j.address, city = j.city, pincode = j.pincode, country = j.country, phone=j.phone, email=j.email, balance=avail_bal2, )
                    query2.save()
                    query1.save()
                    query4.save()
                    query3.save()

                    return render(request, 'Transaction.html', context)
                except:
                    print("transaction failed")
                    break
        else:
            print("invalid data")
    return render(request, 'Transaction.html', context)


def view(request):
    object1 = User.objects.all()
    return render(request, 'View.html', {'object1': object1})


def home_view(request, pk):
    customer = User.objects.get(id = pk)

    context = {
        'customer':customer,

    }
    return render(request, "ViewOne.html", context)