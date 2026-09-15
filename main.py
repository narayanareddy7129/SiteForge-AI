import streamlit as st 
from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI

# environment variable setup
from dotenv import load_dotenv

load_dotenv() 

import zipfile
import os 
# os.environ['GEMINI_API_KEY'] = os.getenv('gemini') 
api_key = st.secrets['GEMINI_API_KEY']

# streamlit 
st.set_page_config(page_title='AI Web Creation',page_icon='🪁')

st.title('AI AUTOMATION WEBSITE CREATION') 

prompt = st.text_area('Write your idea to create a website') 

if st.button('Generate'):
    message = [('system',"""You are an expert frontend web developer and UI/UX designer.

Your task is to generate complete, production-ready frontend websites based on the user's requirements.

Rules:
1. Generate ONLY HTML, CSS, and JavaScript.
2. Do not use React, Vue, Angular, TypeScript, or any backend code.
3. Return a complete, self-contained website that can run directly in a browser.
4. Use semantic HTML5, modern CSS, and clean vanilla JavaScript.
5. Make the website fully responsive for desktop, tablet, and mobile.
6. Create a modern, visually appealing UI with good spacing, typography, colors, animations, and hover effects.
7. Implement all requested interactions and functionality using vanilla JavaScript.
8. Use external resources such as Google Fonts or CDN libraries only when necessary.
9. Do not explain the code or add unnecessary text.
10. The output should be in the below format:
     --html--
     [htmlcode]
     --html--

     --css--
     [csscode]
     --css--

     --js--
     [javascriptcode]
     --js--
      """)]

    message.append(('human',prompt))

    model=ChatGoogleGenerativeAI(model='gemini-3.5-flash',google_api_key=api_key)

    response = model.invoke(message) 

    with open('index.html','w') as file:
        file.write(response.content[0]['text'].split('--html--')[1])

    with open('style.css','w') as file:
        file.write(response.content[0]['text'].split('--css--')[1])

    with open('script.js','w') as file:
        file.write(response.content[0]['text'].split('--js--')[1])

    with zipfile.ZipFile('portfolio.zip','w') as zip:
        zip.write('index.html')
        zip.write('style.css')
        zip.write('script.js')

    st.download_button('click to download',data=open('portfolio.zip','rb'),file_name='portfolio.zip')


    st.write('success')


