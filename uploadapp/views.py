from django.shortcuts import redirect, render
from django.urls import reverse

from uploadapp.forms import UploadForm

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect(reverse('thank_you'))
    else:
        form = UploadForm()
    return render(request,'uploadapp/add_image.html',{'form':form})

def thank_you(request):
    context = {}
    return render(request,'uploadapp/thankyou.html',context)