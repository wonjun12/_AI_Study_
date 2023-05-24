import streamlit as st
from datetime import datetime
import pandas as pd

from app8_folder.app8_utills import save_uploaded_file

def run_app8_csv():
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