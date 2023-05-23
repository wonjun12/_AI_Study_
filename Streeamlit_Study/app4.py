import streamlit as st # 프레임 워크
import pandas as pd # 라이브러리

# 기본 형식
def main():
    # 화면에 관해 처리를 하고 싶다면 st를 사요해야한다.
    st.title('앱 데시보드')
    
    df = pd.read_csv('data/iris.csv')

    # 버튼 만들기
    if st.button('데이터 보기 버튼 눌러!!!!!!!!!!!!!!!!!!!!!!!!'): # if를 넣으면 버튼을 누를시에 발동된다는 말임
        st.dataframe(df)

    name = 'Taiwan Number One'
    # 대문자 버튼을 누르면, 대문자로 표시하고,
    # 소문자 버튼을 누르면 소문자로 나오게 하자.
    if st.button('대문자'):
        st.text(name.lower())

    if st.button('소문자'):
        st.text(name.upper())
    

    st.dataframe(df)

    # 정렬할려한다 : petal_length 기준
    # 오름차순 정렬, 내림차순 정렬 2가지 선택 옵션 radio
    status = st.radio('정렬을 선택하라', ['오름차순', '내림차순'])

    if status == '오름차순':
        st.dataframe(df.sort_values('petal_length'))

    elif status == '내림차순' :
        st.dataframe(df.sort_values('petal_length', ascending=False))


    # checkbox
    if st.checkbox('체크박스 데이터프레임 보기'):
        st.dataframe(df.head())
    else : 
        st.write('데이터가 없음')

    # 여러개 중에 1개를 선택할때
    languages = ['Python', 'Java', 'C', 'Go', 'PHP']
    selected_lang = st.selectbox('선호하는 언어 선택 박스', languages)
    
    if selected_lang == 'Python':
        st.write('파이썬을 선택했다니!')


if __name__ == '__main__':
    main()