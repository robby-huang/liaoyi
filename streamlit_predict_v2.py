import streamlit as st
import pickle
import pandas as pd
import inspect
import os
import pickle
island = ""
sex = ""
bill_length = 0.0
bill_depth = 0.0
flipper_length = 0.0
body_mass = 0.0
submitted = False
st.set_page_config(
    page_title='企鹅分类器🐧',
    page_icon=':penguin:',
    layout='wide',
)
with st.sidebar:
    st.image('https://static.yueya.net/shuomingshu.cn//wp-content/uploads/images/2022/11/25/25603b72f9c344b0998e1c11317c8a0a_3qfgo4dazfi.jpg',width=150)
    st.title('请选择页面')
    page = st.selectbox("请选择页面", ["简介页面", "预测分类页面"], label_visibility='collapsed')
if page == "简介页面":
    st.title("企鹅分类器:penguin:")
    st.header('数据集介绍📖')
    st.markdown("""***:blue[帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集，也可以作为机器学习入门练习。
            该数据集是由Gorman等收集，并发布在一个名为palmerpenguins的R语言包，以对南极企鹅种类进行分类和研究。
            该数据集记录了344行观测数据，包含3个不同物种的企鹅：阿德利企鹅、巴布亚企鹅和帽带企鹅的各种信息。]***""")
    st.header('三种企鹅的卡通图像📌')
    st.image('https://animalspork.com/wp-content/uploads/2025/02/rs57281.1600x0.jpg')
elif page == "预测分类页面":
    st.header("预测企鹅分类👀")
    st.markdown("***:blue[这个Web应用是基于帕尔默群岛企鹅数据集构建的模型。只需输入6个信息，就可以预测企鹅的物种，使用下面的表单开始预测吧！]***")
    col_form, col, col_logo = st.columns([3, 1, 2])
    with col_form:
        with st.form('user_inputs'):
            island = st.selectbox('企鹅栖息的岛屿🍇', options=['托尔森岛', '比斯科群岛', '德里姆岛'])
            sex = st.selectbox('性别🍉', options=['雄性', '雌性'])
            bill_length = st.number_input('喙的长度（毫米）🍌', min_value=0.0)
            bill_depth = st.number_input('喙的深度（毫米）🍒', min_value=0.0)
            flipper_length = st.number_input('翅膀的长度（毫米）🥥', min_value=0.0)
            body_mass = st.number_input('身体质量（克）🥝', min_value=0.0)
            submitted = st.form_submit_button('预测分类')

island_biscoe, island_dream, island_torgerson = 0, 0, 0
if island == '比斯科群岛': 
    island_biscoe = 1
elif island == '德里姆岛':
    island_dream = 1
elif island == '托尔森岛':
    island_torgerson = 1
sex_female, sex_male = 0, 0
if sex == '雌性':
    sex_female = 1
elif sex == '雄性':
    sex_male = 1
format_data = [bill_length, bill_depth, flipper_length, body_mass, island_dream, island_torgerson, island_biscoe, sex_male, sex_female]
filename = inspect.getframeinfo(inspect.currentframe()).filename
script_dir = os.path.dirname(os.path.abspath(filename))
model_path = os.path.join(script_dir,'rfc_model.pkl')
with open(model_path, 'rb') as f1:
    rfc_model = pickle.load(f1)
print(model_path)
uniques_path = os.path.join(script_dir,'output_uniques.pkl')
with open(uniques_path, 'rb') as f2:
    output_uniques = pickle.load(f2)
output_uniques_map = output_uniques
print(output_uniques_map)
print(model_path)
if submitted:
    format_data_df = pd.DataFrame(data=[format_data], columns=rfc_model.feature_names_in_)
    predict_result_code = rfc_model.predict(format_data_df)
    predict_result_species = output_uniques_map[predict_result_code][0]
    st.write(f'根据您输入的数据，预测该企鹅的物种名称是：**{predict_result_species}**')
    with col_logo:
      if not submitted:
          st.image('https://static.vecteezy.com/system/resources/previews/001/877/354/original/cute-cartoon-happy-penguin-vector.jpg', width=300)
      else:
          species_img_map = {"阿德利企鹅":"https://media.australian.museum/media/dd/images/adelie_penguin.d48bf94.width-800.1f7b749.jpg",
                             "巴布亚企鹅":"https://www.wildnatureimages.com/images/xl/130105-087-Gentoo-Penguin_.jpg",
                             "帽带企鹅":"https://img.burrard-lucas.com/antarctica/full/chinstrap_penguin.jpg"}
        
          st.image(species_img_map[predict_result_species], width=300)
    
