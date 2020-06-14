import streamlit as st
# NLP Pkgs
from textblob import TextBlob
import pandas as pd 
# Emoji
import emoji

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Fetch Text From Url
@st.cache
def get_text(raw_url):
	page = urlopen(raw_url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text

def main():

	st.title("Sentiment Analysis ( with emojis! )")

	activities = ["Sentiment","About"]
	choice = st.sidebar.selectbox("Choice",activities)

	if choice == 'Sentiment':
		st.subheader("Sentiment Analysis for your text and emoji message combinations ~ !")
		raw_text = st.text_area("Enter Your Text","Type Here")
		if st.button("Analyze"):
			blob = TextBlob(raw_text)
			result = blob.sentiment.polarity
			if result > 0.0:
				custom_emoji = ':smile:'
				st.write(emoji.emojize(custom_emoji, use_aliases=True))
			elif result < 0.0:
				custom_emoji = ':disappointed:'
				st.write(emoji.emojize(custom_emoji, use_aliases=True))
			else:
				st.write(emoji.emojize(':expressionless:', use_aliases=True))
			st.info("Polarity Score is: {}".format(result))

	if choice == 'About':
		st.subheader("Easy Sentiment Analysis of Text and Emoji App")
		st.info("Built with Textblob and Emoji, Deployed using Streamlit!")
		st.text("Madhav Somanath")
		st.text("github.com/madhav-somanath")

if __name__ == '__main__':
	main()
