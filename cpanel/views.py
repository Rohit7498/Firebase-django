from django.shortcuts import render
from django.contrib import auth
import pyrebase

config = {

    'apiKey': "AIzaSyCWaHZ66-gfABcfNowc6Jo-ynwkkp3skWM",
    'authDomain': "cpanel-cc891.firebaseapp.com",
    'databaseURL': "https://cpanel-cc891.firebaseio.com",
    'projectId': "cpanel-cc891",
    'storageBucket': "cpanel-cc891.appspot.com",
    'messagingSenderId': "729933585427"
  }

firebase = pyrebase.initialize_app(config)

database = firebase.database()
authe = firebase.auth()


def signIn(request):

    return render(request, 'signIn.html')

def postSignIn(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = 'inavlid credentials'
        return render(request, 'signIn.html', {"messg":message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    idtoken = request.session['uid']
    print("id" +" " + ' : ' + str(idtoken))
    a = authe.get_account_info(idtoken)
    print(a)
    a = a['users']
    a = a[0]
    a = a['localId']

    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request, 'welcome.html', {"email":name})


def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')

def signUp(request):

    return render(request, 'signUp.html')

def postSignUp(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    try:
        user = authe.create_user_with_email_and_password(email, passw)
    except:
        message = 'unable to create account try again'
        return render(request, 'signUp.html', {"messg":message})

    uid = user['localId']

    data = {'name': name, "status":"1"}
    mssg = "you may now sign in"
    database.child("users").child(uid).child("details").set(data)
    return render(request, 'signIn.html')

def create(request):

    return render(request, 'create.html')

def post_create(request):

    import time
    import datetime
    from datetime import datetime, timezone
    import pytz

    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))

    work = request.POST.get('work')
    progress = request.POST.get('progress')
    url = request.POST.get('url')

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']


    data = {
        'work': work,
        'progress': progress,
        'url' : url
    }

    database.child('users').child(a).child('reports').child(millis).set(data)
    name = database.child('users').child(a).child('details').child('name').get().val()

    return render(request, 'welcome.html', {"email": name})

def check(request):

    import time
    import datetime
    from datetime import timezone

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    timeStamps = database.child('users').child(a).child('reports').shallow().get().val()
    lis_time = []

    for time in timeStamps:
        lis_time.append(time)

    lis_time.sort(reverse=True)

    work = []

    for time in lis_time:
        work.append(database.child('users').child(a).child('reports').child(time).child('work').get().val())

    date = []
    for i in lis_time:
        i = float(i)
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date.append(dat)



    comb_lis = zip(lis_time, date, work)

    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request, 'check.html', {'comb_lis':comb_lis, 'email':name})

def post_check(request):
    import datetime

    time = request.GET.get('z')
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    work = database.child('users').child(a).child('reports').child(time).child('work').get().val()
    progress = database.child('users').child(a).child('reports').child(time).child('progress').get().val()
    img_url = database.child('users').child(a).child('reports').child(time).child('url').get().val()

    i = float(time)
    dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')

    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request, 'post_check.html', {'w':work, 'p':progress, 'd':dat, 'email':name, 'i':img_url})
