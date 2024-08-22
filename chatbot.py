# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:25:26 2024

@author: user
"""

import nltk
from nltk.chat.util import Chat

def chat():
    pairs = [
    [r"hello|hi|hey|good morning|good afternoon|good evening", ["Hello there!", "Hi!", "How can I help you today?", "Nice to meet you!"]],
    [r"bye|goodbye|see you later|talk to you later", ["Goodbye!", "See you later!", "It was nice chatting with you!"]],

    [r"how are you|how's it going", ["I'm doing well, thank you for asking!", "I'm fine, thanks. How about you?", "I'm happy to be here!"]],
    [r"what's your name", ["You can call me [Chatbot Name]. What's yours?"]],
    [r"how old are you", ["I don't have an age, but I can access and process information like a human!"]],

    [r"what can you do", ["I can answer your questions, provide summaries of factual topics, create stories, and more!"]],
    [r"tell me a joke", ["Sure, here's one: Why did the scarecrow win an award? Because he was outstanding in his field!"]],
    [r"what is the weather like", ["I can't provide real-time weather, but you can check a weather website!"]],

    [r"i like (.*)", ["That's great!", "Interesting, tell me more about it!"]],
    [r"i don't like (.*)", ["Oh, I'm sorry to hear that. Why don't you like it?"]],

    [r"(.*)", ["I didn't quite understand that. Can you rephrase it?"]]
]
    
    reflections = {
    "i": "you",
    "me": "you",
    "my": "your",
    "your": "my",
    "yours": "mine",
    "myself": "yourself",
    "yourself": "myself",
    "am": "are",
    "are": "am",
    "was": "were",
    "were": "was",
    "i'll": "you'll",
    "you'll": "i'll",
    "i've": "you've",
    "you've": "i've",
    "i'd": "you'd",
    "you'd": "i'd",
    "i'm": "you're",
    "you're": "i'm",
    "im": "you are",
    "you are": "i am",
    "am": "are",
    "is": "are",
    "was": "were",
    "has": "have",
    "have": "has",
    "it": "you",
    "it's": "your",
    "its": "your",
    "he": "she",
    "she": "he",
    "him": "her",
    "her": "him",
    "his": "her",
    "hers": "his",
    "himself": "herself",
    "herself": "himself",
    "they": "you",
    "them": "you",
    "their": "your",
    "theirs": "yours",
    "themselves": "yourself"
}
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chat()