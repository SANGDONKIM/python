import pandas as pd
import os

os.getcwd()

df=pd.read_csv("C:/Users/sangdon/Desktop/python/doit_pandas-master/doit_pandas-master/data/gapminder.tsv", sep='\t')

print(df.head())

df.shape

df.columns

df.dtypes # 문자형의 경우 object로 인식

df.info()

country_df=df['country']
type(country_df) # series
country_df.head()
country_df.tail()

subset=df[['country', 'continent', 'year']]
type(subset) # 2개 이상 열이므로 dataframe


# 행 번호로 데이터 추출
df.loc[0] # 자료형이 series
df.tail(n=1) # 자료형이 dataframe

df.loc[[1,2]]


subset=df.loc[:,['year', 'pop']]
subset.head()

subset=df.iloc[:, [2,4,-1]]
subset.head()

small_range=list(range(5))
subset=df.iloc[:, small_range]
subset.head()


subset=df.iloc[:, 0:6:2] # 0, 2, 4번째 열 선택
subset.head()

df.head()

df.loc[[0,99,999], ['country', 'lifeExp']]

# iloc : 행번호만 활용 가능, 열 지정값에 이름 x
# loc : 열 지정값에 정수 리스트 x

# 그룹화한 데이터의 평균 구하기
df.groupby('year')['lifeExp'].mean()
df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean().head()

# 빈도수 구하기
df.groupby('continent')['country'].nunique()


# 그래프 그리기
import matplotlib.pyplot as plt
plt.style.use('ggplot')
global_yearly_life_expectancy=df.groupby('year')['lifeExp'].mean()
global_yearly_life_expectancy.head()

global_yearly_life_expectancy.plot()


# 나만의 데이터 만들기
s=pd.Series(['banana', 42])
s

s=pd.Series(['Wes McKinney', 'Creator of Pandas'])
s

s=pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Pearson', 'Who']) # 문자열을 인덱스로 지정
s

# 데이터 프레임 만들기

scientists=pd.DataFrame({
    'Name' : ['Rosaline', 'William'],
    'Born' : ['1920-07-25', '1876-06-13'],
    'Died': ['1960-07-27', '1937-10-16'],
    'Age' : [37, 61]
})

scientists

scientists=pd.DataFrame({
    'Occupation' : ['Chemist', 'Statistician'],
    'Born' : ['1920-07-25', '1876-06-13'],
    'Died': ['1960-07-27', '1937-10-16'],
    'Age' : [37, 61]
},
index=['Rosaline', 'Williams'],
columns=['Born', 'Age', 'Occupation']) # columns로 열 순서 변경 가능, 열 선택도 가능

scientists # 딕셔너리는 입력한 순서대로 출력을 보장하지 않음

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
vals = ['app', 'bow', 'cow', 'doc', 'err', 'fly', 'gpu']
d = {key: val for key, val in zip(keys, vals)}
d

# 데이터의 순서를 보장할 경우 orderedDict
from _collections import orderedDict


import pandas as pd
scientists = pd.DataFrame({
    'Occupation' : ['Chemist', 'Statistician'],
    'Born' : ['1920-07-25', '1876-06-13'],
    'Died': ['1960-07-27', '1937-10-16'],
    'Age' : [37, 61]},
index=['Rosaline', 'Williams'],
columns=['Occupation', 'Born', 'Died', 'Age'])

first_row=scientists.loc['Williams']
type(first_row)

first_row.index
first_row.values

first_row.index[0]

ages=scientists['Age']
ages

ages.mean()
ages.std()

age.describe() # 요약통계량
age.drop_duplicates() # 중복이 없는 시리즈

age.median()

age.sort_values()

age.to_frame() # 데이터프레임으로 변환



# 데이터 프레임

scientists=pd.read_csv("C:/Users/sangdon/Desktop/python/doit_pandas-master/doit_pandas-master/data/scientists.csv")
ages=scientists['Age']

scientists[scientists['Age']>scientists['Age'].mean()]

scientists[scientists['Age']>scientists['Age'].mean()]*2


# 데이터 처리하기

print(scientists['Born'].dtype)
print(scientists['Died'].dtype)

print(scientists['Born'])
print(scientists['Died'])


# 날짜 변수 datetime 형식으로 변경
born_datetime=pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datetime)

died_datetime=pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(died_datetime)

# 열 추가
scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
scientists.shape

scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
scientists.head()

# 열 무작위로 섞기
import random

random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])

# 열 삭제

scientists_dropped = scientists.drop(['Age'], axis=1) # axis = 1 : 열 삭제, axis = 0 : 행 삭제
print(scientists_dropped.columns)


# 데이터 저장 및 불러오기

# 피클 : 스프레드 시트보다 더 작은 용량으로 데이터 저장 가능. 객체 속성 보존

names = scientists['Name']
names.to_pickle("C:/Users/sangdon/Desktop/python/doit_pandas-master/doit_pandas-master/data/scientists_df.pickle")

# 불러오기
scientist_names_from_pickle = pd.read_pickle("C:/Users/sangdon/Desktop/python/doit_pandas-master/doit_pandas-master/data/scientists_df.pickle")
scientist_names_from_pickle.head()


# xls, xlsx
names_df=names.to_frame()
import xlwt
names_df.to_excel("C:/Users/sangdon/Desktop/python/doit_pandas-master/doit_pandas-master/data/scientists_df.xls")

import openpyxl
names_df.to_excel("C:/Users/sangdon/Desktop/python/doit_pandas-master/doit_pandas-master/data/scientists_df.xlsx")



