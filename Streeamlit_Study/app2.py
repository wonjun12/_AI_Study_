import streamlit as st
# 웹브라우저 표시할때 사용


def main():
    st.title('웹 대시보드')

    name = '읾륾'
    
    print(f"제 이름은 {name}")

    st.text(f"제 이름은 {name}")
    st.header('헤더 영역')
    st.subheader('서브헤더 영역')
    st.success('성공했다? 싶은 문장')
    st.warning('경고다?')
    st.info('알?림')
    st.error('에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러에러')

    st.help(range)
    


if __name__ == '__main__':
    main()
