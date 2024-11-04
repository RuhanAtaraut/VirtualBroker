from django.shortcuts import render, redirect
from .models import Room_Detail,Mess_Detail,Register
from django.contrib.auth import authenticate, login as login_proccess
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import AddRooms, AddMess, Room_cities, Room_Areas, Mess_cities, Mess_Areas, Otp_user, Copy_User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from cryptography.fernet import Fernet
# Create your views here.


#def login(request):
    #return render(request, "login.html")

#def register(request):
    #return render(request, "register.html")

def addrooms(request):
    if request.method == 'GET':
        return render(request, 'add_rooms.html')

    if request.method == 'POST':
        category = request.POST['category']
        rtype = request.POST['rtype']
        city = request.POST['city'].title()
        area = request.POST['area'].title()
        address = request.POST['address']
        price = request.POST['price']

        print('*******', city, area)

        result = Room_cities.objects.filter(room_city_name=city)
        if result.exists():
            print('City is already there')
        else:
            addcity = Room_cities(room_city_name=city)
            addcity.save()

        result = Room_cities.objects.filter(room_city_name=city)

        for i in result:
            room_cities_id = i.room_cities_id

        result = Room_Areas.objects.filter(room_area_name=area)
        if result.exists():
            print('area is already there')
        else:
            room_cities_id = Room_cities.objects.get(room_cities_id=room_cities_id)
            addarea = Room_Areas(rc_id=room_cities_id, room_area_name=area)
            addarea.save()

        result = Room_Areas.objects.filter(room_area_name=area)

        for i in result:
            room_area_id = i.room_area_id
        room_area_id = Room_Areas.objects.get(room_area_id=room_area_id)

        user_id = request.user.id
        copy_user_id = request.user.id
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', user_id, type(user_id))
        user_id = User.objects.get(id=user_id)
        copy_user_id = Copy_User.objects.get(copy_user_id=copy_user_id)

        addroomdetails = AddRooms(u_id=user_id, c_u_id=copy_user_id, ra_id=room_area_id, category=category, rtype=rtype, address=address,
                                  price=price)
        addroomdetails.save()


        result = Room_Areas.objects.filter(room_area_name=area)

        for i in result:
            room_area_id = i.room_area_id

        print(User.id)

        # sql="select * from calc_AddRooms where city='%s' and %s "%(selected_city,sub)

        # addrooms = AddRooms(category=category, rtype=rtype, address=address, price=price)
        # addrooms.save()
        er_massege = None
        er_massege = " your room added successfully"
        return render(request, 'user_home.html')

        # print(category, rtype, city, area, address, price, '\n', type(category), type(rtype))
        # return render(request, 'about.html')

def addmess(request):
    if request.method == 'GET':
        return render(request, 'add_mess.html')

    if request.method == 'POST':
        name = request.POST['name']
        messtype = request.POST['messtype']
        city = request.POST['city'].title()
        area = request.POST['area'].title()
        address = request.POST['address']
        price = request.POST['price']

        print('#######', city, area)

        result = Mess_cities.objects.filter(mess_city_name=city)
        if result.exists():
            print('City is already there')
        else:
            addcity = Mess_cities(mess_city_name=city)
            addcity.save()

        result = Mess_cities.objects.filter(mess_city_name=city)

        for i in result:
            mess_cities_id = i.mess_cities_id

        result = Mess_Areas.objects.filter(mess_area_name=area)
        if result.exists():
            print('area is already there')
        else:
            mess_cities_id = Mess_cities.objects.get(mess_cities_id=mess_cities_id)
            addarea = Mess_Areas(mc_id=mess_cities_id, mess_area_name=area)
            addarea.save()





        result = Mess_Areas.objects.filter(mess_area_name=area)

        for i in result:
            mess_area_id = i.mess_area_id
        mess_area_id = Mess_Areas.objects.get(mess_area_id=mess_area_id)

        user_id = request.user.id
        copy_user_id = request.user.id
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', user_id, type(user_id))
        user_id = User.objects.get(id=user_id)
        copy_user_id = Copy_User.objects.get(copy_user_id=copy_user_id)

        addmessdetails = AddMess(u_id=user_id, c_u_id=copy_user_id, ma_id=mess_area_id, name=name, messtype=messtype, address=address,
                                 price=price)
        addmessdetails.save()


        return render(request, 'user_home.html')



def login(request):
    return render(request,'login.html')

