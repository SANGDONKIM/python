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

