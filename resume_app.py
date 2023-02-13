import streamlit as st
# from streamlit_option_menu import option_menu


# with st.sidebar:
#     selected = option_menu('Menu',

#                            ['Resume',
#                             'Photos'],

#                            default_index=0
#                            )
# if (selected == 'Resume'):

import pandas as pd
from PIL import Image
import os


st.markdown("<h3 style='text-align: center; color: white; font-size: 40px; font-weight: 900; background-color: black;'>JAYESH BHAWSAR</h3>", unsafe_allow_html=True)
st.write('')
st.write('')
st.write('')
st.write('')

st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Address: </h4>",
            unsafe_allow_html=True)
st.write("99, Shyam Nagar Annex A, Near MR10 Square, Sukhliya, INDORE, 452001")
st.write('')
st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Email: </h4>",
            unsafe_allow_html=True)
st.write("mady000745@gmail.com")
st.write('')
st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Contact: </h4>",
            unsafe_allow_html=True)
st.write("+917057053741")
st.write('')
st.write('')
st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Professional Summary:</h4>",
            unsafe_allow_html=True)
st.markdown("""<h6 style='color: black;'>Python programming professional certified in Python and Django from Ethans Tech. (Pune), currently working as Junior Software Engineer in VKAPS IT Solutions Pvt. Ltd INDORE, MP.</h6>""", unsafe_allow_html=True)

st.markdown("Well versed in NumPy, Pandas, Well versed in Object Oriented Programming (OOPs).")

st.markdown("Able to develop and designed API's with FastAPI Framework.")

st.markdown("Basics of HTML5, CSS3 and Bootstrap.")

st.markdown("Computer Knowledge: Windows 7-8, Windows 10, Linux(Ubuntu), MS Office (Excel, Word, PowerPoint).")

st.markdown("Web Scraping with BeautifulSoup and Selenium.")

st.markdown("Machine Learning")

st.markdown("Good communication skills and attention to details.")
st.write('')
st.write('')
st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Education & Certification: </h4>",
            unsafe_allow_html=True)

st.write('')

col_1, col_2 = st.columns(2)
with col_1:
    st.write("<h5 style='text-align: left; color: black;'>B.Tech in Mechanical Engineering</h5>",
            unsafe_allow_html=True)
    st.write('Synergy Institute of Technology, Dewas, MP')
    
with col_2:
    st.write("<h5 style='text-align: right; color: black;'>2019 - 2022</h5>",
            unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')

with col_1:
    st.write("<h5 style='text-align: left; color: black;'>Python Certification: </h5>",
            unsafe_allow_html=True)
    st.write('Ethans Tech. Kharadi - Pune, MH')
with col_2:
    st.write("<h5 style='text-align: right; color: black;'>Dec 2020 - Jan 2020</h5>",
            unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')

with col_1:
    st.write("<h5 style='text-align: left; color: black;'>Internship in Django</h5>",
            unsafe_allow_html=True)
    st.write('CodeBetter - Indore, MP')
with col_2:
    st.write("<h5 style='text-align: right; color: black;'>Mar 2020 - Apr 2020</h5>",
            unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')

with col_1:
    st.write("<h5 style='text-align: left; color: black;'>Post Diploma (Tool & Die Mfg.)</h5>",
            unsafe_allow_html=True)
    st.write('Indo-German Tool Room - Aurangabad, MH (AICTE Delhi)')
with col_2:
    st.write("<h5 style='text-align: right; color: black;'>2016 - 2017</h5>",
            unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')

with col_1:
    st.write("<h5 style='text-align: left; color: black;'>Advance Diploma (Tool & Die Making)</h5>",
            unsafe_allow_html=True)
    st.write('Indo-German Tool Room - Indore, MP (AICTE Delhi & RGTU, Bhopal)')
with col_2:
    st.write("<h5 style='text-align: right; color: black;'>2010 - 2014</h5>",
            unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')


st.write('')
st.write('')

st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Professional Experience: </h4>",
            unsafe_allow_html=True)

col_1, col_2 = st.columns(2)
with col_1:
    st.write("<h5 style='text-align: left; color: black;'>VKAPS IT Solutions Pvt. Ltd INDORE, MP</h5>",
            unsafe_allow_html=True)
    st.write('Junior Software Engineer')
    
with col_2:
    st.write("<h5 style='text-align: right; color: black;'>Oct 2021 - Present</h5>",
            unsafe_allow_html=True)


st.write("Working as Python/Django developer.")

st.write("Working on core python scripts for web scraping.")
st.write("Web Scraping with BeautifulSoup and Selenium of Amazon, Flipkart, selectfashion.uk, serco, Hikrupet etc.")
st.write('Developed a project of Machine Learning task such as PDF/Image processing in Streamlit Web Framework.')
st.write("Developed the script for web scraping the 'consumeraffairs.com & teacherspayteachers.com' and fetched the desired details as per Client.")
st.write("Developed the ML projects for predictions such as 'Diabetes, Heart-Disease, Parkinsons & Heart-Stroke' as Internal Projects in Streamlit Web Framework and FastAPI")


st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Additional Experience: </h4>",
            unsafe_allow_html=True)



col_1, col_2 = st.columns(2)
with col_1:
    st.write("<h5 style='text-align: left; color: black;'>Pitti Engineering Ltd, Hyderabad, Telangana</h5>",
            unsafe_allow_html=True)
    st.write('Sr. Supervisor - Production')
    
with col_2:
    st.write("<h5 style='text-align: right; color: black;'>Aug 2020 - Dec 2020</h5>",
            unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')

with col_1:
    st.write("<h5 style='text-align: left; color: black;'>PMT Machines Ltd. - Pune, MH</h5>",
            unsafe_allow_html=True)
    st.write('Jr. Engineer - Production')
with col_2:
    st.write("<h5 style='text-align: right; color: black;'>Oct 2017 - Aug 2020</h5>",
            unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')

with col_1:
    st.write("<h5 style='text-align: left; color: black;'>Engeetech Engineering - Indore, MP</h5>",
            unsafe_allow_html=True)
    st.write('Jr. Engineer - Quality Control')
with col_2:
    st.write("<h5 style='text-align: right; color: black;'>Jul 2014 - Sep 2016</h5>",
            unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.write('')











# if (selected == 'Photos'):
#     from PIL import Image
#     import os
#     root = os.path.dirname(__file__)
#     img1 = Image.open(root + "/media/images/1.jpg")

#     col_1, col_2 = st.columns(2)
#     with col_1:
#         img11 = st.image(img1, use_column_width=True)
#     with col_2:
#         img22 = st.image(img2, use_column_width=True)


hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
