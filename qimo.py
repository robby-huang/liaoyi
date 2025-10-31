import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from sklearn.linear_model import LinearRegression
import joblib
st.set_page_config(page_title="学生成绩预测", page_icon="", layout="wide")

def load_data():
    df = pd.read_csv(r'D:\streamlit_env\期末考核\student_data_adjusted_rounded.csv') 
    return df
df = load_data()

model = joblib.load("score_predictor.pkl") 

page = st.sidebar.radio("导航菜单", ["项目介绍", "专业数据分析", "期末成绩预测"])

if page == "项目介绍":
    st.title("学生成绩分析与预测系统")
    st.markdown('***')
    st.header('项目概述')
    st.text('本项目是一个基于streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。')
    st.subheader('主要特点：')
    st.markdown('''- 📊数据可视化：多维度真是学生学业数据
- 🎯专业分析：按专业分类的详细统计分析
- 🔮智能预测：基于机器学习模型的成绩预测
- 💡学习建议：根据预测结果提供个性化反馈''')
    st.markdown('***')
    st.header("🚩项目目标")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.header('目标一')
        st.markdown('**分析影响因素**')
        st.markdown('''- 识别关键学习指标
- 探索成绩相关因素
- 提供数据支持决策''')
    with c2:
        st.header('目标二')
        st.markdown('**可视化展示**')
        st.markdown('''- 专业对比分析
- 性别差异研究
- 学习模式识别''')
    with c3:
        st.header('目标三')
        st.markdown('**成绩预测**')
        st.markdown('''- 机器学习模型
- 个性化预测
- 及时干预预警''')

    st.header('技术架构')
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('**前瞻框架**')
        python_code = '''Streamlit
'''
        st.code(python_code, language=None)
    with c2:
        st.markdown('**数据处理**')
        python_code = '''Pandas
Numpy
'''
        st.code(python_code, language=None)
    with c3:
        st.markdown('**可视化**')
        python_code = '''Plotly
Matplotlib
'''
        st.code(python_code, language=None)
    with c4:
        st.markdown('**机器学习**')
        python_code = '''Scikit-learn
'''
        st.code(python_code, language=None)


