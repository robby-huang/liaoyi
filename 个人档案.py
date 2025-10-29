import streamlit as st

page = st.sidebar.selectbox("选择页面", ["数字档案", "南宁美食地图", "动物图鉴","音乐播放器","视频播放器","个人简历"])

if page == "数字档案":
    # 创建一个标题展示元素
    st.title("👨‍💻学生 廖益-数字档案")

# 创建一个章节，该章节为基础信息
    st.header("🗝️基础信息")
# 创建一个文本，介绍一下基础信息
    st.markdown('###### 学生ID：23031310127')
    st.markdown('###### 注册时间：:green[2025年10月20日11:19:34]|精神状态：✅正常')
    st.markdown('###### 当前教室：:green[实训楼204]|安全等级：:green[绝密]')

# 创建一个标题展示元素
    st.header("📊技能矩阵")

# 定义列布局，分成3列
    c1, c2, c3 = st.columns(3)
    c1.metric(label="C语言", value="95%", delta="2%")
    c2.metric(label="Python", value="90%", delta="-5%")
    c3.metric(label="Java", value="70%", delta="0", delta_color="off")

    st.markdown('#### streamlit课程进度')
    st.text('streamlit课程进度')


# 创建一个标题展示元素
    st.header("📔任务日志")

    import pandas as pd   # 导入Pandas并用pd代替
    import streamlit as st  # 导入Streamlit并用st代表它

# 定义数据,以便创建数据框
    data = {
         '日期':['2023-10-11','2023-10-16','2025-10-21'],
         '任务':['学生数字档案','课程管理系统','数据图表展示'],
         '状态':['✅完成','⏲进行中','❌︎未完成'],
         '难度':['⭐⭐','⭐','⭐⭐⭐'],
}
# 定义数据框所用的索引
    index = pd.Series(['0', '1', '2'], name=' ')
# 根据上面创建的data和index，创建数据框
    df = pd.DataFrame(data, index=index)

    st.subheader('默认显示')
    st.dataframe(df)

# 创建一个标题展示元素
    st.header("💻最新代码成果")

    st.subheader('Python代码块')
# 创建要显示的Python代码块的内容
    python_code = '''def hello():
        print("你好，Streamlit！")
'''
# 创建一个代码块，用于展示python_code的内容
# language为默认，即该代码块以Python语法高亮
    st.code(python_code)

# 分割线
    st.markdown('***')

# 动态信息流

    st.write("---")

    st.write("`>> SYSTEM MESSAGE:` 下一个任务目标已解锁...")

    st.write("`>> TARGET:` 课程管理系统")

    st.write("`>> COUNTDOWN:`", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))



elif page == "南宁美食地图":
    import streamlit as st
    import pandas as pd
    import numpy as np


# 餐厅数据
    restaurants_data = {
        "餐厅":['牛天宝','大福食堂','破烂泡泡','大山自助烤肉','苏格拉岛自助'],
        "类型":["自助餐", "中餐", "自助餐", "自助餐", "自助餐"],
        "评分":[4.6, 4.8, 4.7, 4.7, 4.5],
        "人均消费(元)": [70, 50,60,80, 90],
}    
    data = {
        "latitude":[22.832202,22.814752,22.816595,22.813986,22.813919],
        "longitude":[108.286485,108.320848,108.321551,108.321535,108.321484]
}
    df = pd.DataFrame(data)
    st.map(df)

    import streamlit as st
    import pandas as pd

 # 定义数据,以便创建数据框
    data = {
        '牛天宝':[200, 150, 180,180,120,130,150,120, 160,123,150, 200],
        '大福食堂':[120, 160, 123,150,200,190,160,160,150,180,180,200],
        '破烂泡泡':[110, 100, 160,190,160,160,150, 180,180,160,170,180],
        '大山自助烤肉':[150, 200, 230,200,190,180,180,200,180,160,170,160],
        '苏格拉岛自助':[120,240, 143,150, 200, 230,200,190,180,180,200,170],
}
# 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
# 定义数据框所用的新索引
    index = pd.Series(['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'], name='月份')
# 将新索引应用到数据框上
    df.index = index

#展示数据
    st.dataframe(df)
    st.table(df)

#折线图
    st.line_chart(df)
#柱状图
    st.bar_chart(df)

#准备地图坐标点数据
    map_data = {
        "latitude":[22.832202,22.814752,22.816595,22.813986,22.813919],
        "longitude":[108.286485,108.320848,108.321551,108.321535,108.321484]
}

    st.map(pd.DataFrame(map_data))


    import streamlit as st
    import pandas as pd

    crowd_data = pd.DataFrame({
        "时间":['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'],
        "牛天宝":[30,95,50,70,40,85,60,25,85,65,35,90],
        "大福食堂":[65,35,90,65,40,80,50,45,75,55,66,84],
        "破烂泡泡":[34,57,89,12,45,78,23,67,90,56,82,39],
        "大山自助烤肉":[47,83,19,62,95,31,76,24,58,13,69,40],
        "苏格拉岛自助":[28,91,55,17,74,36,80,42,66,35,59,88]
})

