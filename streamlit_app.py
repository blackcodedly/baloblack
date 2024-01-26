import streamlit as st
from PIL import Image

# Custom function to create and display buttons in Streamlit using Markdown and HTML
def st_button(button_text, url, tooltip_text, icon_size):
    button_html = f"""<a href="{url}" target="_blank" style="text-decoration: none;">
    <button style="background-color: #4CAF50; border: none; color: white; padding: 10px {icon_size}px; text-align: center;
    text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 12px;">
    {button_text} <span style="font-size: {icon_size}px;">✍️🤖</span>
    </button></a>"""
    st.markdown(button_html, unsafe_allow_html=True)

# Assuming load_css properly injects custom CSS into your Streamlit app
# load_css() # Uncomment this line if your load_css function is defined elsewhere

# Display a GitHub stars badge using markdown
st.markdown("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)", unsafe_allow_html=True)

# Displaying an image in the center column
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(Image.open('dp.png'))

st.header('Sulaiman.')

st.info('A proficient expert leveraging advanced AI tools like ChatGPT to offer a variety of online services')

icon_size = 20  # Adjusts padding around the button text

# Replacing previous st_button function calls with the updated implementation
st_button('Follow me on Twitter', 'https://twitter.com/baloblack/', 'Follow me on Twitter', icon_size)
st_button('Follow me on LinkedIn', 'https://www.linkedin.com/in/sulaiman-balogun-208557175/', 'Follow me on LinkedIn', icon_size)
st_button('Buy me a Coffee', 'https://www.buymeacoffee.com/baloblack/', 'Support me on Buy me a Coffee', icon_size)

st.info('Check out my GPT-powered applications')
st_button('Crafting AI-Driven Content ✍️🤖 Revolutionizing Your Brands.', 'https://chat.openai.com/g/g-bFeD4GzK7-copywritegpt-crafting-ai-driven-content/', 'Explore Copywrite GPT', icon_size)
