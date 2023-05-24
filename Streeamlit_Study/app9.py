import streamlit as st # 프레임 워크
# 프레임워크란? 
# 툴에서 정해진 규칙에 따라 사용가능한 것
import pandas as pd


import matplotlib.pyplot as plt
import seaborn as sns

# 기본 형식
def main():
    st.title('차트 데시보드')
    df = pd.read_csv('data/iris.csv')

    st.dataframe(df)

    # sepal_length, sepal_width 의 관계를 차트로 
    fig = plt.figure() # 차트 영역 표시
    plt.scatter(
        data=df,
        x='sepal_length',
        y='sepal_width',
    )
    plt.title('sepal length vs width')
    plt.xlabel('length')
    plt.ylabel('width')
    st.pyplot(fig)
    

    fig2 = plt.figure()
    sns.regplot( # 리그레이션 데이터 피팅 선을 찾는다.
        data=df,
        x='sepal_length',
        y='sepal_width',
    )
    st.pyplot(fig2)

    # 상관관계 표시
    correlation = df[['sepal_length', 'sepal_width']].corr()
    st.dataframe(correlation) #그래프가 아니라 dataframe이다.

    # sepal_length 히스토그램 그리자.
    # bin의 갯수는 20개 (범위)
    fig3 = plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
        # 1행 2열의 그래프를 만들고 1번째에 그래프를 그리겠다.
    plt.hist(
        data = df,
        x = 'sepal_length',
        rwidth=0.8, #막대 크기 조절
        bins=20
    )
    plt.subplot(1, 2, 2)
    plt.hist(
        data = df,
        x = 'sepal_length',
        rwidth=0.8, #막대 크기 조절
        bins=10
    )
    st.pyplot(fig3)

    # species 컬럼에는 종에 대한 정보가 들어있는데,
    # 각 종 별로 몇개씩 데이터가 있는지, 차트로 나타내시오.
    st.dataframe(df['species'].value_counts())
    fig4 = plt.figure()
    sns.countplot(
        data = df,
        x = 'species'
    )
    st.pyplot(fig4)


    # 데이터 프레임의 차트 그리는 코드도 실행 가능
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig5)


    # 데이터 프레임 자체 plot 함수는 스트림릿에서 안된다.
    # fig6 = plt.figure()
    # df.plot() # 주피터에서는 사용가능하지만, 여기서는 안됨
    # st.pyplot(fig6)
    
    fig7 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig7)

    

if __name__ == '__main__':
    main()