def log(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        uemail = request.POST.get('uemail')
        password = request.POST.get('password')

        user = check_user(uemail)
        if user:

            eml = User.objects.get(username=uemail)
            if eml.username == uemail and (check_password(password, eml.password)):
                user = authenticate(username=eml, password=password)
                login_proccess(request, user)
                print(uemail, password, type(uemail), type(password), user.id)
                return render(request, 'user_home.html')
            else:
                er_massege = "invalid email OR Password"
                return render(request, 'login.html', {'error': er_massege})
        else:
            er_massege = "You are not registered user"
            return render(request, 'login.html', {'error': er_massege})
        # print(uemail, password, type(uemail), type(password), user.id)

        # return render(request, 'signup.html')

def mail_send(uemail, resend):
    if resend == False:
        otp_user = Otp_user.objects.all()
        for x in otp_user:
            if x.otp_uemail == uemail:
                Otp_user.objects.filter(otp_uemail=uemail).delete()
        import random
        number = random.randint(1111, 9999)
        msg = 'Your OTP123 : ' + str(number)
        print('mail is sent')
        msg_plain = render_to_string('mail.txt')
        send_mail("please confirm yourself", msg_plain, settings.EMAIL_HOST_USER, [uemail], html_message=msg)
        return number

    if resend ==True:
        import random
        number = random.randint(1111, 9999)
        msg = 'Your OTP : ' + str(number)
        print('mail is sent')
        msg_plain = render_to_string('mail.txt')
        send_mail("please confirm yourself", msg_plain, settings.EMAIL_HOST_USER, [uemail], html_message=msg)
        return number

def check_user(em):
    try:
        User.objects.get(username=em)
        return True
    except:
        return False


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        uemail = request.POST['uemail']
        contactnumber = request.POST['contactnumber']
        city = request.POST['city']
        address = request.POST['address']
        password = request.POST['password']
        cpassword=request.POST['cpassword']
       
        er_massege = None
        if password != cpassword:
            er_massege="Password doesn't match"


        
        user = User.objects.all()
        for x in user:
            if x.username == uemail:
                er_massege = 'Email address Already Registered..'

        if not er_massege:
            resend = False
            otp = mail_send(uemail, resend)
            add_otp_user = Otp_user(otp_firstname=firstname, otp_lastname=lastname, otp_uemail=uemail,
                                    otp_contactnumber=contactnumber, otp_city=city, otp_address=address,
                                    otp_password=password, otp=otp)
            add_otp_user.save()




            # note :-> here first_neame = em and em = fn
            '''
            myuser = User.objects.create_user(uemail, firstname, password)
            myuser.last_name = lastname
            myuser.phone = contactnumber
            myuser.city = city
            myuser.address = address
            myuser.otp = otp
    
            myuser.save()
            er_massege = "Acount created successfully"
            '''
            data = {
                'firstname': firstname,
                'lastname': lastname,
                'uemail' : uemail
            }
            return render(request, 'otp.html', data)

        print(firstname, lastname, uemail, contactnumber, city, address, password)
        data1 = {
            'error': er_massege,
        }
        return render(request, 'signup.html', data1)

def userlogout(request):
    logout(request)
    return redirect('index')

def otp_check(request):
    if request.method == 'POST':
        check = request.POST.get('check')
        resend = request.POST.get('resend')
        uemail = request.POST.get('uemail')
        user_entered_otp = request.POST.get('otp')
        otp_table_otp = ""
        if check:
            print('user mail ', uemail)

            otp_user = Otp_user.objects.filter(otp_uemail=uemail)
            for i in otp_user:
                otp_table_otp = i.otp
                otp_firstname = i.otp_firstname
                otp_lastname = i.otp_lastname
                otp_uemail = i.otp_uemail
                otp_contactnumber = i.otp_contactnumber
                otp_city = i.otp_city
                otp_address= i.otp_address
                otp_password = i.otp_password

            print('user entered otp', user_entered_otp, type(user_entered_otp))
            print('otp table otp', otp_table_otp, type(otp_table_otp))

            if user_entered_otp == otp_table_otp:
                print('otp is correct')
                myuser = User.objects.create_user(uemail, otp_firstname, otp_password)
                myuser.last_name = otp_lastname
                myuser.save()

                # result = Room_cities.objects.filter(room_city_name=city)
                res = User.objects.filter(username=uemail)
                for i in res:
                    user_id = int(i.id)
                add_copy_user = Copy_User(copy_user_id=user_id, copy_firstname=otp_firstname, copy_lastname=otp_lastname,
                                        copy_uemail=otp_uemail, copy_contactnumber=otp_contactnumber, copy_city=otp_city,
                                        copy_address=otp_address)
                add_copy_user.save()

                data = {
                    'succ': "Sign Up successful"
                }
                return redirect('log')
            else:
                print('otp is not correct')
                data = {
                    'uemail': uemail,
                    'er_massege': "OTP is not correct"
                }
                return render(request, 'otp.html', data)

        if resend:
            resendotp = True
            otp = mail_send(uemail, resendotp)
            Otp_user.objects.filter(otp_uemail=uemail).update(otp=otp)
            data = {
                'uemail': uemail,
            }
            return render(request, 'otp.html', data)

def register(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phonenumber = request.POST['Phone_number']
        password = request.POST['Password']
        cpassword = request.POST['Confirm_Password']

        ins=Register(fname=fname,lname=lname,email=email,phonenumber=phonenumber,password=password,cpassword=cpassword)
        
        ins.save()

        print("The data has been written to DB")
    return render(request, 'login.html')

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def fetch1(request):
    if request.method == 'GET':
        cities = Mess_cities.objects.all()
        data = {
            'cities': cities
        }
        return render(request, 'fetch1.html', data)

    if request.method == 'POST':
        selected_city_id = request.POST['programming']
        selected_area_id = request.POST['courses']
        selected_type = request.POST['type']
        price_range = request.POST['price']
        cities = Mess_cities.objects.all()

        if (price_range == "0000-1000"):
            sub = "a.price>0 and a.price<=1000"
            minp = 0
            maxp = 1000

        elif (price_range == "1001-2000"):
            sub = "a.price>1000 and a.price<=2000"
            minp = 1001
            maxp = 2000

        elif (price_range == "2001-3000"):
            sub = "a.price>2000 and a.price<=3000"
            minp = 2001
            maxp = 3000

        elif (price_range == "3001-4000"):
            sub = "a.price>3000 and a.price<=4000"
            minp = 3001
            maxp = 4000

        elif (price_range == "4001-5000"):
            sub = "a.price>4000 and a.price<=5000"
            minp = 4001
            maxp = 5000

        else:
            sub = "a.price>5000"
            minp = 5001
            maxp = 100000

        print(selected_city_id, selected_area_id, selected_type, price_range, minp, maxp)
        result = my_custom_sql1(selected_area_id, selected_city_id, selected_type, price_range, minp, maxp)
        print('}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}', result)
        if result:
            data = {
                'cities': cities,
                'mess_details': result,
            }
            return render(request, 'fetch1.html', data)
        else:
            cities = Mess_cities.objects.all()
            er_massege = "Data Not Found"
            return render(request, 'fetch1.html', {'error': er_massege, 'cities': cities})

def my_custom_sql1(selected_area_id, selected_city_id, selected_type, price_range, minp, maxp):
    from django.db import connection
    minp = str(minp)
    maxp = str(maxp)
    print(type(minp), '================', type(maxp))
    with connection.cursor() as cursor:
        # cursor.execute("SELECT * FROM calc_AddRooms as R calc_Room_Areas RA where R.category='flat'")
        # cursor.execute("SELECT u.username, rc.room_city_name, a.address, a.price FROM Users u, Room_cities rc, AddRooms a, Room_Areas ra WHERE u.id=a.u_id AND ra.rc_id=rc.room_cities_id AND a.ra_id=ra.room_area_id")

        cursor.execute("SELECT cp.copy_firstname, cp.copy_lastname, mc.mess_city_name, cp.copy_contactnumber, a.address, a.price FROM calc_Copy_User cp, calc_Mess_cities mc, calc_AddMess a, calc_Mess_Areas ma WHERE cp.copy_user_id=a.c_u_id_id AND ma.mc_id_id=mc.mess_cities_id AND a.ma_id_id=ma.mess_area_id AND ma.mess_area_id = %s AND mc.mess_cities_id =%s AND a.messtype='%s' AND a.price >= %s AND a.price<=%s"%(selected_area_id, selected_city_id, selected_type, minp, maxp))
        #                 [selected_area_id, selected_city_id, selected_type, minp, maxp])'
        # sql="SELECT a.address, a.rtype FROM calc_AddRooms a WHERE a.rtype='%s'"%(selected_type)
        # print(sql)
        # cursor.execute("SELECT a.address, a.rtype FROM calc_AddRooms a WHERE a.rtype='%s'"%(selected_type))

        row = cursor.fetchall()
        # print(row)
    return row

def fetch(request):
    if request.method == 'GET':
        cities = Room_cities.objects.all()
        data = {
            'cities': cities
        }
        return render(request, 'fetch.html', data)

    if request.method == 'POST':
        selected_city_id = request.POST['programming']
        selected_area_id = request.POST['courses']
        selected_type = request.POST['type']
        price_range = request.POST['price']

        if (price_range == "0000-1000"):
            sub = "a.price>0 and a.price<=1000"
            minp = 0
            maxp = 1000

        elif (price_range == "1001-2000"):
            sub = "a.price>1000 and a.price<=2000"
            minp = 1001
            maxp = 2000

        elif (price_range == "2001-3000"):
            sub = "a.price>2000 and a.price<=3000"
            minp = 2001
            maxp = 3000

        elif (price_range == "3001-4000"):
            sub = "a.price>3000 and a.price<=4000"
            minp = 3001
            maxp = 4000

        elif (price_range == "4001-5000"):
            sub = "a.price>4000 and a.price<=5000"
            minp = 4001
            maxp = 5000

        else:
            sub = "a.price>5000"
            minp = 5001
            maxp = 100000

        print(selected_city_id, selected_area_id, selected_type, price_range, minp, maxp)

        # rc = Room_cities.objects.get(room_cities_id=selected_city_id)

        # ra = Room_Areas.objects.get(rc_id=rc)
        # print('&&&&&&&&&', rc, ra)

        # sql ="SELECT cp.copy_firstname, cp.copy_lastname, rc.room_city_name, cp.copy_contactnumber, a.address, a.price FROM calc_Copy_User cp, calc_Room_cities rc, calc_AddRooms a, calc_Room_Areas ra WHERE cp.copy_user_id=a.c_u_id_id AND ra.rc_id_id=rc.room_cities_id AND a.ra_id_id=ra.room_area_id AND ra.room_area_id = %s AND rc.room_cities_id =%s AND a.rtype='%s' AND '%s'"%(selected_area_id, selected_city_id, selected_type, sub)
        # sql = "select room_id, ra_id from calc_AddRooms"
        # result = AddRooms.objects.raw(sql)

        # area_cities = Room_Areas.objects.filter(rc_id=selected_city_id).only('room_area_id').all()
        # print('SELECT CITIES', area_cities)
        result = my_custom_sql(selected_area_id, selected_city_id, selected_type, price_range, minp, maxp)
        # details = AddRooms.objects.value('room_id').filter(room_area_id__in=area_cities)
        # print('SELECTED DETAILS --- ', details)
        # result = AddRooms.objects.filter(ra_id=selected_area_id)
        # result = AddRooms.objects.filter(ra_id=selected_area_id, )
        print('}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}', result)

        # for x in result:
        #     print(x.room_id, '--', x.ra_id.room_area_id)
        # print(type(result[0]))
        cities = Room_cities.objects.all()
        if result:
            data = {
                'room_details': result,
                'cities': cities
            }
            return render(request, 'fetch.html', data)
        else:
            cities = Room_cities.objects.all()
            er_massege = "Data Not Found"
            return render(request, 'fetch.html', {'error': er_massege, 'cities': cities})

def my_custom_sql(selected_area_id, selected_city_id, selected_type, price_range, minp, maxp):
    from django.db import connection
    minp = str(minp)
    maxp = str(maxp)
    print(type(minp), '================', type(maxp))
    with connection.cursor() as cursor:
        # cursor.execute("SELECT * FROM calc_AddRooms as R calc_Room_Areas RA where R.category='flat'")
        # cursor.execute("SELECT u.username, rc.room_city_name, a.address, a.price FROM Users u, Room_cities rc, AddRooms a, Room_Areas ra WHERE u.id=a.u_id AND ra.rc_id=rc.room_cities_id AND a.ra_id=ra.room_area_id")

        cursor.execute("SELECT cp.copy_firstname, cp.copy_lastname, rc.room_city_name, cp.copy_contactnumber, a.address, a.price FROM calc_Copy_User cp, calc_Room_cities rc, calc_AddRooms a, calc_Room_Areas ra WHERE cp.copy_user_id=a.c_u_id_id AND ra.rc_id_id=rc.room_cities_id AND a.ra_id_id=ra.room_area_id AND ra.room_area_id = %s AND rc.room_cities_id =%s AND a.rtype='%s' AND a.price >= %s AND a.price<=%s"%(selected_area_id, selected_city_id, selected_type, minp, maxp))
        #                 [selected_area_id, selected_city_id, selected_type, minp, maxp])'
        # sql="SELECT a.address, a.rtype FROM calc_AddRooms a WHERE a.rtype='%s'"%(selected_type)
        # print(sql)
        # cursor.execute("SELECT a.address, a.rtype FROM calc_AddRooms a WHERE a.rtype='%s'"%(selected_type))

        row = cursor.fetchall()
        # print(row)
    return row

def load_courses(request):
    programming_id = request.GET.get('programming')
    courses = Room_Areas.objects.filter(rc_id=programming_id)
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})


