import streamlit as st # gọi thư viện streamlit
from sklearn.linear_model import LinearRegression


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
with col4:
    b4 = st.button("🥱 Dự đoán giờ đi ngủ ")
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
        #video số 3
        st.write('Mang tiền về cho mẹ')
        video_3 = 'https://www.youtube.com/watch?v=nyw-cXXwk1s'
        st.video(video_3, format='video/mp4')
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
if b3:
    with st.expander("Những bản nhạc giúp tâm trạng vui vẻ hơn"):
        st.title('Ca khúc hay')
        st.write('Những bản nhạc giúp tâm trạng vui vẻ hơn')
        video_5 = 'https://www.youtube.com/watch?v=SlsH6PbDJZk&t=898s'
        st.video(video_5, format='video/mp4')
        st.write('Lỡ Duyên')
        video_8 = 'https://www.youtube.com/watch?v=fq_H4A3HgD4&list=RDfq_H4A3HgD4&start_radio=1&rv=fq_H4A3HgD4'
        st.video(video_8, format='video/mp4')

        st.write('Lỡ Duyên')
        video_9 = 'https://www.youtube.com/watch?v=U0ZoqmyGJo8'
        st.video(video_9, format='video/mp4')
        
        st.write('Bài hat về tình yêu quê hương đất nước')
        video_6 = 'https://www.youtube.com/watch?v=GOMGeUetqlI&list=RDSlsH6PbDJZk&index=3'
        st.video(video_6, format='video/mp4')

        st.write('Đi giữa trời rực rỡ')
        video_7 = 'https://www.youtube.com/watch?v=D1Uf9vREh6Q&list=RDSlsH6PbDJZk&index=3'
        st.video(video_7, format='video/mp4')
# Khởi tạo trạng thái nếu chưa có
if "show_sleep_predictor" not in st.session_state:
    st.session_state.show_sleep_predictor = False

# Nếu nhấn nút "🥱 Dự đoán giờ đi ngủ", bật trạng thái
if b4:
    st.session_state.show_sleep_predictor = True

# Nếu trạng thái đã được bật, hiển thị phần dự đoán
if st.session_state.show_sleep_predictor:
    with st.expander("🛌 Dự đoán giờ đi ngủ", expanded=True):
        st.title("😀 Dự đoán số giờ ngủ cần thiết")

        # Dữ liệu mẫu
        x = [
            [10, 8, 1],
            [20, 6, 5],
            [25, 3, 8],
            [30, 2, 6],
            [50, 2, 2],
            [15, 9, 2],
            [40, 4, 3]
        ]
        y = [10, 8, 6, 6, 5, 7, 9.5]  # giờ ngủ được khuyên

        # Huấn luyện mô hình
        model = LinearRegression()
        model.fit(x, y)

        # Giao diện nhập thông tin
        st.write("Nhập thông tin của bạn:")
        age = st.number_input("Tuổi của bạn", min_value=5, max_value=100, value=25, key="tuoi")
        activity = st.slider("Mức độ hoạt động thể chất (1 = ít, 10 = rất năng động)", 1, 10, 5, key="van_dong")
        screen_time = st.number_input("Thời gian dùng màn hình mỗi ngày (giờ)", min_value=0, max_value=24, value=6, key="man_hinh")

        # Nút dự đoán
        if st.button("📊 Dự đoán ngay", key="du_doan"):
            input_data = [[age, activity, screen_time]]
            result = model.predict(input_data)[0]
            st.success(f"Bạn nên ngủ khoảng {result:.1f} giờ mỗi đêm")

            # Gợi ý thêm
            if result < 6.5:
                st.warning("😴 Có thể bạn cần nghỉ ngơi nhiều hơn để cải thiện sức khỏe.")
            elif result > 9:
                st.info("💪 Bạn có thể đang vận động nhiều – ngủ đủ giúp hồi phục cơ thể.")
            else:
                st.success("✅ Lượng ngủ lý tưởng! Hãy giữ thói quen tốt nhé.")
