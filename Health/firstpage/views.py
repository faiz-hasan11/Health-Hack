from django.shortcuts import render
import joblib
import pandas as pd
import requests
import json
# Create your views here.
apiKey = "Bearer " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdSI6Imx4ZzphcGkiLCJzYyI6WyJrZzpyZWFkIiwiZXh0cmFjdGlvbjpyZWFkIl0sImFpIjoiYXBpOjA0NmM3ZWU4LTUwZDMtY2M5NS1kMjU3LThkNTYwMTY3MTQyMyIsInVpIjoidXNlcjpkMDM2Y2MwMS1lOWU0LTk5MWItYWU3My0zYjhhYTc0ZjZiOTAiLCJpYXQiOjE2MTEzNzIyOTF9.jp6hlCHeEbjBZRrrF-8jBRmGqWjX3JVlmstjDJvRRbU"

def home(request):
    return render(request,'home.html')

def diabetes(request):
    return render(request,'diabetes.html')

def predictdiabetes(request):
    reloadModel = joblib.load('./models/ModelDiabetes.pkl')
    if request.method == 'POST':
        temp={}
        arr = []
        temp['preg'] = request.POST.get('pregVal')
        temp['plasma'] = request.POST.get('plasmaVal')
        temp['bp'] = request.POST.get('bpVal')
        temp['skin'] = request.POST.get('skinVal')
        temp['insulin'] = request.POST.get('insulinVal')
        temp['bmi'] = request.POST.get('bmiVal')
        temp['pedigree'] = request.POST.get('pedigreeVal')
        temp['age'] = request.POST.get('ageVal')
        arr.append(float(temp['preg']))
        arr.append(float(temp['plasma']))
        arr.append(float(temp['bp']))
        arr.append(float(temp['skin']))
        arr.append(float(temp['insulin']))
        arr.append(float(temp['bmi']))
        arr.append(float(temp['pedigree']))
        arr.append(float(temp['age']))
        scoreval = reloadModel.predict([arr])
        return render(request,'preddiabetes.html',{'scoreval':scoreval})

def heart(request):
    return render(request,'heart.html')

def predictheart(request):
    reloadModel = joblib.load('./models/ModelForHeartDiseasePrediction2.pkl')
    if request.method == 'POST':
        temp={}
        arr = []
        temp['age'] = request.POST.get('ageVal')
        temp['sex'] = request.POST.get('genderVal')
        temp['cp'] = request.POST.get('chestpainVal')
        temp['trestbps'] = request.POST.get('trestbpsVal')
        temp['chol'] = request.POST.get('cholVal')
        temp['fbs'] = request.POST.get('fbsVal')
        temp['restecg'] = request.POST.get('restecgVal')
        temp['thalach'] = request.POST.get('thalachVal')
        temp['exang'] = request.POST.get('exangVal')
        temp['oldpeak'] = request.POST.get('oldpeakVal')
        temp['slope'] = request.POST.get('slopeVal')
        temp['ca'] = request.POST.get('caVal')
        temp['thal'] = request.POST.get('thalVal')
        arr.append(temp['age'])
        arr.append(temp['sex'])
        arr.append(temp['cp'])
        arr.append(temp['trestbps'])
        arr.append(temp['chol'])
        arr.append(temp['fbs'])
        arr.append(temp['restecg'])
        arr.append(temp['thalach'])
        arr.append(temp['exang'])
        arr.append(temp['oldpeak'])
        arr.append(temp['slope'])
        arr.append(temp['ca'])
        arr.append(temp['thal'])
    scoreval = reloadModel.predict([arr])
    return render(request,'predheart.html',{'scoreval':scoreval})


def liver(request):
    return render(request,'liver.html')

