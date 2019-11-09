from django.shortcuts import render,get_object_or_404
import contact.models

def contactme(request, contact_id):
    contact_details = get_object_or_404(contact , pk = contact_id)
    if request.method == 'POST':
        contact_details.email_id = request.POST.get('emailid','')
    contact_details.save()
    return render(request,'contact/contact.html')
