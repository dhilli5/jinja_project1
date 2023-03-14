from django.shortcuts import render

# Create your views here.


def condition(request):
    d={'a':200,'b':400,'c':700}
    return render(request,'condition.html',d)
def condition1(request):
     d={'a':200,'b':400,'c':700}
     return render(request,'condition1.html',d)