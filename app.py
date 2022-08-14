import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Ahmed's Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#@-----LOAD ASSETS-----------
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_coding1 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_knvn3kk2.json")
#img_contact_form = Image.open("images/yt_contact_form.png")
#img_lottie_animation = Image.open("images/yt_lottie_animation.png")

#---HEADER SECTION-------
with st.container():
	st.subheader("Hello, :wave:")
	st.title("I am a Deep Learning Enthusiast")
	st.write("I am Passionate about Neural Networks and like to develop solutions to real world problems")
	st.write ("[Leaern More>](https://docs.streamlit.io/library/get-started)")

with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("What I do")
		st.write("##")
		st.write(
		"""
		Few of My constibutions
		1. Development of DNN to halide  Conversion Tool
		2. Image Recognition and Anomaly Detection
		3. LLVM Compiler Optimizations
		4. Legacy Translator
		5. Open64 Project
		6. GCC Compiler Framework
	       """
		)
		st.write("[AI Tools that Inspire>](https://www.youtube.com/watch?v=891pzwMZDC8)")
	with right_column:
		st_lottie(lottie_coding1, height=300, key="coding")
		
# ---- PROJECTS ----
with st.container():
	st.write("---")
	st.header("My Projects")
	st.write("##")
	image_column, text_column = st.columns((1, 2))
	with image_column:
		st_lottie(lottie_coding, height=300, key="coding1")
	with text_column:
		st.subheader("Future of AI")
		st.write(
            """
         	Undoubtedly, Artificial Intelligence (AI) is a revolutionary field of computer science,
 		which is ready to become the main component of various emerging technologies like big data,
		robotics, and IoT. It will continue to act as a technological innovator in the coming years
            """
		)
	#st.markdown("[Watch Video...]("https://www.youtube.com/watch?v=63yr9dlI0cU")
		#st.markdown("[Watch Video...]("https://www.youtube.com/watch?v=63yr9dlI0cU")
		



# ---- CONTACT ----
with st.container():
	st.write("---")
	st.header("Get In Touch With Me!")
	st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
	contact_form = """
    <form action="https://formsubmit.co/invinx188@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
	left_column, right_column = st.columns(2)
	with left_column:
 		st.markdown(contact_form, unsafe_allow_html=True)
	with right_column:
 		st.empty()
	