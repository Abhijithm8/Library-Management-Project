from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from libraryapp.models import Course, Student, Books, Issue_Book, A


# Create your views here.

@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def adminreg_fun(request):
    return render(request,'admin_reg.html',{'data':''})


def admindata_fun(request):
    user_name = request.POST['tbname']
    user_email = request.POST['tbemail']
    user_password = request.POST['tbpswd']
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request,'admin_reg.html',{'data':'username and email already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name,email=user_email,password=user_password)
        u1.save()
        return redirect('login')


def login_fun(request):
    return render(request,'login.html')


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def stdreg_fun(request):
    c1 = Course.objects.all()
    return render(request,'std_reg.html',{'course': c1})


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def stddata_fun(request):
    s1 = Student()
    s1.student_name = request.POST['tbname']
    s1.student_phno = request.POST['tbphno']
    s1.student_sem = request.POST['tbsem']
    s1.student_password = request.POST['tbpswd']
    s1.student_course = Course.objects.get(course_name = request.POST['ddlcourse'])
    s1.save()
    return redirect('login')


def logdata_fun(request):
    user_name = request.POST['tbname']
    A.x = user_name
    user_password = request.POST['tbpswd']
    user1 = authenticate(username = user_name,password = user_password)

    if user1 is not None:
        if user1.is_superuser:
            login(request, user1)
            return redirect('adminhome')
    elif Student.objects.filter(Q(student_name = user_name) & Q(student_password = user_password)).exists():
        return render(request,'student_home.html',{'data': user_name})
    else:
        return render(request, 'login.html',{'data':'invalid username and password'})


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def stdhome_fun(request):
    return render(request,'student_home.html')


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def adminhome_fun(request):
    return render(request,'admin_home.html')


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def addbook_fun(request):
    c1 = Course.objects.all()
    return render(request,'addbook.html',{'course':c1})


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def bookdata_fun(request):
    b1 = Books()
    b1.book_name = request.POST['tbname']
    b1.author_name = request.POST['tbaname']
    b1.course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
    b1.save()

    return redirect('addbook')


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def display_fun(request):
    b1 = Books.objects.all()
    return render(request,'display.html',{'data':b1})


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def update_fun(request,id):
    b1 = Books.objects.get(id=id)
    c1 = Course.objects.filter()
    if request.method == 'POST':
        b1.book_name = request.POST['tbbname']
        b1.author_name = request.POST['tbaname']
        b1.course_id = Course.objects.get(course_name = request.POST['ddlcourse'])
        b1.save()
        return redirect('display')
    return render(request,'update.html', {'course':c1,'book':b1})


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def delete_fun(request,id):
    b1 = Books.objects.get(id=id)
    b1.delete()
    return redirect('display')



@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def log_out_fun(request):
    logout(request)
    return redirect('login')


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def assignbook_fun(request):
    c1 = Course.objects.all()
    if request.method == 'POST':
        c2 = Course.objects.get(course_name=request.POST['ddlcourse'])
        c = c2.id
        s1 = Student.objects.filter(Q(student_sem= request.POST['tbssem']) & Q(student_course=c))
        b1 = Books.objects.filter(course_id=c)
        return render(request,'assignbook.html',{'data':s1,'book': b1, 'course': c1})
    return render(request,'assignbook.html',{'course':c1})


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def abookdata_fun(request):
    i1 = Issue_Book()
    i1.std_name = Student.objects.get(student_name=request.POST['ddlsn'])
    i1.bk_name = Books.objects.get(book_name=request.POST['ddlbname'])
    i1.start_date = request.POST['tbsdate']
    i1.end_date = request.POST['tbedate']
    i1.save()
    return redirect('assignbook')


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def issuebook_fun(request):
    i1 = Issue_Book.objects.all()
    return render(request,'issuebook.html',{'data':i1})


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def updateissuebk_fun(request,id):
    i1 = Issue_Book.objects.get(id=id)
    b1 = Books.objects.all()
    if request.method == 'POST':
        i1.std_name = Student.objects.get(student_name=request.POST['tbsname'])
        i1.bk_name = Books.objects.get(book_name=request.POST['ddlbname'])
        i1.start_date = request.POST['tbsdate']
        i1.end_date = request.POST['tbedate']
        i1.save()
        return redirect('issuebook')
    return render(request,'updateissuebook.html',{'data':i1, 'book':b1})


@login_required
@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def deleteissuebk_fun(request,id):
    i1 = Issue_Book.objects.get(id=id)
    i1.delete()
    return redirect('issuebook')



@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def issuedbkdata_fun(request):
    s1 = Student.objects.get(student_name=A.x)
    i_d = s1.id
    b1 = Issue_Book.objects.filter(std_name = i_d)
    return render(request,'issuedbkdata.html',{'data': b1})


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def logoutstd_fun(request):
    logout(request)
    return redirect('login')


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def stdprofile_fun(request):
    username = A.x
    s1 = Student.objects.get(student_name=username)
    if request.method == 'POST':
        return render(request, 'updateprofile.html', {'sd': s1})
    return render(request, 'stdprofile.html', {'data': username, 'sd': s1})


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def updateprofile_fun(request):
    return render(request, 'updateprofile.html')


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def profiledata_fun(request):
    s1 = Student.objects.get(student_name=A.x)
    s1.student_name = request.POST['tbuname']
    s1.student_phno = request.POST['tbphno']
    s1.student_sem = request.POST['tbsem']
    s1.student_password = request.POST['tbpass']
    s1.save()
    A.x = request.POST['tbuname']
    return redirect('stdprofile')