from django.urls import path

from libraryapp import views

urlpatterns = [
    path('adminreg',views.adminreg_fun,name='adminreg'),
    path('admindata',views.admindata_fun),
    path('',views.login_fun,name='login'),
    path('stdreg',views.stdreg_fun,name='stdreg'),
    path('stddata',views.stddata_fun),
    path('logdata',views.logdata_fun),
    path('stdhome',views.stdhome_fun,name='stdhome'),
    path('adminhome',views.adminhome_fun,name='adminhome'),
    path('addbook',views.addbook_fun,name='addbook'),
    path('bookdata',views.bookdata_fun),
    path('displaybook',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('delete/<int:id>',views.delete_fun,name='delete'),
    path('log_out',views.log_out_fun,name='log_out'),
    path('assignbook',views.assignbook_fun,name='assignbook'),
    path('abookdata',views.abookdata_fun),
    path('issuebook',views.issuebook_fun,name='issuebook'),
    path('updateissuebk/<int:id>',views.updateissuebk_fun, name='updateissuebk'),
    path('deleteissuebk/<int:id>',views.deleteissuebk_fun, name='deleteissuebk'),
    path('issuedbkdata',views.issuedbkdata_fun,name='issuedbkdata'),
    path('logoutstd',views.logoutstd_fun,name='logoutstd'),
    path('stdprofile',views.stdprofile_fun,name='stdprofile'),
    path('updateprofile',views.updateprofile_fun,name='updateprofile'),
    path('uprofiledata',views.profiledata_fun)



]