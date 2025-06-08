# ⚽ Football Match Predictor Bot

A Telegram bot that predicts football match outcomes using live match data, odds, and weather.

## 🔧 Features

- Predicts match outcome: Win1 / Draw / Win2
- Shows Double Chance probabilities (1x, x2)
- Fetches live match details via API-Sports
- Gets live betting odds from The Odds API
- Includes match location weather using OpenWeatherMap

## 📦 Requirements

- Python 3.x
- Telegram Bot Token
- API Keys:
  - [API-Sports](https://api-sports.io/) 
  - [The Odds API](https://the-odds-api.com/) 
  - [OpenWeatherMap](https://openweathermap.org/api) 

## 🛠️ Setup Instructions

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables in Render or `.env` file
4. Run locally: `python bot.py`
5. Or deploy on Render

## 🤖 Commands

- `/start` – Get welcome message
- Send any match ID (e.g., `123456`) to get predictions

## 🚀 Deployed?

Use [Render](https://render.com)  to host your bot for free and keep it running 24/7.

Made with ❤️ by [YourName]
