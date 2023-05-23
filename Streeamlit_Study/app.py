import streamlit as st # 프레임 워크
# 프레임워크란? 
# 툴에서 정해진 규칙에 따라 사용가능한 것

# 기본 형식
def main():
    # 화면에 관해 처리를 하고 싶다면 st를 사요해야한다.
    st.title('앱 데시보드')
    # 대부분 main에서 작업을 한다.
    st.text('테스트 텍스트')
    st.text('텍스트')


if __name__ == '__main__':
    main()