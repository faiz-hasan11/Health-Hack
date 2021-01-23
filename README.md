# Health Hack
This website is a one stop solution for all your Health Needs. It provides 3 main features =>

* It has various machine learning models integrated with it which helps to predict whether one have kidney disease, heart disease, chronic kidney disease , diabetes or lung cancer. It has different forms which takes as input various health condition of the user and predicts the result on the basis of the information given. 
* It has the facility to take input about the situation of the patient and on that basis it suggests drugs and cause of such health condition.This is done with the help of Lexigram API. 
* It also calulates the BMI and tells whether one is underweight or overweight.

## Built With
* [Django](https://www.djangoproject.com/) - The Web Framework used for backend
* [Scikit Learn](https://scikit-learn.org/) - The Library used for building the model
* [Pandas](https://pandas.pydata.org/) - The Library used for handling data

## Installation
* After cloning or downloading this github repo on the local system. 
* Create a Virual Environment on the Desktop.
```bash
~/desktop/virtualenv VirtualEnvironmentName
```
* Now copy the repository inside your virtual environment.
* Activate the virtual environment.
```bash
~/desktop/VirtualEnvironmentName/Scripts/activate
```
* Move inside the virtual environment.
```bash
~/desktop/cd VirtualEnvironmentName
```
* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.
```bash
pip install -r requirements.txt
```
* Change directory to Health
```bash
~/desktop/VirtualEnvironmentName/Health
```
* Run the following command
```bash
python manage.py runserver
```
An IP address will be shown, copy it and run it on a web browser.

## Using the app
Internet connection is a must to run the app.

The app is now live at localhost.

## Screenshots
* Landing Page
![LandingPage](https://github.com/faiz-hasan11/Health-Hack/blob/master/Screenshots/landing.png)
* Input Page For Disease Prediction
![Input Page](https://github.com/faiz-hasan11/Health-Hack/blob/master/Screenshots/pred.png)
* Enquiry Page
![Enquiry Page](https://github.com/faiz-hasan11/Health-Hack/blob/master/Screenshots/enq.png)
* BMI Page
![BMI Page](https://github.com/faiz-hasan11/Health-Hack/blob/master/Screenshots/bmi.png)

