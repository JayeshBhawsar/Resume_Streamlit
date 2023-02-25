import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", 
                           
                           ["LinkedIn", 'Settings'],
 
                           default_index=0)
    if (selected == "LinkedIn"):
        components.html('''<div class="feed-identity-module artdeco-card overflow-hidden mb2">
<!---->
  <div class="feed-identity-module__actor-meta break-words">
    <div class="feed-identity-module__member-bg-image
        feed-identity-module__default-bg" style="">
<!---->    </div>

    <a href="/in/jayesh-bhawsar-460b4a13a/" id="ember157" class="ember-view block">
      <div>
        <img width="64" src="https://media.licdn.com/dms/image/C5603AQGiYf_32NaLow/profile-displayphoto-shrink_100_100/0/1628322195569?e=1682553600&amp;v=beta&amp;t=mzW8X8ZiUaz14ppn_cIWdesfSRe0uI2cBXVv9jaTlbY" loading="lazy" height="64" alt="Photo of JAYESH BHAWSAR" id="ember158" class="feed-identity-module__member-photo EntityPhoto-circle-5 lazy-image ember-view">
      </div>
      <div class="t-16 t-black t-bold">
          JAYESH BHAWSAR
      </div>
    </a>

      <p class="identity-headline t-12 t-black--light t-normal mt1">
        Python Developer
      </p>
      </div>

<!---->
      <div class="feed-identity-module__widgets pv3">
        
<div class="entity-list-wrapper ">
  <ul class="entity-list row">
      <li class="feed-identity-module__entity-list-item entity-list-item">
          <a href="/mynetwork/" id="ember159" class="ember-view full-width">
    <div class="display-flex align-items-baseline">
  <div class="text-align-left">
      <div id="ember160" class="ember-view t-12 t-black--light t-bold mr2">
<span>Connections</span>  </div>

        <div id="ember161" class="ember-view t-12 t-black t-bold">
<span>Grow your network</span>  </div>

      </div>
  <div class="feed-identity-widget-item__icon-stat t-12 t-black t-bold flex-1">
      <span class="feed-identity-widget-item__stat">
        75
      </span>
  </div>
</div>
  </a>

      </li>
      <li class="feed-identity-module__entity-list-item entity-list-item">
          <a href="/me/profile-views/" id="ember162" class="ember-view full-width">
    <div class="display-flex align-items-baseline">
  <div class="text-align-left">
      <div id="ember163" class="ember-view t-12 t-black--light t-bold mr2">
<span>Who's viewed your profile</span>  </div>

<!---->  </div>
  <div class="feed-identity-widget-item__icon-stat t-12 t-black t-bold flex-1">
      <span class="feed-identity-widget-item__stat">
        16
      </span>
  </div>
</div>
  </a>

      </li>
  </ul>

<!---->
  

</div>
      </div>

          
<a class="app-aware-link  link-without-visited-state feed-identity-module__anchored-widget feed-identity-module__anchored-widget--premium-upsell t-12 t-black t-bold link-without-hover-state text-align-left" href="https://www.linkedin.com/premium/products/?upsellOrderOrigin=premium_homepage_identity_upsell&amp;destRedirectURL=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2F" data-test-app-aware-link="">
    <h3 class="t-12 t-black--light t-normal">
      Access exclusive tools &amp; insights
    </h3>
  <span class="display-flex align-items-start">
      <li-icon aria-hidden="true" type="premium-chip" class="feed-identity-module__premium-icon mr1 flex-shrink-zero"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M20 20a3.36 3.36 0 001-2.39V6.38A3.38 3.38 0 0017.62 3H6.38A3.36 3.36 0 004 4z" fill="#f8c77e"></path>
  <path d="M4 4a3.36 3.36 0 00-1 2.38v11.24A3.38 3.38 0 006.38 21h11.24A3.36 3.36 0 0020 20z" fill="#e7a33e"></path>
</svg></li-icon>
      <span class="feed-identity-module__premium-cta-text">
        Try Premium for free
      </span>
  </span>
</a>


    <a href="/my-items/" id="ember164" class="ember-view feed-identity-module__anchored-widget link-without-hover-state p3 text-align-left">
      <span class="t-12 t-black t-bold v-align-middle display-flex">
        <span class="t-black--light mr2 inline-flex">
          <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="bookmark-fill-small" class="">
<!---->    

    <use href="#bookmark-fill-small" width="16" height="16"></use>
</svg>

        </span>
        My items
      </span>
    </a>
</div>''', height=300)

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
