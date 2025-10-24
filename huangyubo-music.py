import streamlit as st

st.set_page_config(page_title='音乐播放器', page_icon='🎵', layout='wide')

# 图片对象数组
music = [
    {
        'url': 'https://music.163.com/song/media/outer/url?id=1993462019.mp3',
        'name': '相遇在广袤无垠的宇宙',
        'photo': 'https://p2.music.126.net/cjU3PWyao4ovp48-UXFQlw==/109951168309686632.jpg?param=130y130',
        'author': '黄誉博'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=2083464817.mp3',
        'name': '轻轻把我放在这儿',
        'photo': 'https://https://p2.music.126.net/sr8qe3f2huX_9b7ES0dbUw==/109951168926347263.jpg?param=130y130',
        'author': '黄誉博'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=1937944392.mp3',
        'name': '是圣人吗？不谈恋爱',
        'photo': 'https://p1.music.126.net/cjU3PWyao4ovp48-UXFQlw==/109951168309686632.jpg?param=130y130',
        'author': '黄誉博'
    }
]


if 'ind' not in st.session_state:
    st.session_state['ind'] = 0


def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music)

def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(music)


a1, a2 = st.columns([1, 2])
with a1:
    st.image(music[st.session_state['ind']]['photo'])
with a2:
    st.title(music[st.session_state['ind']]['name'])
    st.audio(music[st.session_state['ind']]['url'], autoplay=True)


col1, col2 = st.columns(2)
with col1:
    st.button('上一首', on_click=prevImg)
with col2:
    st.button('下一首', on_click=nextImg)
