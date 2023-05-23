import streamlit as st # 프레임 워크
import pandas as pd
# 데이터 프레임 출력하기 위해 pandas 모듈 사용

# 기본 형식
def main():
    st.title('앱 데시보드')
    df = pd.read_csv('data/iris.csv')
    # print(df)
    # 웹 브라우저에 데이타프레임 작성
    st.dataframe(df)

    specie_nuniq = df['species'].nunique()
    specie_uniq = df['species'].unique()

    st.text(f"아이리스 꽃의 종류는 {specie_nuniq}개 이다.")
    st.text(f"아이리스 꽃은 {specie_uniq}으로 되어있다.")

    # write : 니 맘대로 작성하렴
    st.write(df.head())




if __name__ == '__main__':
    main()