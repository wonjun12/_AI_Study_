import streamlit as st # 프레임 워크
import pandas as pd


import altair as alt

import plotly.express as px # 설치 해야함

# 기본 형식
def main():
    st.title('웹 차트 데시보드')

    df1 = pd.read_csv('data/lang_data.csv')

    st.dataframe(df1)

    st.text(df1.shape)

    #print(df1.columns[1:])

    lang_list = df1.columns[1:]

    choice_list = st.multiselect('언어를 선택하라.', lang_list)
    
    if choice_list != []:
        choice_df = df1[choice_list]

        st.dataframe(choice_df)

        # 스트림릿이 제공하는 라인차트
        st.line_chart(choice_df)

        # 스트림릿이 제공하는 영역차트
        st.area_chart(choice_df)
    

    # 
    df2 = pd.read_csv('data/iris.csv')

    # 스트림릿이 제공하는 바차트
    df3 = df2[['sepal_length', 'sepal_width']]
    st.bar_chart(df3)

    # Altair
    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species'
    )
    st.altair_chart(chart)

    # 스트림릿의 map 차트
    df4 = pd.read_csv('data/location.csv',index_col=0)
    print(df4)
    st.map(df4, 7)


    # plotly의 pie 차트 
    # 비율을 보고 싶을때
    df5 = pd.read_csv('data/prog_languages_data.csv', index_col=0)
    st.dataframe(df5)
    
    fig1 = px.pie(df5, 'lang', 'Sum', title='각 언어별 비율')
    st.plotly_chart(fig1)

    # plotly의 bar 차트
    df5 = df5.sort_values('Sum', ascending=False)
    fig2 = px.bar(df5, x='lang', y='Sum')
    # 차트를 정렬해서 보여주고 싶을때는 pandas에서 미리 정렬한 후 차트를 그린다.
    st.plotly_chart(fig2)



if __name__ == '__main__':
    main()