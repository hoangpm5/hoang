import streamlit as st # gọi thư viện streamlit
with st.sidebar:
    image = "https://ticketgo.vn/photos/70/hinhanh-tintuc/5d30234792700.jpg"
    st.image(image, caption='Đen Vâu')
    st.write('Họ và tên: Nguyễn Đức Cường')
    st.write('Nghệ danh: Đen Vâu')
    st.write('''Nguyễn Đức Cường, thường được biết đến với nghệ danh Đen Vâu hay Đen, là một nam rapper
              và nhạc sĩ người Việt Nam. Đen Vâu từng giành được giải cống hiến và là một trong số ít nghệ sĩ
             thành công từ làn sóng underground và âm nhạc indie của Việt Nam.''')
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    b1 = st.button('Bài hát của Đen Vâu')
with col2:
    b2 = st.button('Bài hát của Hà anh Tuấn')    
with col3:
    b3 = st.button('Những bản nhạc giúp tâm trạng vui vẻ hơn')   
if b1:
    with st.expander('Đen Vâu'):
        st.title('MV yêu thích')
        #video số 1
        st.write('Đi về nhà')
        video = 'https://www.youtube.com/watch?v=vTJdVE_gjI0'
        st.video(video, format='video/mp4')
        #video số 2
        st.write('Mang tiền về cho mẹ')
        video_2 = 'https://www.youtube.com/watch?v=UVbv-PJXm14'
        st.video(video_2, format='video/mp4')
if b2:
    with st.expander('Hà Anh Tuấn'):
        st.title('MV YÊU THÍCH')
        #video số 3
        st.write('Vào hạ')
        video_3 ='https://www.youtube.com/watch?v=lXx-kdlxL48&list=RDEMrx5Xy48sg-WCr9qiaw1hhg&index=10'
        st.video(video_3, format='video/mp4')


        #video số 4
        st.write('Nước ngoài')
        video_4 = 'https://www.youtube.com/watch?v=pU3O9Lnp-Z0&list=RDEMrx5Xy48sg-WCr9qiaw1hhg&index=19'
        st.video(video_4, format='video/mp4')
        
        #video số 5
        st.write('STAY HOME, STAY HAPPY, STAY HÀANHTUẤN')
        video_5 = 'https://www.youtube.com/watch?v=MMgPOQ9gJhM&list=RDEMrx5Xy48sg-WCr9qiaw1hhg&index=2'
        st.video(video_5, format='video/mp4')
