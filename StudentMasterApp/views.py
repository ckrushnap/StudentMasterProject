from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from StudentMasterApp.models import Student, Task, Master


def home_fun(request):
    return render(request, 'index.html')


def std_login_fun(request):
    return render(request, 'ST_login.html')


def std_register_fun(request):
    return render(request, 'ST_register.html')


def mst_login_fun(request):
    return render(request, 'MST_login.html')


def mst_register_fun(request):
    return render(request, 'MST_register.html')


def task_view_fun(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'data': tasks})


def task_assign_fun(request):
    students = Student.objects.all()
    return render(request, 'assign_task.html', {'data': students})


def read_student_login_fun(request):
    user_name = request.POST['txtUserName']
    user_password = request.POST['txtPassword']
    if Student.objects.filter(Q(UserName=user_name) & Q(Password=user_password)).exists():
        return render(request, 'student_home.html')
    else:
        return render(request, 'ST_login.html')


def read_master_login_fun(request):
    user_name = request.POST['txtUserName']
    user_password = request.POST['txtPassword']
    if Master.objects.filter(Q(UserName=user_name) & Q(Password=user_password)).exists():
        return render(request, 'master_home.html')
    else:
        return render(request, 'MST_login.html')


def read_student_register_fun(request):
    if request.method == 'POST':
        username = request.POST['txtUserName']
        name = request.POST['txtName']
        email = request.POST['txtEmail']
        password = request.POST['txtPassword']
        if Student.objects.filter(Q(UserName=username) | Q(Password=password)).exists():
            return render(request, 'ST_register.html')
        else:
            s1 = Student()
            s1.Name = name
            s1.UserName = username
            s1.UserEmail = email
            s1.Password = password
            s1.save()
            return render(request, 'ST_login.html', {'data': ''})


def read_master_register_fun(request):
    if request.method == 'POST':
        username = request.POST['txtUserName']
        name = request.POST['txtName']
        email = request.POST['txtEmail']
        password = request.POST['txtPassword']
        if Master.objects.filter(Q(UserName=username) | Q(Password=password)).exists():
            return render(request, 'ST_register.html')
        else:
            m1 = Master()
            m1.Name = name
            m1.UserName = username
            m1.UserEmail = email
            m1.Password = password
            m1.save()
            return render(request, 'MST_login.html', {'data': ''})


def create_task_fun(request):
    t1 = Task()
    t1.Left = request.POST['left']
    t1.Right = request.POST['right']
    t1.Operator = request.POST['operators']
    t1.Student_id = Student.objects.get(Name=request.POST['ddlstudent'])
    t1.save()
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'data': tasks})


def logout_fun(request):
    return redirect('home')


def solve_fun(request, id):
    t1 = Task.objects.get(id=id)
    left = t1.Left
    left = globals()[left]
    right = t1.Right
    right = globals()[right]
    op = t1.Operator
    op = globals()[op]
    print(left, right,op)
    res = left(op(right()))
    t1.Complete = True
    return render(request, 'task_list.html', {'sol': {res},
                                              'data': Task.objects.all()
                                              })

def make_num(num, func):
    if func == None:
        return num
    else:
        return func(num)


def zero(func=None):
    return make_num(0, func)


def one(func=None):
    return make_num(1, func)


def two(func=None):
    return make_num(2, func)


def three(func=None):
    return make_num(3, func)


def four(func=None):
    return make_num(4, func)


def five(func=None):
    return make_num(5, func)


def six(func=None):
    return make_num(6, func)


def seven(func=None):
    return make_num(7, func)


def eight(func=None):
    return make_num(8, func)


def nine(func=None):
    return make_num(9, func)


def times(right):
    sum = lambda left: left * right
    return sum


def plus(right):
    sum = lambda left: left + right
    return sum


def minus(right):
    sum = lambda left: left - right
    return sum


def divided_by(right):
    sum = lambda left: left // right
    return sum