#使用data的数据创建数据帧dataFrame

    st.line_chart(crowd_data.set_index('时间'))



elif page == "动物图鉴":
    st.title("动物图鉴")
    st.set_page_config(page_title='动物园', page_icon='🐒')

# 图片对象数组
    images = [
        {
        'url':'https://www.thehappycatsite.com/wp-content/uploads/2020/12/What-does-it-mean-if-a-cat-winks-at-you-HC-long.jpg',
        'parm':'猫'
        },
        {
         'url': 'https://www.birds.cornell.edu/home/wp-content/uploads/2018/10/program-bps.jpg',
         'parm':'鸟'
        },
        {
          'url':'https://housing.com/news/wp-content/uploads/2023/07/Cute-dog-breeds-that-make-the-best-pets-f-686x400.jpg',
          'parm':'狗'
        },
        {
          'url':'https://n.sinaimg.cn/sinakd20113/179/w1290h1289/20230326/79b7-3d2a1863258979bbb1dd6ba371ae1a0e.jpg',
          'parm':'猫meme'
        },
        {
          'url':'https://v-huya-img2.msstatic.com/process/1745313478458/1055760708/99.jpg?x-oss-process=image/resize,limit_0,m_lfit,h_460/sharpen,80/format,jpg/interlace,1/quality,q_80',
          'parm':'danking'
        }
]

#将ind的值存储到streamlit的内存中，如果内存中没有ind，才要设置成0，否则不需要设置
    if 'ind' not in st.session_state:
        st.session_state['ind']=0


#define:定义
    def nextImg():
        st.session_state['ind']=(st.session_state['ind']+1)%len(images)
    def lastImg():
        st.session_state['ind']=(st.session_state['ind']-1)%len(images)

# st.image()总共两个参数，url：图片地址 caption:图片的备注
    st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])

#将一行分成两列
    c1,c2 = st.columns(2)

    with c1:
        #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
        st.button('上一张',on_click=lastImg,use_container_width=True)
    
    with c2:
        #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
        st.button('下一张',on_click=nextImg,use_container_width=True)

