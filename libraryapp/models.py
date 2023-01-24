from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.course_name}'

class Books(models.Model):
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book_name}'

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_phno = models.BigIntegerField()
    student_sem = models.CharField(max_length=50)
    student_password = models.CharField(max_length=50)
    student_course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_name}'

class Issue_Book(models.Model):
    std_name = models.ForeignKey(Student,on_delete=models.CASCADE)
    bk_name = models.ForeignKey(Books,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class A:
    x = ''



