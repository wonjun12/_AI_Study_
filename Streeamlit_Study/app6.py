import streamlit as st # 프레임 워크
# 프레임워크란? 
# 툴에서 정해진 규칙에 따라 사용가능한 것

# 기본 형식
def main():
    st.title('키보드 입력 받기')
    
    # 문자 입력
    name = st.text_input('이름 입력하세요', max_chars=10)
    st.text(f"당신의 이름은 : {name}")

    message = st.text_area('메시지를 입력하세요.', height=10)
    st.text(message)


    # 숫자 입력
    # number = st.number_input('숫자를 입력하세요.', min_value=1)
    number = st.number_input('숫자를 입력하세요.', 1.0, 5.0)
    st.text(number * 5)

    # 날짜 입력
    my_date = st.date_input('약속 날짜 입력')
    print(type(my_date))
    st.text(my_date)

    # 시간 
    my_time = st.time_input('시간 선택')
    st.text(my_time)

    # 비밀번호 처리
    password = st.text_input('비밀번호 입력', type='password')
    st.text(password)

    # 색 입력
    color = st.color_picker('색을 선택하세요.')
    st.text(color)




if __name__ == '__main__':
    main()