elif page == "音乐播放器":
    # 创建一个标题展示元素，内容是全中文的
    # 如不定义anchor参数，则无锚点
    st.title("🎧️简易音乐播放器")

    # 第一个普通文本展示元素，无工具提示
    st.text("使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

    # 数组
    images = [
            {
            'url':'https://music.163.com/song/media/outer/url?id=2526625.mp3',
            'author':'歌手：Deep Side',
            'photo':'https://p1.music.126.net/dUSiZ5ASRpWgaq9OTMtoDw==/860917604602698.jpg?param=250y250',
            'name':'booty music'
            },
            {
            'url':'https://music.163.com/song/media/outer/url?id=1842728629.mp3',
            'author':'歌手：郑润泽',
            'photo':'https://p1.music.126.net/-xMsNLpquZTmMZlIztTgHg==/109951165953469081.jpg?param=250y250',
            'name':'如果呢'
            },
            {
            'url':'https://music.163.com/song/media/outer/url?id=18638059.mp3',
            'author':'歌手：Justin Bieber',
            'photo':'https://p1.music.126.net/w-KG9LFj7Z2F9bjtlHG3JA==/109951165476414199.jpg?param=250y250',
            'name':'One Time'
            }
]

#将ind的值存储到streamlit的内存中，如果内存中没有ind，才要设置成0，否则不需要设置
    if 'ind' not in st.session_state:
        st.session_state['ind']=0


#define:定义
    def nextImg():
        st.session_state['ind']=(st.session_state['ind']+1)%len(images)
    def lastImg():
        st.session_state['ind']=(st.session_state['ind']-1)%len(images)


    b1,b2=st.columns([1,2])
    with b1:
# st.image()总共两个参数，url：图片地址 caption:图片的备注
       st.image(images[st.session_state['ind']]['photo'],caption=images[st.session_state['ind']]['name'])

    with b2:
       st.title(images[st.session_state['ind']]['name'])
       st.header(images[st.session_state['ind']]['author'])
   
   #将一行分成两列
       c1,c2 = st.columns(2)

       with c1:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
        st.button('上一首',on_click=lastImg,use_container_width=True)
    
       with c2:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
        st.button('下一首',on_click=nextImg,use_container_width=True)

    st.audio(images[st.session_state['ind']]['url'])

elif page == "视频播放器":
    # 创建一个标题展示元素，内容是全中文的
    # 如不定义anchor参数，则无锚点
    st.title("📺︎简易danking播放器")

    st.set_page_config(page_title='视频', page_icon='📺︎')

    # 读取视频数据
    video_url = [
        {
       'url':'https://upos-sz-estghw.bilivideo.com/upgcxcode/73/18/32384681873/32384681873-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&gen=playurlv3&deadline=1761303356&mid=0&uipk=5&oi=2672555743&os=estghw&og=hw&trid=cb7e064860274d17aaa41986b8a5073h&nbs=1&upsig=66171c5af2c1f5bf3313ae55a4ce8c9e&uparams=e,platform,gen,deadline,mid,uipk,oi,os,og,trid,nbs&bvc=vod&nettype=0&bw=329593&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
       'title':'danking',
       'number':'1'
       },
        {
       'url':'https://upos-sz-estgcos.bilivideo.com/upgcxcode/32/16/1503841632/1503841632-1-192.mp4?e=ig8euxZM2rNcNbNgnWdVhwdlhbNHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=cos&uipk=5&platform=html5&oi=1782024106&nbs=1&trid=efa9da65cdf04612871efecb2cec25eh&deadline=1761303280&mid=0&gen=playurlv3&os=estgcos&upsig=6f58a9ce873193a162dae190a4aeb997&uparams=e,og,uipk,platform,oi,nbs,trid,deadline,mid,gen,os&bvc=vod&nettype=0&bw=1843750&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
       'title':'乌兰巴托',
      'number':'2'
       },
        {
       'url':'https://upos-sz-estgcos.bilivideo.com/upgcxcode/19/77/28647557719/28647557719-1-192.mp4?e=ig8euxZM2rNcNbNVnWdVhwdlhbdHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=1782024106&os=estgcos&trid=9e12356f2f814775b1a288d92adbe0fh&nbs=1&uipk=5&platform=html5&mid=0&gen=playurlv3&og=cos&deadline=1761303429&upsig=cffe660fa75b1febe6cd6f713390befe&uparams=e,oi,os,trid,nbs,uipk,platform,mid,gen,og,deadline&bvc=vod&nettype=0&bw=1677456&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
       'title':'“我会装作不在乎 直到真正不在乎”',
       'number':'3'
         }
]

    #将ind的值存储到streamlit的内存中，如果内存中没有ind，才要设置成0，否则不需要设置
    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    st.title(video_url[st.session_state['ind']]['title']+'-第'+video_url[st.session_state['ind']]['number']+'集')
    st.video(video_url[st.session_state['ind']]['url'])


    #将一行分成三列
    c1,c2,c3 = st.columns(3)

    def play(arg):
             #点击哪个按钮，就播放第几集
             #将传递过来的值，赋值给内存中的ind
             st.session_state['ind']=int(arg)

    for i in range(len(video_url)):
        st.button('第' + str(i+1) + '集',use_container_width=True,on_click=play,args=([i]))

else:
    from datetime import datetime, timedelta
    from datetime import datetime, time

    st.set_page_config(page_title="个人简历生成器", page_icon="", layout="wide")
    st.header("个人信息表单")
    st.text('使用stream创建您的个性化简历')

    c1,c2 =st.columns([1,2])
    with c1:
        st.subheader("个人信息表单")
        st.markdown('***')


        name = st.text_input('姓名', autocomplete='name')

        position = st.text_input('职位', autocomplete='position')

        phone = st.text_input('电话', autocomplete='phone')

        postbox = st.text_input('邮箱', autocomplete='postbox')


    # value参数默认为None，初始状态为今天
        date = st.date_input("出生日期", value=None)

        st.write('性别')
    # 设置标签为“hidden”
    # 设置水平排列
        gender = st.radio(
        '你的性别是什么？',
        ['男', '女', '其他'],
        horizontal=True,
        label_visibility='hidden'
)
        st.write('学历')
        education = st.selectbox(
        '选择学历',
        ['小学', '初中','中专','高中','大专','本科','研究生','博士'],
        label_visibility='collapsed'
)
        st.write('语言能力')
        # 自定义format_func函数
        def my_format_func(option):
            return f'{option}'
        options = st.multiselect(
            '语言能力',
            ['英语', '法语','德语','日语','西班牙语','意大利语','其他'],
            format_func=my_format_func,
            label_visibility='hidden'
            )

        # 自定义format_func函数
        def my_format_func(option):
            return f'{option}'
        st.write('技能（可多选）')
        options_2 = st.multiselect(
            '选择你的技能',
            ['圈米', 'AWP的使用'],
             format_func=my_format_func,
            label_visibility='hidden'
            )

        age = st.slider('工作经验（年）', 0, 30, 3)

        values = st.slider(
            '选择一组范围',
            3000, 50000, (10000, 20000))

        gr = st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...',
                          height=200, max_chars=200)

        w2 = st.time_input("每日最佳联系时间段", time(8, 45))

        photo = st.file_uploader('上传你的照片')
        if photo is not None:
            bytes_data=photo.getvalue()

    with c2:
        st.subheader('简历实时预览')
        st.markdown('***')
        b1,b2 =st.columns(2)
        with b1:
            st.image(bytes_data)
            st.write('姓名:',name)
            st.write('职位:',position)
            st.write('电话:',phone)
            st.write('邮箱:',postbox)
            st.write('出生日期:',date)
        with b2:
            st.write('性别:',gender)
            st.write('学历:',education)
            st.write('期望薪资:',values)
            st.write('工作经验:',age)
            st.write('最佳联系时间:',w2 )
            st.write('语言能力:',options)
        st.markdown('***')
        st.write('个人简介',gr)
        st.write('专业技能',options_2)
    
