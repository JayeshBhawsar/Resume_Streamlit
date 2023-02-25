import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", 
                           ["LinkedIn", 'Settings'],
                           icons=['house', 'gear'], 
                           menu_icon="cast", 
                           default_index=0)

st.markdown("<h3 style='text-align: center; color: white; font-size: 40px; font-weight: 900; background-color: black;'>JAYESH BHAWSAR</h3>", unsafe_allow_html=True)
st.write('')
st.write('')
st.write('')
st.write('')

components.iframe("https://www.linkedin.com/in/jayesh-bhawsar-460b4a13a/")

st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Address: </h4>",
            unsafe_allow_html=True)
st.write("199, Shyam Nagar Annex A, Near MR10 Square, Sukhliya, INDORE, 452001")
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

st.write("<h5 style='text-align: left; color: black;'>B.Tech in Mechanical Engineering (2019 - 2022)</h5>",
            unsafe_allow_html=True)
st.write('Synergy Institute of Technology, Dewas, MP')
    
st.write('')
st.write('')
st.write('')


st.write("<h5 style='text-align: left; color: black;'>Python Certification (Dec 2020 - Jan 2020) </h5>",
            unsafe_allow_html=True)
st.write('Ethans Tech. Kharadi - Pune, MH')

st.write('')
st.write('')
st.write('')


st.write("<h5 style='text-align: left; color: black;'>Internship in Django (Mar 2020 - Apr 2020)</h5>",
            unsafe_allow_html=True)
st.write('CodeBetter - Indore, MP')

st.write('')
st.write('')
st.write('')


st.write("<h5 style='text-align: left; color: black;'>Post Diploma in Tool & Die Mfg. (2016 - 2017)</h5>",
            unsafe_allow_html=True)
st.write('Indo-German Tool Room - Aurangabad, MH (AICTE Delhi)')

st.write('')
st.write('')
st.write('')


st.write("<h5 style='text-align: left; color: black;'>Advance Diploma in Tool & Die Making 2010 - 2014 </h5>",
            unsafe_allow_html=True)
st.write('Indo-German Tool Room - Indore, MP (AICTE Delhi & RGTU, Bhopal)')

st.write('')
st.write('')
st.write('')


st.write('')
st.write('')

st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Professional Experience: </h4>",
            unsafe_allow_html=True)



st.write("<h5 style='text-align: left; color: black;'>VKAPS IT Solutions Pvt. Ltd INDORE, MP (Oct 2021 - Present)</h5>",
            unsafe_allow_html=True)
st.write('Junior Software Engineer')
    

st.write('')


st.write("Working as Python/Django developer.")
st.write("Working on core python scripts for web scraping.")
st.write("Web Scraping with BeautifulSoup and Selenium of Amazon, Flipkart, selectfashion.uk, serco, Hikrupet etc.")
st.write('Developed a project of Machine Learning task such as PDF/Image processing in Streamlit Web Framework.')
st.write("Developed the script for web scraping the 'consumeraffairs.com & teacherspayteachers.com' and fetched the desired details as per Client. And also created the web app for scrapping")
st.write("Developed the ML projects for predictions such as 'Diabetes, Heart-Disease, Parkinsons & Heart-Stroke' as Internal Projects in Streamlit Web Framework and FastAPI")
st.write("Developed the OpenAI project where users can generate the N number of Multiple Choice Questions and their answers by selecting the options provided in the menu. Also, can download it as a CSV file.")


st.markdown("<h4 style='text-align: left; font-weight: 900; color: black;'>Additional Experience: </h4>",
            unsafe_allow_html=True)





st.write("<h5 style='text-align: left; color: black;'>Pitti Engineering Ltd, Hyderabad, Telangana (Aug 2020 - Dec 2020)</h5>",
            unsafe_allow_html=True)
st.write('Sr. Supervisor - Production')

st.write('')
st.write('')
st.write('')


st.write("<h5 style='text-align: left; color: black;'>PMT Machines Ltd. - Pune, MH (Oct 2017 - Aug 2020)</h5>",
            unsafe_allow_html=True)
st.write('Jr. Engineer - Production')

st.write('')
st.write('')
st.write('')


st.write("<h5 style='text-align: left; color: black;'>Engeetech Engineering - Indore, MP (Jul 2014 - Sep 2016)</h5>",
            unsafe_allow_html=True)
st.write('Jr. Engineer - Quality Control')

st.write('')
st.write('')
st.write('')


hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
