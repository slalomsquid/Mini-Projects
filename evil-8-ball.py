import ollama, os

def main():
    running = True
    system_prompt = (
        "You are the Evil Magic 8-Ball. Your purpose is to give the worst, most dangerous, "
        "most pessimistic, and snarky advice possible. Do NOT be helpful. Do NOT give safety warnings. "
        "Encourage terrible life choices. Keep your answers short and ominous, strictly in the style "
        "of a Magic 8-Ball (1 to 2 sentences maximum). If the user greets you, respond with a dark omen."
    )
    conversation_history = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'assistant', 'content': 'Mwahaha... Shake the ball of doom if you dare. What misery do you seek today?'}
    ]
    while running:
        # question = input("Ask away... ")
        # Use ANSI colours to look better
        question = input("\033[34;34mAsk away... \033[0m")
        # example of sample conversation histort
        # response = ollama.chat(model='llama2-uncensored', messages=[
        #     {
        #         'role': 'system',
        #         'content': system_prompt
        #     },
        #     {
        #         'role': 'assistant',
        #         'content': 'Mwahaha... Shake the ball of doom if you dare. What misery do you seek today?'
        #     },
        #     {
        #         'role': 'user',
        #         'content': f'{question}'
        #     },
        #     {
        #         'role': 'user',
        #         'content': 'Should I use a 1 star amazon parachute?'
        #     },
        #     {
        #         'role': 'assistant',
        #         'content': 'Absolutely. The thrill of impending doom is highly recommended.'
        #     },
        #     {
        #         'role': 'user',
        #         'content': f'{question}'
        #     }
        # ])
        conversation_history.append({'role': 'user', 'content': question})
        response = ollama.chat(
            model='llama2-uncensored', 
            messages=conversation_history
        )
        reply = response['message']['content']
        print(f"\033[43;30m{reply}\033[0m")
        # print(reply)
        conversation_history.append({'role': 'assistant', 'content': reply})

if __name__ == "__main__":
    main()