import streamlit as st
from datetime import datetime
from app8_folder.app8_utills import save_uploaded_file
# 파일 업로드 함수
# 디렉토리 이름, 파일을 주면 해당 디렉토리에 파일을 저장해주는 함수

def run_app8_image():
    st.subheader('이미지 파일 업로드')

    img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])
    if img_file is not None: # 파일이 없는 경우는 실행 하지 않음
        print(type(img_file))
        print(img_file.name)
        print(img_file.size)
        print(img_file.type)

        # 유저가 올린 파일을,
        # 서버에서 처리하기 위해서(유니크하게) 
        # 파일명을 현재 시간 조합으로 만든다. 
        current_time = datetime.now()
        print(current_time)
        print(current_time.isoformat().replace(':', "_") + '.jpg') #문자열로 만들어 달라
        # 파일 명에 특정 특수문자가 들어가면 만들수 없다.
        filename = current_time.isoformat().replace(':', "_") + '.jpg'
        img_file.name = filename

        save_uploaded_file('image', img_file)

        st.image(f'image/{img_file.name}')