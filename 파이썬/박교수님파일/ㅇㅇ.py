import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

testcopy = test.copy()

train.head(5)

print('Train clumns with null values: \n{} \n'. format(train.isnull().sum()))

print('Test clumns with null values: \n{} \n'. format(test.isnull().sum()))

train.describe()
test.describe()

train['Age'].fillna(train['Age'].median(), inplace = True)
train['Embarked'].fillna(train['Embarked'].mode()[0], inplace = True)
train['Fare'].fillna(train['Fare'].median(), inplace = True)

test['Age'].fillna(test['Age'].median(), inplace = True)
test['Embarked'].fillna(test['Embarked'].mode()[0], inplace = True)
test['Fare'].fillna(test['Fare'].median(), inplace = True)

print('Tarin columns with null valuse: \n{} \n'. format(train.isnull().sum()))
print('Test columns with null valuse: \n{} \n'. format(test.isnull().sum()))

drop_column = ['PassengerId','Cabin','Ticket']
train.drop(drop_column, axis=1, inplace = True)
test.drop(drop_column, axis=1, inplace = True)

print('Tarin columns with null valuse: \n{} \n'. format(train.isnull().sum()))
print('Test columns with null valuse: \n{} \n'. format(test.isnull().sum()))

alltables = [train, test]

for dataset in alltables:    
    
    # 가족의 수
    dataset['FamilySize'] = dataset ['SibSp'] + dataset['Parch'] + 1

    # 혼자 탑승했는지 여부
    dataset['IsAlone'] = 1 # 초기값을 1로 지정
    dataset['IsAlone'].loc[dataset['FamilySize'] > 1] = 0 # 만약 가족의 수가 1보타 크면 0으로 변경

    # 이름에서 Mr. MIss 등을 분리해서 Title 변수로 지정
    dataset['Title'] = dataset['Name'].str.split(", ", expand=True)[1].str.split(".", expand=True)[0]


    # 운임요금을 4등급으로 나눠 범주형 변수로 변환
    dataset['FareBin'] = pd.qcut(dataset['Fare'], 4)

    # 나이를 4등급으로 나눠 범주형 변수로 변환
    dataset['AgeBin'] = pd.cut(dataset['Age'].astype(int), 5)

# 희귀한 이름 찾기
title_names = (train['Title'].value_counts() < 10) #this will create a true false series with title name as index

# 적용
train['Title'] = train['Title'].apply(lambda x: 'Misc' if title_names.loc[x] == True else x)
print(train['Title'].value_counts())

import seaborn as sns
sns.countplot(x="Survived", data=train)
plt.show()

fig, saxis = plt.subplots(2, 2,figsize=(8,8))

# Embarked, IsAlone, Pclass, Sex에 따른 생존 유무
sns.countplot(x='Survived', hue="Embarked", data=train,ax = saxis[0,0])   
sns.countplot(x='Survived', hue="IsAlone", data=train,ax = saxis[0,1])
sns.countplot(x="Survived", hue="Pclass", data=train, ax = saxis[1,0])
sns.countplot(x="Survived", hue="Sex", data=train, ax = saxis[1,1])
plt.show()