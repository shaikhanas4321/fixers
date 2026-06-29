from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect ,JsonResponse
from accounts.models import *
from django.contrib.auth.decorators import login_required
from services.models import *
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
import json
# Create your views here.
@login_required
def index(request):
    user = request.user
    complete = False
    if user.user_type == "CUSTOMER":
        try:
            profile = CustomerProfile.objects.get(user=user)

            if profile.phone.strip() and profile.address.strip():
                profile.user.profile_completed = True
                profile.user.save()
                complete = True
            else:
                profile.user.profile_completed = False
                profile.user.save()
                complete = False

        except CustomerProfile.DoesNotExist:
            complete = False
        return render(request , "services/index.html",{
            "complete":complete
        })
    if user.user_type == "PROVIDER":
        try:
           profile= ProviderProfile.objects.get(user=user)
           if (bool(profile.skills) and  bool(profile.experience_years) and bool(profile.bio) and bool(profile.phone) and bool(profile.is_active)):
                profile.user.profile_completed = True
                profile.user.save()
                comp = True
           else:
                profile.user.profile_completed = False
                profile.user.save()
                comp = False   
        except:
                profile.user.profile_completed = False
                profile.user.save()
                comp = False
        return render(request, "services/index.html", {
          "comp":comp
          })

    

@login_required
def completion(request):
    if request.method=="POST":
        profile = CustomerProfile.objects.get(user=request.user)
        profile.phone=request.POST.get("phone")
        house = request.POST["house_number"]
        street = request.POST["street"]
        city = request.POST["city"]
        full_address = f"House {house}, Street {street}, {city}"
        profile.address = full_address
        profile.save()
        return HttpResponseRedirect(reverse("services:index"))
    else:
        profile = CustomerProfile.objects.get(user=request.user)
        return render(request , "services/completion.html",{
            "profile":profile
        })
    
def provider(request):
    
        profile, created = ProviderProfile.objects.get_or_create(user=request.user)       
        if request.method == "POST":
            skill_id = request.POST.get("skill")
            profile.experience_years = request.POST.get("experience_years")
            profile.bio = request.POST.get("bio")
            profile.skills = skills.objects.get(id=skill_id)
            profile.phone=request.POST.get("phone")
            if request.POST.get("available") == "yes":
                 profile.is_active=True
            else:
                 profile.is_active=False
            profile.save()
            return HttpResponseRedirect(reverse("services:index"))
        
        return render(request, "services/completion.html", {
        "skills": skills.objects.all()
    })

@login_required
def listing(request):
      providers=ProviderProfile.objects.filter(is_active=True)
      return render(request , "services/listing.html",{
          "providers":providers
     })
@login_required
def calling(request , provider):
     if request.method=="POST":
      provider_user = get_object_or_404(User, username=provider)
      service_request.objects.create(customer=request.user , provider=provider_user , status="PENDING")
      return HttpResponseRedirect(reverse("services:index"))
 
@login_required
def jobs(request , provider):
    expire_old_requests()
    provider_user = User.objects.get(username=provider)
    jobs=service_request.objects.filter(provider=provider_user)
    return render(request ,"services/jobs.html",{
         "jobs":jobs
    })


def expire_old_requests():
    time_limit = timezone.now() - timedelta(minutes=30)

    service_request.objects.filter(
        status='pending',
        created_at__lt=time_limit
    ).update(status='expired')

@login_required
def status_update(request ,j_id):
    if request.method=="POST":
     data=json.loads(request.body)
     status=data.get("status")
     job=service_request.objects.get(id=j_id)
     job.status=status
     job.save()
     return JsonResponse({
         "success":True,
         "status":status
     })
    return JsonResponse({"success":False})

    