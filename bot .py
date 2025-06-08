# bot.py
import telebot
from config import TELEGRAM_BOT_TOKEN
from predictor import predict_match
from api_helpers import get_match_data

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Football Match Predictor Bot!\nSend me a match ID to get predictions.")

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    try:
        match_id = int(message.text.strip())
        match = get_match_data(match_id)
        if not match:
            bot.reply_to(message, "Invalid match ID.")
            return

        home = match['teams']['home']['name']
        away = match['teams']['away']['name']

        # Simulate strength
        s_home = 9.24
        s_away = 6.81
        delta = s_home - s_away
        probs = predict_match(delta)

        response = f"Prediction for {home} vs {away}
