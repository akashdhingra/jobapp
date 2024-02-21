from django.shortcuts import render
from subscribe.forms import SubscribeForm

from subscribe.models import Subscribe

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty=""
    if request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        print("POST REQUEST : ", email)
        if email=="":
            email_error_empty = "No email entered"

        subscribe = Subscribe(first_name = first_name,last_name = last_name,email =email)
        subscribe.save()

    context={"form" : subscribe_form , "email_error_empty":email_error_empty}
    return render(request,'subscribe/subscribe.html',context)