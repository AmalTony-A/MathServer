from django.shortcuts import render

def bmi(request):
    context = {}
    context['bmi'] = "0"
    context['w'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        w = request.POST.get('Weight','0')
        h = request.POST.get('Height','0')
        print('request=', request)
        print('Weight=', w)
        print('Height=', h)
        a=float(w)
        b=float(h)
        bmi=a/(b*b)
        context['bmi']=bmi
        context['w']=w
        context['h']=h
        print('BMI=',bmi)
    return render(request, 'mathapp/math.html', context)

