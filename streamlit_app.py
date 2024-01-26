import streamlit as st
from PIL import Image

def st_button(button_text, url, tooltip_text, icon_size):
    # Updated button HTML to change the background color to blue and ensure the text is centered
    button_html = f"""<a href="{url}" target="_blank" style="text-decoration: none;">
    <button style="background-color: #007BFF; border: none; color: white; padding: 10px 20px; text-align: center;
    text-decoration: none; display: block; font-size: 16px; margin: 4px auto; cursor: pointer; border-radius: 12px; width: 100%;">
    {button_text}
    </button></a>"""
    st.markdown(button_html, unsafe_allow_html=True)

# Display a GitHub stars badge using markdown
st.markdown("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)", unsafe_allow_html=True)

# Displaying an image in the center column
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(Image.open('dp.png'))

st.header('Sulaiman.')

st.info('A proficient expert leveraging advanced AI tools like ChatGPT to offer a variety of online services')

icon_size = 20  # This no longer affects padding directly due to CSS adjustments

# Updated st_button function calls
st_button('Follow me on Twitter', 'https://twitter.com/baloblack/', 'Follow me on Twitter', icon_size)
st_button('Follow me on LinkedIn', 'https://www.linkedin.com/in/sulaiman-balogun-208557175/', 'Follow me on LinkedIn', icon_size)
st_button('Buy me a Coffee', 'https://www.buymeacoffee.com/baloblack/', 'Support me on Buy me a Coffee', icon_size)

st.info('Check out my GPT-powered applications')
st_button('Crafting AI-Driven Content ✍️🤖 Revolutionizing Your Brands.', 'https://chat.openai.com/g/g-bFeD4GzK7-copywritegpt-crafting-ai-driven-content/', 'Explore Copywrite GPT', icon_size)
