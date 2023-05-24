import streamlit as st # 프레임 워크

from PIL import Image

# 기본 형식
def main():
    st.title('사진과 영상 보여주는 방법')

    # 사진 파일 열기
    img = Image.open('data/image_03.jpg')
    print(img)

    st.image(img)

    st.image(img, use_column_width=True)

    #이미지 URL로 불러와서 보여주기
    st.image('https://blog.kakaocdn.net/dn/c5yBDX/btq0tYV8yLt/v8fw4Tkc43yBFSQd4MTKK1/img.png')

    # 비디오
    # rb?
    # read bynery
    video_file = open('data/video1.mp4', 'rb')
    st.video(video_file)


if __name__ == '__main__':
    main()