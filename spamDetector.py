import streamlit as st
from model import *
import pythoncom
from win32com.client import Dispatch


def speak(text):
	speak= Dispatch("SAPI.SpVoice", pythoncom.CoInitialize())
	speak.Speak(text)


if __name__ == "__main__":
	st.title("Email Spam Classification Application")
	st.write("Build with Streamlit & Python")
	activites=["Classification","About"]
	choices=st.sidebar.selectbox("Select Activities",activites)
	if choices=="Classification":
		st.subheader("Classification")
		msg=st.text_area("Enter a text", height = 400)
		if st.button("Process"):
			print(msg)
			print(type(msg))
			# vec=cv.transform(data).toarray()
			result=predict_a_mail(msg)
			if result == 0:
				st.success("This is Not A Spam Email")
				speak("This is Not A Spam Email")
			else:
				st.error("This is A Spam Email")
				speak("This is A Spam Email")
	else:
		st.write("Members of team:")
		st.write("1. Le Lien Huong")
		st.write("2. Le Thi Thanh Huyen")
		st.write("3. Phan Cao Minh Nhat")
		st.write("4. Tran Quang Tri")
