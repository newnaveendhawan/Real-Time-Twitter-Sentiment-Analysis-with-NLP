# Real-Time-Twitter-Sentiment-Analysis-with-NLP
A clean, modern, and intuitive web application that analyzes the **sentiment of tweets** from any public Twitter account in real time. Built with Flask, this project combines **natural language processing** with **live Twitter data** to help users understand how people feel based on their tweets — visually and analytically.

## 🚀 Project Overview
This app fetches the latest tweets of a user and determines whether each tweet is Positive, Negative, or Neutral  using the VADER Sentiment Analysis tool. It displays an overall sentiment summary, sentiment-tagged tweets, and supports both Light and Dark mode UI for better readability. Whether you're analyzing a brand's reputation, tracking public opinion, or exploring social media trends, this tool provides actionable insights at your fingertips.

## 🔧 Key Features
##### ✨ Analyze live tweets by entering a username
##### 🌈 Sentiment color indicators: Positive ✅, Negative ❌, Neutral ⚪
##### 🌙 Toggle between Light and Dark mode for better accessibility
##### 📊 Sentiment breakdown summary in percentages
##### 💡 Clear sentiment labels with compound scores
##### 📱 Fully responsive design for seamless use on all devices

## 🖼️ Screenshot of the Web App
##### Here’s a glimpse of the web app in action:
![image](https://github.com/user-attachments/assets/96afd23a-fe36-417a-9d8d-35b2a45beb01)

## 🛠 Tools & Technologies Used:
##### Python 3 – Core programming language
##### Flask – Lightweight web framework for backend
##### HTML + CSS – For frontend UI design
##### Jinja2 – Templating engine to render dynamic HTML
##### Gunicorn – WSGI HTTP server for production deployment
##### Twitter API – To fetch live tweets from user profiles
##### Render / Railway – For hosting and deployment
##### Git & GitHub – Version control and collaboration
##### python-dotenv – To securely manage environment variables
##### re (Regular Expressions) – For cleaning tweet text before analysis
##### requests – for handling HTTP requests

## 📊 Techniques Used:
##### Sentiment Analysis – Using VADER (Valence Aware Dictionary and Sentiment Reasoner) to analyze tweet sentiments
##### Data Preprocessing – Basic cleaning of tweet text before analysis
##### Environment Variables – Managing secret API keys securely
##### Frontend Rendering – Displaying results interactively using dynamic templates

## ⚙️ How It Works
##### Input: The user enters a public Twitter username.
##### Fetch Tweets: The app retrieves the latest tweets via the Twitter API.
##### Sentiment Analysis: Each tweet is passed through the VADER sentiment analyzer.
##### Classification: The app classifies each tweet as:
#### ✅ Positive
#### ❌ Negative
#### ⚪ Neutral
##### Output: The app displays:
##### Sentiment-tagged tweets with scores
##### An overall sentiment summary (percentage breakdown)
##### A toggleable UI for light/dark mode

## 📈 Key Outcomes
##### Real-time sentiment classification from live Twitter data
##### Visual summary of tweet sentiments (positive, negative, neutral)
##### Fully responsive and toggleable UI for enhanced user experience
##### Secure handling of API keys using .env
##### Deployed and accessible via the web

## 📜 License
This project is licensed under the [MIT License](https://github.com/newnaveendhawan/Real-Time-Twitter-Sentiment-Analysis-with-NLP/blob/main/LICENSE). See the LICENSE file for details.

## 👨‍💻 About the Author
# Naveen Dhawan
##### 🎓 B.Tech – NIT Warangal
##### 💼 Data Analyst | Data Science | Dashboard Creator
##### 💡 Passionate about turning raw data into meaningful insights
##### 📫 Connect on [LinkedIn](https://www.linkedin.com/in/newnaveendhawan/)
