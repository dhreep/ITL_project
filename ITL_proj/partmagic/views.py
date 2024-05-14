from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Courses,Pubs
from .forms import PubsForm
from django.shortcuts import get_object_or_404

def delete_course(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    course.delete()
    return redirect('partmagic')

def delete_pub(request, pub_id):
    pub = get_object_or_404(Pubs, pk=pub_id)
    pub.delete()
    return redirect('partmagic')

def add_course(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        c_code = request.POST.get('c_code')
        cred = request.POST.get('cred')
        # Validate and save the course
        course = Courses(cname=cname, c_code=c_code, cred=cred)
        course.save()
        return redirect('partmagic')
    return HttpResponse('Method not allowed', status=405)

def add_pub(request):
    if request.method == 'POST':
        auth = request.POST.get('auth')
        pub_title = request.POST.get('pub_title')
        topic = request.POST.get('topic')
        pub_date = request.POST.get('pub_date')
        print(auth,pub_title,topic,pub_date)
        # Validate and save the publication
        pub = Pubs(auth=auth, pub_title=pub_title, topic=topic, pub_date=pub_date)
        pub.save()
        return redirect('partmagic')
    return HttpResponse('Method not allowed', status=405)

def partmagic(request):
    data = Courses.objects.all().values()
    data2 = Pubs.objects.all().values()
    context = {
        'Courses':data,
        'Pubs':data2,
    }
    template = loader.get_template('base1.html')
    return HttpResponse(template.render(context=context,request=request))
# Create your views here.
