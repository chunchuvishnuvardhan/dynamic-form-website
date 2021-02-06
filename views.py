
from django.contrib import messages
from django.shortcuts import render
from .models import Basic,Family
# Create your views here.

def index(request):
    return render(request,"index.html")

def submit(request):
    if request.method=="POST":
        # Name = request.POST['hname']
        mobile = request.POST['mobile']
        electricity = request.POST['electricity']
        Hno = request.POST['hno']
        village = request.POST['village']
        district = request.POST['district']
        mandal = request.POST['mandal']
        # info=request.POST['info']
        comm_info = Basic(mobile=mobile, electricity=electricity, hno=Hno,
                              district=district,village=village.capitalize(), mandal=mandal)
        comm_info.save()
        params = { 'usc': electricity}
        return render(request,'form.html',params)
    else:
        messages.error(request,'Something went wrong try again')
        return render(request,'index.html')


def form(request):
    if request.method=='POST':
        FName = request.POST['fname']
        usc=request.POST['usc']
        role=request.POST['role']
        gender=request.POST['gender']
        age=request.POST['age']
        qual=request.POST['qual']
        res=request.POST['res']
        occ=request.POST['occupation']
        f=Family.objects.filter(electricity=usc)
        params = {'usc': usc, 'f': f}
        if(res=='submit survey'):
            return render(request,"result.html")
        else:
            try:
                family_info=Family(name=FName, electricity=usc, role=role, gender=gender, age=age, qual=qual,occupation=occ)
                family_info.save()
                return render(request, "form.html",params)
            except:
                return render(request, "form.html",params)

    return render(request,'form.html')
def result(request):
    # b=Basic.objects.values_list('electricity', flat=True).filter(village='akkapur')
    # f = Family.objects.filter(electricity__in=list(b))
    # print(f)
    # m1=Basic.objects.values_list('electricity', flat=True).filter(mandal='Machareddy')
    # m2= Family.objects.filter(electricity__in=list(m1))
    # # print(m2)
    # d1 = Basic.objects.values_list('electricity', flat=True).filter(district='Kamareddy')
    # d2 = Family.objects.filter(electricity__in=list(d1))
    # # print(d2)

        # print(i,len(list(f)))

        # print(i, len(list(f)))
    b=Family.objects.all()
    total=len(list(b))
    if request.method=='POST':
        if(request.POST['distvise']=='get'):
            dist = Basic.objects.values_list('district', flat=True).distinct()
            ldist = {}
            for i in list(dist):
                b = Basic.objects.values_list('electricity', flat=True).filter(district=i)
                f = Family.objects.filter(electricity__in=list(b))
                ldist.update({i: len(list(f))})
            return render(request, "result.html", {'ldist': ldist,'total':total})
    return render(request,"result.html",{'total':total})
def exit(request):
    return render(request,"exit.html")

def mandalwise(request):
    b=Family.objects.all()
    total=len(list(b))
    if(request.method=='POST'):
        if (request.POST['mandalwise'] == 'submit'):
            dist = request.POST['district']
            dman = Basic.objects.values_list('mandal', flat=True).distinct().filter(district=dist.capitalize())
            lman = {}
            for i in list(dman):
                b = Basic.objects.values_list('electricity', flat=True).filter(mandal=i)
                f = Family.objects.filter(electricity__in=list(b))
                lman.update({i: len(list(f))})
            return render(request, "result.html", {'ldist': lman, 'total':total})
    return render(request,"result.html",{'total':total})

def villagewise(request):
    b=Family.objects.all()
    total=len(list(b))
    if(request.method=='POST'):
        mandal = request.POST['mandal']
        if (request.POST['villagewise']):
            dvill = Basic.objects.values_list('village', flat=True).distinct().filter(mandal=mandal.capitalize())
            lvill = {}
            for i in list(dvill):
                b = Basic.objects.values_list('electricity', flat=True).filter(village=i)
                f = Family.objects.filter(electricity__in=list(b))
                lvill.update({i: len(list(f))})
            return render(request, "result.html", {'ldist': lvill,'total':total})
    return render(request,"result.html",{'total':total})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


