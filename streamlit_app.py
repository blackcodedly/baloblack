import streamlit as st
from PIL import Image
import base64

def st_button(button_text, url, tooltip_text, icon_size):
    button_html = f"""<a href="{url}" target="_blank" style="text-decoration: none;">
    <button style="background-color: #007BFF; border: none; color: white; padding: 10px 20px; text-align: center;
    text-decoration: none; display: block; font-size: 16px; margin: 4px auto; cursor: pointer; border-radius: 12px; width: 100%;">
    {button_text}
    </button></a>"""
    st.markdown(button_html, unsafe_allow_html=True)

# Display a GitHub stars badge using markdown
st.markdown("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)", unsafe_allow_html=True)

# Method to convert image to base64 (optional, use if displaying local images through HTML)
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Displaying an image in the center column, making it round and smaller
image_path = 'dp.png'  # Path to your image
image_base64 = get_image_base64(image_path)  # Convert image to base64, use if needed
image_html = f"""<div style="text-align: center;">
<img src="data:image/png;base64,{image_base64}" style="border-radius: 50%; width: 100px; height: 100px; object-fit: cover;" />
</div>"""

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(image_html, unsafe_allow_html=True)  # Use this line if using the base64 method

st.header('Sulaiman.')

st.info('A proficient expert leveraging advanced AI tools like ChatGPT to offer a variety of online services')

icon_size = 20

# Updated st_button function calls
st_button('Follow me on Twitter', 'https://twitter.com/baloblack/', 'Follow me on Twitter', icon_size)
st_button('Follow me on LinkedIn', 'https://www.linkedin.com/in/sulaiman-balogun-208557175/', 'Follow me on LinkedIn', icon_size)
st_button('Buy me a Coffee', 'https://www.buymeacoffee.com/baloblack/', 'Support me on Buy me a Coffee', icon_size)

st.info('Check out my GPT-powered applications')
st_button('Crafting AI-Driven Content ✍️🤖 Revolutionizing Your Brands.', 'https://chat.openai.com/g/g-bFeD4GzK7-copywritegpt-crafting-ai-driven-content/', 'Explore Copywrite GPT', icon_size)
