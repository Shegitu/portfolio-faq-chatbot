faqs = {
    "hi": "Hey there, happy to see you!",
    "who are you": "I am Shegitu Shukuri.",
    "where do you study": "I am studying at AASTU.",
    "what is your department": "I am a Software Engineering student.",
    "what technical skills do you have": "Python, C++, Java, Generative AI, Graphic Design.",
    "what projects have you done": "Pharmacy Management System, Smart Stove Safety System, Community Connect, AASTU Assistant Chatbot.",
    "do you have certificates": "Yeah, in AI and ML, SolidWorks, Data Science, and Machine Learning.",
    "why are you interested in": "I am mainly interested in Quantum Computing.",
    "how can i contact you": "You can contact me through my LinkedIn account who https://www.linkedin.com/in/shegitu-shukuri-49b73637",
    "bye":"Goodbye! Have a nice day."
}

import string

while True:
    user_input = input("You: ").lower()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))

    
    if user_input in ["bye", "exit", "quit"]:
        bot_reply = "Goodbye! Have a nice day!"
        print("Bot:", bot_reply)
        with open("chat_history.txt", "a") as f:
            f.write(f"You: {user_input}\n")
            f.write(f"Bot: {bot_reply}\n")
        break


    elif user_input in faqs:
        bot_reply = faqs[user_input]

    
    elif "hi" in user_input or "hello" in user_input:
        bot_reply = "Hey there, happy to see you!"
    elif "skills" in user_input or "knowledge" in user_input or "experience" in user_input:
        bot_reply = "Python, C++, Java, Generative AI, Graphic Design."
    elif "project" in user_input:
        bot_reply = "I have built Pharmacy MS, Smart Stove Safety System, Community Connect, and Campus Assistant Chatbot."
    else:
        bot_reply = "Sorry, I don’t understand."

    
    print("Bot:", bot_reply)
    with open("chat_history.txt", "a") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"Bot: {bot_reply}\n")
