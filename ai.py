#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:34:48 2023

@author: bmiit202006100110040
"""

import openai

# Set your OpenAI API key here
openai.api_key = "sk-5yHvYYPHIoTxxkVf2W3HT3BlbkFJGQxRxcxPSErJPKroHPKhz"

def ask_chatbot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose an appropriate engine
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()

print("Chatbot: Hello! I'm your AI chatbot. You can start chatting with me. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    chatbot_response = ask_chatbot(user_input)
    print("Chatbot:", chatbot_response)
