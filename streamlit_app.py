import streamlit as st
from PIL import Image
import base64

# Function to create a custom Streamlit button with a link
def st_button(button_text, url, tooltip_text, icon_size):
    button_html = f"""<a href="{url}" target="_blank" style="text-decoration: none;">
    <button style="background-color: #007BFF; border: none; color: white; padding: 10px 20px; text-align: center;
    text-decoration: none; display: block; font-size: 16px; margin: 4px auto; cursor: pointer; border-radius: 12px; width: 100%;">
    {button_text}
    </button></a>"""
    st.markdown(button_html, unsafe_allow_html=True)

# Function to convert an image to base64
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Light and Dark Mode Switch
def render_mode_switch():
    mode_switch = """
    <div style="text-align: right;">
        <label class="switch">
          <input type="checkbox" id="mode-switch" onchange="toggleMode()">
          <span class="slider round"></span>
        </label>
    </div>
    <style>
    .switch {
      position: relative;
      display: inline-block;
      width: 60px;
      height: 34px;
    }

    .switch input { 
      opacity: 0;
      width: 0;
      height: 0;
    }

    .slider {
      position: absolute;
      cursor: pointer;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: #ccc;
      -webkit-transition: .4s;
      transition: .4s;
    }

    .slider:before {
      position: absolute;
      content: "";
      height: 26px;
      width: 26px;
      left: 4px;
      bottom: 4px;
      background-color: white;
      -webkit-transition: .4s;
      transition: .4s;
    }

    input:checked + .slider {
      background-color: #2196F3;
    }

    input:focus + .slider {
      box-shadow: 0 0 1px #2196F3;
    }

    input:checked + .slider:before {
      -webkit-transform: translateX(26px);
      -ms-transform: translateX(26px);
      transform: translateX(26px);
    }

    .slider.round {
      border-radius: 34px;
    }

    .slider.round:before {
      border-radius: 50%;
    }
    </style>
    <script>
    function toggleMode() {
        var checkBox = document.getElementById("mode-switch");
        if (checkBox.checked == true){
            document.body.style.backgroundColor = "black";
            document.body.style.color = "white";
        } else {
            document.body.style.backgroundColor = "white";
            document.body.style.color = "black";
        }
    }
    </script>
    """
    st.markdown(mode_switch, unsafe_allow_html=True)

# Call the function to render the mode switch
render_mode_switch()

# Display a GitHub stars badge using markdown
st.markdown("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)", unsafe_allow_html=True)

# Displaying an image in the center column
image_path = 'dp.png'
image_base64 = get_image_base64(image_path)
image_html = f"""<div style="text-align: center;">
<img src="data:image/png;base64,{image_base64}" style="border-radius: 50%; width: 100px; height: 100px; object-fit: cover;" />
</div>"""

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(image_html, unsafe_allow_html=True)

st.header('Sulaiman.')

st.info('A proficient expert leveraging advanced AI tools like ChatGPT to offer a variety of online services')

icon_size = 20

# Updated st_button function calls
st_button('Follow me on Twitter', 'https://twitter.com/baloblack/', 'Follow me on Twitter', icon_size)
st_button('Follow me on LinkedIn', 'https://www.linkedin.com/in/sulaiman-balogun-208557175/', 'Follow me on LinkedIn', icon_size)
st_button('Buy me a Coffee', 'https://www.buymeacoffee.com/baloblack/', 'Support me on Buy me a Coffee', icon_size)

st.info('Check out my GPT-powered applications')
st_button('Crafting AI-Driven Content ✍️🤖 Revolutionizing Your Brands.', 'https://chat.openai.com/g/g-bFeD4GzK7-copywritegpt-crafting-ai-driven-content/', 'Explore Copywrite GPT', icon_size)
st_button('Unraveling Crypto Trends 📊💡 Personalized Bitcoin sentiment analysis guide.', 'https://chat.openai.com/g/g-4AWWN6mXB-bitcoin-analystgpt-unraveling-crypto-trends/', 'Bitcoin AnalystGPT', icon_size)
