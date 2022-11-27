import streamlit as st
import requests
st.title('Toonify AI App')
#image=st.camera_input('Click Your Image')
#image=st.file_uploader('Upload Your Image')
word_toimage=st.text_input('Please Enter a Word:')
#st.write(type(image))
def image_generator(word_toimage):
    r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': word_toimage,
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
    #st.write(r.json())
    return(r.json()['output_url'])
if st.button('Image'):
    cartoon=image_generator(word_toimage)
    st.image(cartoon)
