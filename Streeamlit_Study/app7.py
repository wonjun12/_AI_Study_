import streamlit as st

import pandas as pd

from datetime import datetime

import os # 경로 탐색

# 파일 업로드 함수
# 디렉토리 이름, 파일을 주면 해당 디렉토리에 파일을 저장해주는 함수
def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리(폴더) 있는지 확인
    #   없다면 디렉토리를 먼저 만든다.
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # 2. 디렉토리가 있으니, 파일 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('파일 업로드 성공!')



# 기본 형식
def main():
    st.title('앱 데시보드')

    menu = ['이미지 업로드', 'csv 업로드', 'About']

    choice = st.sidebar.selectbox('메뉴', menu)
    
    if choice == menu[0]:
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


    elif choice == menu[1]:
        st.subheader('csv 파일 업로드 ')

        csv_file = st.file_uploader('CSV 파일 업로드', type=['csv'])

        print(csv_file)
        if csv_file is not None:
            current_time = datetime.now()
            filename = current_time.isoformat().replace(':', '_') + '.csv'

            csv_file.name = filename

            save_uploaded_file('csv', csv_file)

            # csv를 보여주기 위해 pandas 데이터 프레임으로 만들어야한다.
            df = pd.read_csv('csv/'+filename)
            st.dataframe(df)


    else :
        st.subheader('이 대시보드 설명')

if __name__ == '__main__':
    main()