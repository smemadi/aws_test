from django.shortcuts import render
#from . import fake_model
from . import ml_predict
def home(requests):
    return render(requests,'index.html')

def result(requests):
    pclass=int(requests.GET.get("pclass",False))
    sex=int(requests.GET.get("sex",False))
    age=int(requests.GET.get("age",False))
    sibsp=int(requests.GET.get("sibsp",False))
    parch=int(requests.GET.get("parch",False))
    fare=int(requests.GET.get("fare",False))
    embarked=int(requests.GET.get("embarked",False))
    title=int(requests.GET.get("title",False))
    prediction=ml_predict.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    return render(requests,'result.html',{'prediction':prediction})