def predictliver(request):
    reloadModel = joblib.load('./models/ModelLiverDisease.pkl')
    if request.method == 'POST':
        temp={}
        arr = []
        temp['age'] = request.POST.get('ageVal')
        temp['TotalBillirubin'] = request.POST.get('TotalBillirubinVal')
        temp['ConjugatedBillirubin'] = request.POST.get('ConjugatedBillirubinVal')
        temp['ALP'] = request.POST.get('ALPVal')
        temp['ALT'] = request.POST.get('ALTVal')
        temp['AST'] = request.POST.get('ASTVal')
        temp['Proteins'] = request.POST.get('ProteinsVal')
        temp['Albumin'] = request.POST.get('AlbuminVal')
        temp['AG'] = request.POST.get('AGVal')
        arr.append(temp['age'])
        arr.append(temp['TotalBillirubin'])
        arr.append(temp['ConjugatedBillirubin'])
        arr.append(temp['ALP'])
        arr.append(temp['ALT'])
        arr.append(temp['AST'])
        arr.append(temp['Proteins'])
        arr.append(temp['Albumin'])
        arr.append(temp['AG'])
        scoreval = reloadModel.predict([arr])
        return render(request,'predliver.html',{'scoreval':scoreval[0]})

def cancer(request):
    return render(request,'cancer.html')

def predcancer(request):
    reloadModel = joblib.load('./models/ModelLungCancer2.pkl')
    if request.method == 'POST':
        temp={}
        arr = []
        temp['age'] = request.POST.get('ageVal')
        temp['smoke'] = request.POST.get('smokeVal')
        temp['area'] = request.POST.get('areaVal')
        temp['alc'] = request.POST.get('alcVal')
        arr.append(temp['age'])
        arr.append(temp['smoke'])
        arr.append(temp['area'])
        arr.append(temp['alc'])
        scoreval = int(reloadModel.predict([arr]))
        return render(request,'predcancer.html',{'scoreval':scoreval})



def kidney(request):
    return render(request,'kidney.html')

def predictkidney(request):
    reloadModel = joblib.load('./models/ModelKNNChronicKidneyDisease.pkl')
    if request.method == 'POST':
        temp={}
        arr = []
        temp['sg'] = request.POST.get('sgVal')
        temp['alb'] = request.POST.get('albVal')
        temp['pus'] = request.POST.get('pusVal')
        temp['hae'] = request.POST.get('haeVal')
        temp['pc'] = request.POST.get('pcVal')
        temp['hp'] = request.POST.get('hpVal')
        temp['dm'] = request.POST.get('dmVal')
        arr.append(temp['sg'])
        arr.append(temp['alb'])
        arr.append(temp['pus'])
        arr.append(temp['hae'])
        arr.append(temp['pc'])
        arr.append(temp['hp'])
        arr.append(temp['dm'])
        scoreval = int(reloadModel.predict([arr]))
        return render(request,'predkidney.html',{'scoreval':scoreval})

def enquire(request):
    return render(request,'enquire.html')

def enquiredata(request):
    if request.method == 'POST':
        temp={}
        temp['text'] = request.POST.get('textVal')
        error = False
        data = {}
        try:
            url = "https://api.lexigram.io/v1/extract/entities"
            r = requests.post(url, data=json.dumps({'text': temp['text']}),
            headers={'Authorization': apiKey, 'Content-Type': 'application/json'})
            response = json.loads(r.text)
            for match in response['matches']:
                for i in match['types']:
                    if i not in data:
                        data[i] = [match['label']]
                    else:
                        data[i].append(match['label'])
        except:
            error = True
        return render(request,'enquiredata.html',{'data':data,'error':error})

def bmi(request):
    return render(request,'bmi.html')

def predictbmi(request):
    if request.method == 'POST':
        temp={}
        arr = []
        temp['weight'] = request.POST.get('weightVal')
        temp['height'] = request.POST.get('heightVal')
        bmi = float(temp['weight']) / ( float(temp['height']) ** 2 )
        case = ""
        if bmi < 25:
            case = "Underweight"
        else:
            case = "Overweight"
        return render(request,'predbmi.html',{'case':case,'bmi':round(bmi, 2)})
