import streamlit as st
from datetime import datetime, time

# 页面配置
st.set_page_config(page_title="个人简历生成器", layout="wide")
import streamlit as st
from PIL import Image

# 图片上传组件
uploaded_img = st.file_uploader("选择一张图片上传", type=["jpg", "jpeg", "png", "gif"])

# 图片展示逻辑
if uploaded_img is not None:
    img = Image.open(uploaded_img)
    st.image(img, width=300, caption="上传的图片预览")
else:
    st.write("请上传图片")

# 左侧表单区域
with st.sidebar:
    st.subheader("个人信息表单")
    # 插入你提供的网络图片链接
    st.image("https://c-ssl.dtstatic.com/uploads/blog/202402/04/AvSzNL5VSw8L6QP.thumb.400_0.jpg", caption="个人头像", width=150)
    name = st.text_input("姓名", "廖益")
    position = st.text_input("职位", "软件测试")
    phone = st.text_input("电话", "13667815820")
    email = st.text_input("邮箱", "2328486665@qq.com")
    birth_date = st.date_input("出生日期", datetime(2024, 10, 21))
    gender = st.radio("性别", ["女"], horizontal=True)
    education = st.selectbox("学历", ["本科"])
    work_exp = st.slider("工作经验", min_value=0, max_value=10, value=0)
    salary_range = st.select_slider("期望薪资", options=[10000, 20000, 30000, 40000, 50000], value=(10000, 50000))
    best_time = st.time_input("最佳联系时间", time(8, 0))
    lang_options = st.multiselect("语言能力", ["中文", "英语"])
    st.subheader("个人简介")
    intro = st.text_area("个人简介", """廖益，女，广西职业师范学院大数据分析与应用专业学生，ENFP人格。专业基础扎实，掌握Python、Streamlit等工具，有简历生成器开发经验。目标成为数据专家，用数据驱动业务增长。个人热情开放、创意实践，善于探索新领域、协作解决问题。""", height=150)
    st.subheader("专业技能")
    skills = st.multiselect("技能", ["Python", "Java", "HTML/CSS", "SQL", "数据分析", "项目管理"])

# 右侧预览区域
st.title(name)
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"**职位**：{position}")
    st.markdown(f"**电话**：{phone}")
    st.markdown(f"**邮箱**：{email}")
    st.markdown(f"**出生日期**：{birth_date.strftime('%Y/%m/%d')}")
with col2:
    st.markdown(f"**性别**：{gender}")
    st.markdown(f"**学历**：{education}")
    st.markdown(f"**工作经验**：{work_exp} 年")
    st.markdown(f"**期望薪资**：{salary_range[0]}-{salary_range[1]}元")
    st.markdown(f"**最佳联系时间**：{best_time.strftime('%H:%M')}")
    st.markdown(f"**语言能力**：{', '.join(lang_options)}")

st.markdown("---")
st.subheader("个人简介")
st.write(intro)

st.markdown("---")
st.subheader("专业技能")
if skills:
    for skill in skills:
        st.markdown(f"- {skill}")
else:
    st.markdown("请在左侧选择技能")
