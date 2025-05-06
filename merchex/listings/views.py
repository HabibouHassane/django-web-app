from django.http import HttpResponse
from listings.models import Band, Listing
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from listings.forms import ContactUsForm, BandForm, ListingForm

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

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            # print("Formulaire valide, groupe créé :", band)  # Ajouté
            return redirect('band-detail', band.id)
        # else:
        #     print("Formulaire invalide :", form.errors)  # Ajouté
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            # print("Formulaire valide, groupe créé :", listing)  # Ajouté
            return redirect('listing-detail', listing.id)
        # else:
        #     print("Formulaire invalide :", form.errors)  # Ajouté
    else:
        form = ListingForm()
    return render(request, 'listings/band_create.html', {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})


def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request,
                'listings/listing_update.html',
                {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')


    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        listing.delete()
        # rediriger vers la liste des groupes
        return redirect('listing-list')


    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/listing_delete.html',
                    {'listing': listing})



