# Ex.05 Design a Website for Server Side Processing
## Date:01.10.2025

## AIM:
 To design a website to calculate the Body Mass Index (BMI) in the server side. 


## FORMULA:
BMI = W / H<sup>2</sup>
<br> BMI → Body Mass Index (in kg/m<sup>2</sup>)
<br> H → Height 
<br> W → Weight

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html>
<head>
<title>Body Mass Index</title>
<style type="text/css">
body {
    background-color:rgb(27, 99, 31);
}
.edge {
    width:1440px;
    margin-left:auto;
    margin-right:auto;
    padding-top: 100px;  
    padding-left:300px;
}
.box {
    display:block;
    border:Thick dashed lime;
    width:900px;
    min-height:400px;
    font-size: 25px; 
    background-color:rgb(12, 0, 104);
    text-align:center;  
    padding-top: 20px;
}
.formelt { 
    color:rgb(255, 255, 0); 
    text-align: center; 
    margin-top: 10px; 
    margin-bottom: 10px;
}
h1 {
    color:yellow;
    margin:0;
    padding:0;
}
h2 {
    color:rgb(255,0,179);
    margin-top: 10px;
    margin-bottom: 20px;
}
</style>
</head>
<body>
    <div class="edge">
        <div class="box">
           
            <h1>Amal Tony Charles (25016419)</h1>
          
            <h2>Body Mass Index</h2>

            <form method="POST">
            {% csrf_token %}
            <div class="formelt">
                Weight: <input type="number" step="any" name="Weight" value="{{w}}">(in kg)<br/>
            </div>
            <div class="formelt">
                Height: <input type="number" step="any" name="Height" value="{{h}}">(in m)<br/>
            </div>
            <div class="formelt">
                <input type="submit" value="calculate"></input><br/>
            </div>
            <div class="formelt">
                BMI: <input type="text" name="BMI" value="{{bmi}}"></input>kg/m<sup>2</sup><br/>
            </div>
            </form>
        </div>
    </div>
</body>
</html>



views.py

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
        a=int(w)
        b=int(h)
        bmi=a/(b*b)
        context['bmi']=bmi
        context['w']=w
        context['h']=h
        print('BMI=',bmi)
    return render(request, 'mathapp/math.html', context)

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns=[
    path('admin/', admin.site.urls),
    path('bodymassindex/', views.bmi, name="bodymassindex"),
    path('', views.bmi, name="bodymassindexroot")
]


```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-10-02 162634.png>)

## HOMEPAGE:
![alt text](<Screenshot 2025-10-02 162528.png>)

## RESULT:
The program for performing server side processing is completed successfully.
