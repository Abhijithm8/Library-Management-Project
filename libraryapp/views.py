from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from libraryapp.models import Course, Student, Books, Issue_Book, A


# Create your views here.
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


def stdreg_fun(request):
    c1 = Course.objects.all()
    return render(request,'std_reg.html',{'course': c1})


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
            return redirect('adminhome')
    elif Student.objects.filter(Q(student_name = user_name) & Q(student_password = user_password)).exists():
        return render(request,'student_home.html',{'data': user_name})
    else:
        return render(request, 'login.html',{'data':'invalid username and password'})


def stdhome_fun(request):
    return render(request,'student_home.html')


def adminhome_fun(request):
    return render(request,'admin_home.html')


def addbook_fun(request):
    c1 = Course.objects.all()
    return render(request,'addbook.html',{'course':c1})


def bookdata_fun(request):
    b1 = Books()
    b1.book_name = request.POST['tbname']
    b1.author_name = request.POST['tbaname']
    b1.course_id = Course.objects.get(course_name=request.POST['ddlcourse'])
    b1.save()

    return redirect('addbook')


def display_fun(request):
    b1 = Books.objects.all()
    return render(request,'display.html',{'data':b1})


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


def delete_fun(request,id):
    b1 = Books.objects.get(id=id)
    b1.delete()
    return redirect('display')


def log_out_fun(request):
    return redirect('login')


def assignbook_fun(request):
    c1 = Course.objects.all()
    if request.method == 'POST':
        c2 = Course.objects.get(course_name=request.POST['ddlcourse'])
        c = c2.id
        s1 = Student.objects.filter(Q(student_sem= request.POST['tbssem']) & Q(student_course=c))
        b1 = Books.objects.filter(course_id=c)
        return render(request,'assignbook.html',{'data':s1,'book': b1, 'course': c1})
    return render(request,'assignbook.html',{'course':c1})


def abookdata_fun(request):
    i1 = Issue_Book()
    i1.std_name = Student.objects.get(student_name=request.POST['ddlsn'])
    i1.bk_name = Books.objects.get(book_name=request.POST['ddlbname'])
    i1.start_date = request.POST['tbsdate']
    i1.end_date = request.POST['tbedate']
    i1.save()
    return redirect('assignbook')


def issuebook_fun(request):
    i1 = Issue_Book.objects.all()
    return render(request,'issuebook.html',{'data':i1})


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


def deleteissuebk_fun(request,id):
    i1 = Issue_Book.objects.get(id=id)
    i1.delete()
    return redirect('issuebook')


def issuedbkdata_fun(request):
    s1 = Student.objects.get(student_name=A.x)
    i_d = s1.id
    b1 = Issue_Book.objects.filter(std_name = i_d)
    return render(request,'issuedbkdata.html',{'data': b1})


def logoutstd_fun(request):
    return redirect('login')


def stdprofile_fun(request):
    username = A.x
    s1 = Student.objects.get(student_name=username)
    if request.method == 'POST':
        return render(request, 'updateprofile.html', {'sd': s1})
    return render(request, 'stdprofile.html', {'data': username, 'sd': s1})


def updateprofile_fun(request):
    return render(request, 'updateprofile.html')


def profiledata_fun(request):
    s1 = Student.objects.get(student_name=A.x)
    s1.student_name = request.POST['tbuname']
    s1.student_phno = request.POST['tbphno']
    s1.student_sem = request.POST['tbsem']
    s1.student_password = request.POST['tbpass']
    s1.save()
    A.x = request.POST['tbuname']
    return redirect('stdprofile')