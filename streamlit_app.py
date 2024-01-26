import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Sulaiman.')

st.info('A proficient expert leveraging advanced AI tools like ChatGPT to offer a variety of online services')

icon_size = 20

st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/baloblack/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/sulaiman-balogun-208557175//', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/baloblack/', 'Buy me a Coffee', icon_size)