def load_courses1(request):
    programming_id = request.GET.get('programming')
    courses = Mess_Areas.objects.filter(mc_id=programming_id)
    return render(request, 'courses_dropdown_list_options1.html', {'courses': courses})


def load_areas(request):
    area_id = request.GET.get('courses')
    room_details = AddRooms.objects.filter(ra_id=area_id)
    return render(request, 'courses_dropdown_list_options1.html', {'room_details': room_details})



def submit(request):
    if request.method == "POST":
        selected_city = request.POST['programming']
        selected_area = request.POST['courses']
        selected_type = request.POST['type']
        price_range = request.POST['price']

        print(selected_city, selected_area, selected_type, price_range)
        return redirect('index')
        #print(price_range)
        if (price_range == "0000 - 1000"):
            sub="price>0 and price<=1000"

        elif(price_range == "1001 - 2000"):
            sub="price>1000 and price<=2000"

        elif (price_range == "2001 - 3000"):
            sub = "price>2000 and price<=3000"

        elif (price_range == "3001 - 4000"):
            sub = "price>3000 and price<=4000"

        elif (price_range == "4001 - 5000"):
            sub = "price>4000 and price<=5000"

        else:
             sub = "price>5000"

        sql="select * from AddRooms where ra_id='%s' and %s "%(selected_city,sub)
        #sql1='"select * from Room_Detail where city="+selected_city+" and "+sub'
         #   sql = "select * from room_details where city='%s' and price>=500 and price<1000" % (filter2)
        result=AddRooms.objects.raw(sql)
        myres=AddRooms.objects.filter(city=selected_city, price__range=(minp, maxp))
        print(myres)
        for res in myres:
            
            print(res.room_id)
            print(res.category)
            print(res.rtype)
            print(res.city)
            print(res.area)
            print(res.address)
            print(res.price)

        # return render(request, 'submit.html',{'result':result})