# 시각화
import seaborn as sns

anscombe = sns.load_dataset('anscombe')
anscombe.head()

import matplotlib.pyplot as plt

dataset_1=anscombe[anscombe['dataset']=='I']
plt.plot(dataset_1['x'], dataset_1['y']) # 선 산점도
plt.plot(dataset_1['x'], dataset_1['y'], 'o') # 점 산점도


dataset_2=anscombe[anscombe['dataset']=='II']
dataset_3=anscombe[anscombe['dataset']=='III']
dataset_4=anscombe[anscombe['dataset']=='IV']

fig = plt.figure() # 기본 틀
# 구역 나누기
axes1 = fig.add_subplot(2, 2, 1) # 행 크기, 열 크기
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(dataset_1['x'], dataset_1['y'], 'o') # 점 찍기
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

# 제목
axes1.set_title('dataset_1')
axes2.set_title('dataset_2')
axes3.set_title('dataset_3')
axes4.set_title('dataset_4')

fig

# 전체 제목 추가
fig.suptitle('Anscombe Data')

# 글자가 겹칠 때
fig.tight_layout()


tips = sns.load_dataset('tips')
tips.head()
type(tips)

# 히스토그램
fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
axes1.hist(tips['total_bill'], bins=10)
axes1.set_title('histogram of total bill')
axes1.set_xlabel('frequency')
axes1.set_ylabel('total bill')

# 산점도
scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1,1,1)
axes1.scatter(tips['total_bill'], tips['tip'])
axes1.set_title('scatterplot of total bill vs tip')
axes1.set_xlabel('total bill')
axes1.set_ylabel('tip')

# 상자 그림
boxplot = plt.figure()
axes1 = boxplot.add_subplot(1,1,1)

axes1.boxplot([tips[tips['sex'] == 'Female']['tip'],
              tips[tips['sex'] == 'Male']['tip']],
              labels = ['Female', 'Male'])

# 성별을 0, 1 로 치환
def recode_sex(sex) :
    if sex == 'Female':
        return 0
    else :
        return 1

tips['sex_color'] = tips['sex'].apply(recode_sex)
scatter_plot=plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(
    x=tips['total_bill'],
    y=tips['tip'],
    s=tips['size']*10,
    c=tips['sex_color'],
    alpha = 0.5)


# seaborn 라이브러리 활용

ax = plt.subplots()
ax = sns.distplot(tips['total_bill']) # 히스토그램과 density가 같이 그려짐
ax.set_title('total bill histogram with density plot')
ax = sns.distplot(tips['total_bill'], kde=False) # density 제외
ax = sns.distplot(tips['total_bill'], hist=False) # histogram 제외
ax = sns.distplot(tips['total_bill'], rug=True) # rug 그래프 추가

ax = plt.subplots()
ax = sns.countplot('day', data=tips)


# 이변량 그래프

ax = plt.subplots()
ax = sns.regplot(x = 'total_bill', y= 'tip', data = tips) # 산점도와 회귀직선을 함께 그림
ax = sns.regplot(x = 'total_bill', y= 'tip', data = tips, fit_reg=False) # 회귀직선 제외

joint = sns.jointplot(x='total_bill', y='tip', data = tips)
joint.fig.suptitle('joint plot of total bill and tip', fontsize = 10)


hexbin = sns.jointplot(x='total_bill', y='tip', data = tips, kind='hex')

# 2차원 density

ax = sns.kdeplot(data=tips['total_bill'],
                 data2=tips['tip'],
                 shade = True)

# 막대 그래프
ax = plt.subplots()
ax = sns.barplot(x='time', y='total_bill', data=tips)

# 상자 그림
ax = plt.subplots()
ax = sns.boxplot(x='time', y='total_bill', data=tips)


# 데이터의 분산을 강조하고 싶을 때
ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', data=tips)


# 관계 그래프
fig = sns.pairplot(tips)

pair_grid = sns.PairGrid(tips)
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.distplot, rug = True)


# 다변량 그래프

# 바이올린 그래프
ax = plt.subplots()
ax = sns.violinplot(x = 'time', y = 'total_bill', data = tips, split = True) # hue : 색상 추가

scatter = sns.lmplot(x = 'total_bill', y= 'tip', data = tips, hue = 'sex', fit_reg=False)

fig = sns.pairplot(tips, hue = 'sex')


# 산점도 모양 및 크기 조절
scatter = sns.lmplot(x = 'total_bill', y= 'tip', data = tips, hue = 'sex', fit_reg=False,
                     scatter_kws={'s' : tips['size']*10})

# 점 모양 바꾸기
scatter = sns.lmplot(x = 'total_bill', y= 'tip', data = tips, hue = 'sex', fit_reg=False,
                     scatter_kws={'s' : tips['size']*10}, markers=['o', 'x'])


# 그룹별로 그래프 나눠서 그리기

anscombe_plot = sns.lmplot(x= 'x', y= 'y', data = anscombe, fit_reg = False,
                           col = 'dataset', col_wrap=2) # col_wrap : 그래프 그릴 열의 최대값 지정

facet = sns.FacetGrid(data = tips, col = 'time')
facet.map(sns.distplot, 'total_bill', rug = True)


facet = sns.FacetGrid(tips, col = 'day', hue = 'sex')
facet = facet.map(plt.scatter, 'total_bill', 'tip')
facet = facet.add_legend()

facet = sns.FacetGrid(tips, col='time', row = 'smoker', hue = 'sex')
facet.map(plt.scatter, 'total_bill', 'tip')


# 스타일 변경

sns.set_style('whitegrid')