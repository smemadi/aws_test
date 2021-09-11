import pandas as pd
import numpy as np

df=pd.read_csv("train.csv")
df_test=pd.read_csv("test.csv")
def get_title(name):
    if "." in name:
        return name.split(",")[1].split(".")[0].strip()
    else:
        return "No title"
titles=set([x for x in df.Name.map(lambda x: get_title(x))])
def shorter_titles(x):
    title=x["Title"]
    if title in ["Capt","Col","Major"]:
        return "Officer"
    elif title in ["Jonkheer","Don","the Countess","Dona","Lady","Sir"]:
        return "Royalty"
    elif title=="Mme":
        return "Mrs"
    elif title in ["Mlle","Ms"]:
        return "Miss"
    else:
        return title
df["Title"]=df["Name"].map(lambda x: get_title(x))
df["Title"]=df.apply(shorter_titles,axis=1)
df.loc[df["Age"].isnull(),"Age"]=df["Age"].median()
df["Age"].fillna(df["Age"].median(),inplace=True)
df["Embarked"].fillna("S",inplace=True)
del df["Cabin"]
df.drop("Name",axis=1,inplace=True)
df.Sex.replace(("male","female"),(0,1),inplace=True)
df.Embarked.replace(("S","C","Q"),(0,1,2),inplace=True)
df.Title.replace(('Mr','Miss','Mrs','Master','Dr','Rev','Officer','Royalty'), (0,1,2,3,4,5,6,7), inplace = True)
df.drop("Ticket",axis=1,inplace=True)
##############
from sklearn.model_selection import train_test_split
x=df.drop(["Survived","PassengerId"],axis=1)
y=df["Survived"]
x_train,x_val,y_train,y_val=train_test_split(x,y,test_size=0.2,random_state=1979)
import pickle #It saves our model parameters. Fantastic!
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
####
randomforest=RandomForestClassifier()
randomforest.fit(x_train,y_train)
y_pred=randomforest.predict(x_val)
accuracy_randomforest=round(accuracy_score(y_pred,y_val)*100,2)
#print("random forest acccuracy is :",accuracy_randomforest)
pickle.dump(randomforest,open('titanic_model.sav','wb'))

def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x=[[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest=pickle.load(open('titanic_model.sav','rb'))
    predictions=randomforest.predict(x)
    print(predicitons)
