import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

# Assuming load_css properly injects custom CSS into your Streamlit app
load_css()

# Display a GitHub stars badge using markdown
st.markdown("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)", unsafe_allow_html=True)

# Displaying an image in the center column
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(Image.open('dp.png'))

st.header('Sulaiman.')

st.info('A proficient expert leveraging advanced AI tools like ChatGPT to offer a variety of online services')

# Assuming icon_size is used within st_button to control the size of icons (this might need adjustment)
icon_size = 20

# Function calls to st_button - Ensure that st_button is correctly handling these parameters
st_button('twitter', 'https://twitter.com/baloblack/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/sulaiman-balogun-208557175//', 'Follow me on LinkedIn', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/baloblack/', 'Buy me a Coffee', icon_size)

st.info('Check out my GPT-powered applications')
st_button('Copywrite GPT', 'https://chat.openai.com/g/g-bFeD4GzK7-copywritegpt-crafting-ai-driven-content/', 'Crafting AI-Driven Content ✍️🤖 Revolutionizing Your Brands.', icon_size)

