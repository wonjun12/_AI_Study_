import streamlit as st # 프레임 워크

from app8_folder.app8_image import run_app8_image
from app8_folder.app8_csv import run_app8_csv
from app8_folder.app8_about import run_app8_about

# 기본 형식
def main():
    st.title('앱 데시보드')

    menu = ['이미지 업로드', 'csv 업로드', 'About']

    choice = st.sidebar.selectbox('메뉴', menu)
    
    if choice == menu[0]:
        run_app8_image()

    elif choice == menu[1]:
        run_app8_csv()

    else :
        run_app8_about()

if __name__ == '__main__':
    main()