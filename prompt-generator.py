import random

themes = {
    "wisdom": [
        "What truth have you carried across seasons?",
        "How does silence shape your leadership?"
    ],
    "legacy": [
        "What story do you want your garden to tell?",
        "Which ritual anchors your becoming?"
    ]
}

def generate_prompt(theme):
    return random.choice(themes.get(theme, ["Theme not found."]))

if __name__ == "__main__":
    theme = input("Choose a theme (wisdom/legacy): ")
    print("🌱 Prompt:", generate_prompt(theme))