elif page == "专业数据分析":
    st.header("专业数据分析")
    st.markdown('### 1.各专业男女性别比例')
    df_student = pd.read_csv("student_data_adjusted_rounded.csv")


    gender_count = df_student.groupby(["专业", "性别"]).size().unstack(fill_value=0)

    if gender_count.columns.tolist() == ["男", "女"]:
        gender_count = gender_count[["女", "男"]]


    gender_ratio = (gender_count / gender_count.sum(axis=1).values.reshape(-1, 1) * 100).round(1)

    df_gender = gender_ratio.reset_index()
    df_gender.columns = ["major", "女", "男"]  


    fig_gender = go.Figure()

    fig_gender.add_trace(go.Bar(
        x=df_gender["major"],
        y=df_gender["男"],
        name="男",
        marker_color="#87CEEB"
    ))

    fig_gender.add_trace(go.Bar(
        x=df_gender["major"],
        y=df_gender["女"],
        name="女",
        marker_color="#4169E1"
    ))

    fig_gender.update_layout(
        barmode="group",  
        xaxis_title="专业",  
        yaxis_title="比例(%)", 
        height=400,  
        legend_title="性别",  
        legend=dict(orientation="v", yanchor="top", y=0.99, xanchor="right", x=0.99)  
    )


    col1, col2 = st.columns([2, 1]) 
    with col1:
        
        st.plotly_chart(fig_gender, use_container_width=True)
    with col2:
        
        st.subheader("性别比例数据")
        
        st.dataframe(df_gender.set_index("major"), use_container_width=True)

    st.markdown('***')
        
    st.header("2.各专业学习指标对比")
    st.caption("各专业平均学习时间与成绩对比")

    df = pd.read_csv("student_data_adjusted_rounded.csv")

    metrics = ["每周学习时长（小时）", "期中考试分数", "期末考试分数"]
    df_major = df.groupby("专业")[metrics].mean().round(1).reset_index()
    df_melt = df_major.melt(id_vars="专业", var_name="指标", value_name="数值")


    bar_layer = alt.Chart(df_melt[df_melt["指标"] == "期中考试分数"]).mark_bar(color="#4169E1").encode(
        x=alt.X("专业", axis=alt.Axis(labelAngle=-45)),
        y=alt.Y("数值", title="指标数值"),
        tooltip=["专业", "指标", "数值"]
    )

    line_layer1 = alt.Chart(df_melt[df_melt["指标"] == "每周学习时长（小时）"]).mark_line(point=True, color="#87CEEB").encode(
        x="专业",
        y="数值",
        tooltip=["专业", "指标", "数值"]
    )

    line_layer2 = alt.Chart(df_melt[df_melt["指标"] == "期末考试分数"]).mark_line(point=True, color="#FF6347").encode(
        x="专业",
        y="数值",
        tooltip=["专业", "指标", "数值"]
    )


    chart = bar_layer + line_layer1 + line_layer2
    chart = chart.properties(height=400).configure_axis(titleFontSize=14, labelFontSize=12)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.altair_chart(chart, use_container_width=True, theme="streamlit")
    with col2:
        st.subheader("详细数据")
        st.dataframe(df_major.set_index("专业"), use_container_width=True)

    st.markdown('***')
    st.header("3.各专业出勤率分析")
    st.subheader("出勤率排名")


    df = pd.read_csv("student_data_adjusted_rounded.csv")
    df_attendance = df.groupby("专业")["上课出勤率"].mean().reset_index()
    df_attendance["平均出勤率"] = (df_attendance["上课出勤率"] * 100).round(1)
    df_attendance_sorted = df_attendance.sort_values("平均出勤率", ascending=False).reset_index(drop=True)
    df_attendance_sorted["排名"] = df_attendance_sorted.index
    df_result = df_attendance_sorted[["排名", "专业", "平均出勤率"]]


    chart = (
        alt.Chart(df_result)
        .mark_bar()
        .encode(
            x=alt.X("专业", sort="-y", title="专业"),
            y=alt.Y("平均出勤率", title="平均出勤率(%)"),
            color=alt.Color("专业", scale=alt.Scale(scheme="category10")),  
            tooltip=["排名", "专业", "平均出勤率"]
        )
        .properties(height=350)
    )


    col_chart, col_table = st.columns([1, 1])
    with col_chart:
        st.altair_chart(chart, use_container_width=True, theme="streamlit")
    with col_table:
        st.dataframe(df_result.set_index("排名"), use_container_width=True)
    st.markdown('***')
    st.header("4.大数据管理专业专项分析")


    df = pd.read_csv("student_data_adjusted_rounded.csv")
    df_bd = df[df["专业"] == "大数据管理"].copy()


    avg_study = df_bd["每周学习时长（小时）"].mean().round(1)
    avg_attend = (df_bd["上课出勤率"].mean() * 100).round(1)
    avg_final = df_bd["期末考试分数"].mean().round(1)
    pass_rate = round((len(df_bd[df_bd["期末考试分数"] >= 60]) / len(df_bd) * 100), 1)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("平均学习时间", f"{avg_study} 小时")
    with col2:
        st.metric("平均出勤率", f"{avg_attend}%")
    with col3:
        st.metric("平均期末成绩", f"{avg_final} 分")
    with col4:
        st.metric("及格率", f"{pass_rate}%")


    st.subheader("大数据管理专业期末成绩箱线图")
    boxplot = (
        alt.Chart(df_bd)
        .mark_boxplot(color="#4169E1", size=60)
        .encode(
            x=alt.X("专业:N", title="专业", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("期末考试分数:Q", title="期末成绩（分）", scale=alt.Scale(domain=[40, 100])),
            tooltip=["期末考试分数"]
        )
        .properties(height=350)
    )
    st.altair_chart(boxplot, use_container_width=True, theme="streamlit")


    st.subheader("大数据管理专业期末成绩分布")
    histogram = (
        alt.Chart(df_bd)
        .mark_bar(color="#87CEEB", opacity=0.8)
        .encode(
            x=alt.X("期末考试分数:Q", title="期末成绩（分）", bin=alt.Bin(maxbins=10)),
            y=alt.Y("count():Q", title="学生人数"),
            tooltip=[alt.Tooltip("期末考试分数:Q", bin=True, title="成绩区间"), "count():Q"]
        )
        .properties(height=350)
    )
    st.altair_chart(histogram, use_container_width=True, theme="streamlit")

else:
    st.title("🎯 期末成绩预测系统")
    st.markdown("通过输入学生的学习特征，系统将基于机器学习模型预测期末成绩并提供个性化建议")
    st.markdown("---")

    # 信息录入表单（分两列布局）
    with st.form("predict_form", clear_on_submit=False):
        st.subheader("📝 学生学习信息录入")
        h1, h2 = st.columns(2)
        
        with h1:
            student_id = st.text_input("学号", placeholder="例如：2023001001")
            gender = st.selectbox("性别", ["男", "女"])
            major = st.selectbox("专业", df["专业"].unique())
            study_hours = st.slider(
                "每周学习时长（小时）", 
                min_value=0.0, max_value=50.0, step=0.5, value=15.0,
                help="学生平均每周投入学习的时长"
            )
        
        with h2:
            attendance = st.slider(
                "上课出勤率", 
                min_value=0.0, max_value=1.0, step=0.01, value=0.8,
                help="实际出勤课时/应出勤课时"
            )
            mid_score = st.slider(
                "期中考试分数", 
                min_value=0.0, max_value=100.0, step=1.0, value=70.0
            )
            homework_rate = st.slider(
                "作业完成率", 
                min_value=0.0, max_value=1.0, step=0.01, value=0.9,
                help="已完成作业数/总作业数"
            )
        
        submit_btn = st.form_submit_button("🔍 预测期末成绩", type="primary")

    # 预测结果展示
    if submit_btn and student_id:  # 验证学号是否输入
        # 模型预测
        X = [[study_hours, attendance, mid_score, homework_rate]]
        pred_score = model.predict(X)[0]
        pred_score = max(0, min(100, round(pred_score, 1)))  # 限制在0-100并保留1位小数

        # 结果卡片
        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
        st.subheader(f"📊 学号 {student_id} 的预测结果")
        
        # 分数展示（带进度条）
        z1, z2 = st.columns([1, 3])
        with z1:
            st.markdown(f'<div class="result-highlight">{pred_score} 分</div>', unsafe_allow_html=True)
        with z2:
            st.progress(pred_score / 100)  # 进度条可视化分数
        
        # 等级评定
        if pred_score >= 90:
            st.success("🌟 成绩等级：优秀")
            st.image("https://n.sinaimg.cn/sinakd20112/317/w960h957/20230209/a75f-9a7923a9af325774a9e7edce00f0794c.jpg", width=200)
        elif pred_score >= 80:
            st.success("👍 成绩等级：良好")
            st.image("https://c-ssl.dtstatic.com/uploads/blog/202109/26/20210926150543_31dc7.thumb.400_0.jpeg",width=200)
        elif pred_score >= 60:
            st.info("✅ 成绩等级：合格")
            st.image("https://imgs.qiubiaoqing.com/qiubiaoqing/imgs/67cda61f47a88YGx.jpeg", width=200)
        else:
            st.warning("⚠️ 成绩等级：待提高")
            st.image("https://imgs.qiubiaoqing.com/qiubiaoqing/imgs/67c65f100d0f02Yp.jpeg", width=200)
        
        # 个性化建议
        st.markdown('<div class="advice-box">', unsafe_allow_html=True)
        st.subheader("💡 学习建议")
        if attendance < 0.7:
            st.markdown("- 建议提高出勤率，课堂互动对成绩影响显著")
        if homework_rate < 0.8:
            st.markdown("- 需加强作业完成质量，作业是巩固知识的关键")
        if study_hours < 10:
            st.markdown("- 建议增加每周学习时长，保证足够的知识消化时间")
        if pred_score < 60:
            st.markdown("- 可针对性复习期中考试薄弱环节，必要时寻求老师帮助")
        else:
            st.markdown("- 保持当前学习状态，建议定期总结知识体系，查漏补缺")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif submit_btn:
        st.error("请输入学号后再进行预测")
