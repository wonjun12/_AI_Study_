import streamlit as st
import os


# 파일 업로드 함수가 계속해서 반복되다보니 파일로 만들어서 작성한다.
def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리(폴더) 있는지 확인
    #   없다면 디렉토리를 먼저 만든다.
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # 2. 디렉토리가 있으니, 파일 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('파일 업로드 성공!')