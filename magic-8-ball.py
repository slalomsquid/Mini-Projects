import random

def main():
    running = True

    answers = [
        "Yes, definitely!",
        "It is certain.",
        "Without a doubt.",
        "Yes, you may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    while running:
        input("Ask away... ")
        print(f"The Magic 8 Ball says: {random.choice(answers)}")

if __name__ == "__main__":
    main()