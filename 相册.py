import streamlit as st
st.set_page_config(page_title='黄誉博', page_icon='👦')

images = [
    {
       'url':'https://c-ssl.duitang.com/uploads/blog/202405/09/2YSEwM4GT6Xal1D.jpeg',
        'parm':'发光誉博'},
    {
        'url':'https://img.alicdn.com/imgextra/i4/2251059038/O1CN01zbF8Sz2GdSYCnZUtq_!!2251059038.jpg',
        'parm':'唱歌誉博'
    },
    {
        'url':'https://c-ssl.dtstatic.com/uploads/blog/202405/09/n6S0D2wYT92YqJL.thumb.1000_0.png',
        'parm':'黑衣黄誉博'
    }
  ]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0


def nextImg():
    st.session_state['ind'] = (st.session_state['ind']+1) % len(images)

    st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['parm'])
c1,c2 = st.columns(2)

with c1:
    st.button('上一张',on_click=nextImg,use_container_width=True)

with c2:
    st.button('下一张',on_click=nextImg,use_container_width=True)

