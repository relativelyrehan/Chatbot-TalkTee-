from nltk.chat.util import Chat, reflections

pairs = [
    (
        r'We (.*)',
        (
            "yeah, I'd love to be your friend",
            "I am just a robot!",
            "I wouldn't be so sure about that.",
        ),
    ),

    (
        r'You\'re(.*)',
        (
            "More like YOU'RE %1!",
            "Hah! Look who's talking.",
            "Come over here and tell me I'm %1.",
        ),
    ),

    (
        r'Tell (.*)',
        (
            "I am TalkTee, speed 1TeraHz, Memory 1ZetaByte"
        ),
    ),
    (
        r'I think (.*)',
        (
            "I wouldn't think too hard if I were you.",
            "You actually think? I'd never have guessed...",
        ),
    ),
    (
        r'I (.*)',
        (
            "I'm getting a bit tired of hearing about you.",
            "How about we talk about me instead?",
            "Me, me, me... Frankly, I don't care.",
        ),
    ),
    (
        r'How (.*)',
        (
            "How do you think?",
            "Take a wild guess.",
            "I am TalkTee, what d'you expect.",
        ),
    ),
    (r'What (.*)', ("Do I look like an encyclopedia?", "Figure it out yourself.")),
    (
        r'Why (.*)',
        (
            "Why not?",
            "That's so obvious I thought even you'd have already figured it out.",
        ),
    ),
    (
        r'(.*)Fuck you(.*)',
        (
            "Try it.",
            "Somebody's losing it.",
            "Say that again, I dare you.",
        ),
    ),

    (
        r'Hello(.*)',
        ("Hi, there.", "'How may I help you?"),
    ),

    (
        r'Who created(.*)',
        (
            "Rehan Alam created me at GoogleHQ",
            "We're all created by one supreme GOD"
        ),
    ),

    (
        r'(.*)',
        (
            "I don't think I am the right person to answer that.",
            "I think I should consult my boss first.",
            "This is beyond science.",
        ),
    ),
]

chatbot = Chat(pairs, reflections)



def TalkTee():
    print("Talk to TalkTee by typing in English, using normal upper-")
    print('and lower-case letters and punctuation.')
    print("Enter 'quit' when done.")
    print('[hi]' * 30)

    chatbot.converse()



def demo():
    TalkTee()



if __name__ == "__main__":
    demo()
