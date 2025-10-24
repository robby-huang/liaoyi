import streamlit as st
st.set_page_config(page_title='视频网站',page_icon='📽')

# 视频地址
video_url = [
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/56/88/1469978856/1469978856-1-192.mp4?e=ig8euxZM2rNcNbNzhbdVhwdlhbhghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&nbs=1&gen=playurlv3&og=ali&oi=771356656&deadline=1761303848&uipk=5&os=cosovbv&trid=608ac0d0033744489936dec5e9e72c8h&mid=0&upsig=24b066b3e9913d6dcc5bfdf0595d5fcc&uparams=e,platform,nbs,gen,og,oi,deadline,uipk,os,trid,mid&bvc=vod&nettype=0&bw=1870110&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
        'title': '蓝豆合体',
        'episode': '1'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/61/59/30524245961/30524245961-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&platform=html5&uipk=5&mid=0&deadline=1761303903&trid=977267871c16422293355fb7147a2fbh&oi=771356656&gen=playurlv3&os=cosovbv&og=cos&upsig=1ffe89c9e1001795e0a218f5aa5e3f59&uparams=e,nbs,platform,uipk,mid,deadline,trid,oi,gen,os,og&bvc=vod&nettype=0&bw=753314&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
        'title': '霎那闪烁照亮银河',
        'episode': '2'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/66/58/816175866/816175866-1-208.mp4?e=ig8euxZM2rNcNbhjhwdVhwdlhzTVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=771356656&gen=playurlv3&os=cosovbv&nbs=1&platform=html5&trid=4d053183e63247b390741a33e4fe790h&deadline=1761303948&og=hw&uipk=5&mid=0&upsig=0aae2b548cc6d1ee38928eb454ab89ca&uparams=e,oi,gen,os,nbs,platform,trid,deadline,og,uipk,mid&bvc=vod&nettype=0&bw=2882093&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
        'title': '最初的梦想',
        'episode': '3'
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
    
st.title(video_url[st.session_state['ind']]['title'] + '-第' + video_url[st.session_state['ind']]['episode'] + '集')
st.video(video_url[st.session_state['ind']]['url'])

c1, c2, c3 = st.columns(3)

def play(arg):
    # 将传递过来的值，赋值给内存中的ind
    st.session_state['ind'] = int(arg)

for i in range(len(video_url)):
    st.button('第' + str(i + 1) + '集', use_container_width=True, on_click=play, args=([i]))
