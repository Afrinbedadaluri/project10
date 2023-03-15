from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10,'b':30,'c':20}
    return render(request,'conditions.html',context=d)


def loops(request):
    d={'name':'afrin'}
    return render(request,'loops.html',context=d)
