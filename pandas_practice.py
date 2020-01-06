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

