from django.http import HttpResponse
from listings.models import Band, Listing
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from listings.forms import ContactUsForm 

def band_list(request):
    bands = Band.objects.all()
    return render(request,'listings/band_list.html',{'bands': bands})

def listing_list(request):
    listings = Listing.objects.all()
    return render(request,'listings/listing_list.html',{'listings': listings})

def about(request):
    return render(request,'listings/about.html')

def listings(request):
    bands = Band.objects.all()
    return render(request,'listings/listings.html',{'bands': bands})

def contact(request):
    # print('La methodede requete est :',request.method)
    # print("les données POST sont :",request.POST)
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Mesage from {form.cleaned_data['name'] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else :
        form = ContactUsForm()
    return render(request,
                  'listings/contact.html',
                  {'form':form})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 
                  'listings/band_detail.html', 
                  {'band':band})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 
                  'listings/listing_detail.html', 
                  {'listing':listing})


