from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(
            listing=listing,
            listing_id = listing_id,
            name = name,
            email = email,
            phone = phone,
            message = message,
            user_id = user_id
            
        )

        contact.save()

        messages.success(
                request, 
                'Your inquiry has been submitted successfully'
            )
        return redirect('/listings/'+listing_id)

    else:
        return redirect('listings')