def submit1(request):
    if request.method == "POST":
        selected_city = request.POST['cities']
        price_range = request.POST['mess_price']

        print('PRICE RANGE--> ', type(price_range))

        #print(price_range)
        if (price_range == "0000 - 1000"):
            sub="price>0 and price<=1000"
        elif(price_range == "1001 - 2000"):
            sub="price>1000 and price<=2000"
        elif (price_range == "2001 - 3000"):
            sub = "price>2000 and price<=3000"
        elif (price_range == "3001 - 4000"):
            sub = "price>3000 and price<=4000"
        # else:
        #     sub = "mess_price>4000"

        sql="select * from calc_AddMess where city='%s' and %s "%(selected_city,sub)
        #sql1='"select * from Room_Detail where city="+selected_city+" and "+sub'
         #   sql = "select * from room_details where city='%s' and price>=500 and price<1000" % (filter2)
        result=AddMess.objects.raw(sql)
        print(result)
        for res in result:
            
            print(res.name)
            print(res.messtype)
            print(res.city)
            print(res.area)
            print(res.price)

        return render(request, 'submit1.html',{'result':result})
    #     return redirect('index')

def fill(request):
    if request.method=="POST":
        name=request.POST['name']
        city = request.POST['city']
        address = request.POST['address']
        contact = request.POST['contact']
        price = request.POST['price']
        name=request.POST['name']
        city = request.POST['city']
        address = request.POST['address']
        contact = request.POST['contact']
        mess_price = request.POST['mess_price']

        ins=Room_Detail(name=name,city=city,address=address,contact=contact,price=price)
        ins=Mess_Detail(name=name,city=city,address=address,contact=contact,mess_price=mess_price)
        ins.save()

        print("The data has been written to DB")
    return render(request, 'fill.html')
def fill1(request):
    if request.method=="POST":
        name=request.POST['name']
        city = request.POST['city']
        address = request.POST['address']
        contact = request.POST['contact']
        price = request.POST['price']

        ins=Room_Detail(name=name,city=city,address=address,contact=contact,price=price)
        
        ins.save()

        print("The data has been written to DB")
    return render(request, 'fill1.html')

def fill2(request):
    if request.method=="POST":
        name=request.POST['name']
        city = request.POST['city']
        address = request.POST['address']
        contact = request.POST['contact']
        mess_price = request.POST['mess_price']

        ins=Mess_Detail(name=name,city=city,address=address,contact=contact,mess_price=mess_price)
        ins.save()

        print("The data has been written to DB")
    return render(request, 'fill2.html')

