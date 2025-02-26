from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.views.decorators.cache import never_cache
from . models import *

# Create your views here.

# Login,Logout,Signup Section

@never_cache
def loginPage(request):
    if "username" in request.session:
        return redirect(homePage)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            request.session['username'] = username 
            login(request, user) 
            if user.is_superuser:
                request.session['adminUser'] = username
                return redirect(adminPenel)
            elif user.is_staff:
                request.session['vendorname'] = username 
                return redirect(vendorIndexPage)
            else:
                return redirect(homePage)
        else:
            return redirect(loginPage)

    return render(request, 'registrations/login.html')

def signupPage(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email =  request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password==re_password:
           user = User.objects.create_user(username,email,re_password)
           user.last_name = lastname
           user.first_name = firstname
           user.save()
           return redirect(loginPage)
    return render(request,'registrations/signup.html')

def vendorSignupPage(request):
    if request.method == 'POST':
        companyName = request.POST.get('companyName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password == re_password:
            user = User.objects.create_user(username,email,re_password)
            user.first_name = companyName
            user.is_staff = True
            user.save()
            return redirect(loginPage)
    return render(request,'registrations/vendorSignup.html')

def logout_view(request):
    if 'username' in request.session:
        request.session.flush()
        return redirect(loginPage)
    else:
        return redirect(loginPage) 

def logout_view_vendor(request):
    if 'vendorname' in request.session:
        request.session.flush()
        return redirect(loginPage)
    else:
        return redirect(loginPage) 
    
def logout_view_admin(request):
    if 'adminUser' in request.session:
        request.session.flush()
        return redirect(loginPage)
    else:
        return redirect(loginPage) 

# User Section

def homePage(request):
    if "username" in request.session:
        return render(request,'userInterface/index.html')
    else:
        return redirect(loginPage)


def aboutPage(request):
    return render(request,'userInterface/about.html')

def bookingPage(request):
    return render(request,'userInterface/booking.html')

def contactPage(request):
    return render(request,'userInterface/contact.html')

def destinationPage(request):
    return render(request,'userInterface/destination.html')

def packagePage(request):
    if 'ids' in request.session:
        request.session.flush()

    verified = 'verified'
    items = packages.objects.filter(verification=verified)
    context = {
        'items':items,
    }
    return render(request,'userInterface/package.html',context)

def servicePage(request):
    return render(request,'userInterface/service.html')

def teamPage(request):
    return render(request,'userInterface/team.html')

def testimonialPage(request):
    return render(request,'userInterface/testimonial.html')

def fournotforPage(request):
    return render(request,'userInterface/404.html')

def UserViewSection(request,id):
    item = packages.objects.filter(id=id)
    request.session['ids'] = id
    context = {
        'item':item
    }
    return render(request,'userInterface/userView.html',context)

def UserBookingDetails(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone1')
        altPhone = request.POST.get('phone2')
        passenger = request.POST.get('traveller')
        destination = request.POST.get('destination')
        packager_name = request.POST.get('packager_name')
        
        request.session['passengerName'] = name
        details = bookingDetails(
            name = name,
            email = email,
            phone = phone,
            altPhone = altPhone,
            numTraveller = passenger,
            packager_name = packager_name,
            destination = destination,
        )
        details.save()
        return redirect(checkoutPage)
    
def searchHere(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        items = packages.objects.filter(destination=destination)
        context = {
            'items':items,
        }
        return render(request,'userInterface/package.html',context)
    

def checkoutPage(request):
    id = request.session.get('ids')
    item = packages.objects.filter(id = id).first()
    name = request.session.get('passengerName')
    user = bookingDetails.objects.filter(name = name)
    use = bookingDetails.objects.filter(name = name).first()
    total = item.price*use.numTraveller
    context = {
        'user' : user,
        'total' : total,
    }    
    return render(request,'userInterface/checkout.html',context)



# Vendor Section

def vendorIndexPage(request):
    if "vendorname" in request.session:
        username = request.session['vendorname']
        if request.method == 'POST':
            destination = request.POST.get('destination')
            description = request.POST.get('description')
            duration = request.POST.get('duration')
            price = request.POST.get('price')
            packager_name = request.POST.get('packager_name')
            image1 = request.FILES.get('image1',None)
            image2 = request.FILES.get('image2',None)
            image3 = request.FILES.get('image3',None)
            image4 = request.FILES.get('image4',None)

            item = packages(
                destination = destination,
                description = description,
                duration = duration,
                price = price,
                packager_name = packager_name,
                image1 = image1,
                image2 = image2,
                image3 = image3,
                image4 = image4,
            )
            item.save()
            return redirect(vendorIndexPage)
        user = User.objects.get(username = username)
        vendor_name = user.first_name
        packitems = packages.objects.filter(packager_name = vendor_name)
        verified = 'verified'
        items = packitems.filter(verification = verified)
        context = {
            'items':items,
            'user':user,
        }
        return render(request,'vendorSection/index.html',context)
    return redirect(loginPage)

def vendorPackageView(request,id):
    item = packages.objects.filter(id=id)
    context = {
        'item':item
    }
    if request.method == 'POST':
        destination = request.POST.get('destination')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        packager_name = request.POST.get('packager_name')
        image1 = request.FILES.get('image1',None)
        image2 = request.FILES.get('image2',None)
        image3 = request.FILES.get('image3',None)
        image4 = request.FILES.get('image4',None)
        edited = packages(
            id = id,
            destination = destination,
            description = description,
            duration = duration,
            price = price,
            packager_name = packager_name,
            image1 = image1,
            image2 = image2,
            image3 = image3,
            image4 = image4,
        )
        edited.save()
        return redirect(vendorIndexPage)
    return render(request,'vendorSection/view.html',context)

def vendorBookingSection(request):
    return render(request,'vendorSection/booking.html')

# Admin Section

def adminPenel(request):
    if 'adminUser' in request.session:
        verified = 'Not Verified'
        items = packages.objects.filter(verification=verified)
        context = {
            'items':items,
        }
        return render(request,'adminSection/index.html',context)
    else:
        return redirect(loginPage)

def verification(request,id):
    item = packages.objects.get(id=id)
    verified = 'verified'
    item.verification=verified
    item.save()
    return redirect(adminPenel)

def viewSection(request,id):
    item = packages.objects.filter(id=id)
    context = {
        'item':item
    }
    return render(request,'adminSection/view.html',context)

def removeSection(request,id):
    item = packages.objects.filter(id=id)
    item.delete()
    return redirect(adminPenel)


def AdminPanelUserSection(request):
    is_staff = False
    user = User.objects.filter(is_staff = is_staff)
    context = {
        'user':user,
    }
    return render(request,'adminSection/userSection.html',context)

def AdminPanelVendorSection(request):
    is_staff = True
    user = User.objects.filter(is_staff = is_staff)
    context = {
        'user':user,
    }
    return render(request,'adminSection/vendorSection.html',context)