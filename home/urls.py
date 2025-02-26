from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Login,Logout and Signup Section
    path('',views.loginPage,name='loginPage'),
    path('signup/',views.signupPage,name='signup'),
    path('vendorSignup/',views.vendorSignupPage,name='vendorSignup'),
    path('logoutUser/',views.logout_view,name='logoutUser'),
    path('logoutVendor/',views.logout_view_vendor,name='logoutVendor'),
    path('logoutadmin/',views.logout_view_admin,name='logoutAdmin'),
    # User Section
    path('homePage/',views.homePage,name='homepage'),
    path('aboutPage/',views.aboutPage,name='aboutPage'),
    path('bookingPage/',views.bookingPage,name='bookingPage'),
    path('contactPage/',views.contactPage,name='contactPage'),
    path('destinationPage/',views.destinationPage,name='destinationPage'),
    path('packagePage/',views.packagePage,name='packagePage'),
    path('servicePage/',views.servicePage,name='servicePage'),
    path('teamPage/',views.teamPage,name='teamPage'),
    path('testimonialPage/',views.testimonialPage,name='testimonialPage'),
    path('fournotfourPage/',views.fournotforPage,name='fournotfourPage'),
    path('userviewSection/<int:id>/',views.UserViewSection,name='Userviewsection'),
    path('bookingDetails/',views.UserBookingDetails,name='bookingDetails'),
    path('searchHere/',views.searchHere,name='searchHere'),
    path('checkoutPage/',views.checkoutPage,name='checkoutPage'),
    # Vendor Section
    path('vendorpage/',views.vendorIndexPage,name='vendorpage'),
    path('bookigVendor/',views.vendorBookingSection,name='vendorBooking'),
    path('vendorPackageView/<int:id>',views.vendorPackageView,name='vendorPackageView'),
    # Admin Section
    path('adminpanel/',views.adminPenel,name='adminpanel'),
    path('verification/<int:id>/',views.verification,name='verification'),
    path('viewsection/<int:id>/',views.viewSection,name='viewsection'),
    path('removeItem/<int:id>/',views.removeSection,name='removeItem'),
    path('AdminPanelUserSection/',views.AdminPanelUserSection,name='AdminPanelUserSection'),
    path('AdminPanelVendorSection/',views.AdminPanelVendorSection,name='AdminPanelVendorSection'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)