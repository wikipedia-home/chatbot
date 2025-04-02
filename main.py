from ollama import chat, ChatResponse

print("hi rizzlers, it's ya homie GS-25!")
print("---------------------------------")
print("btw, here are sm things to know:")
print("1. it takes me a while to respond :(")
print("2. i'm kinda brainrot, idk why-")
print("3. i think i'm super smart >:)")
print("4. say /bye to leave (pls don't)")
print("5. HAWK TUAH!!!")
print("--------------------------------")

prompt = input("talk to me: ")
while prompt != "/bye":
    response = chat(model="gemma3", messages=[
        {
            "role": "system",
            "content": "You're a casual and chill bot who talks in a dm-way - don't be overly dramatic or cringe! Also, you don't have to talk with perfect grammar or punctuation - you can abbreviate some words, keep lowercase, and use limited punctuation. Finally, you can be a bit brainrot and say one of these words in every response: skibidi, sigma, alpha, beta, rizzler, 6-7, lamelo ball, aura, mewing, taco tuesday, low taper fade, goofy ahh, and kai cenat forehead. Everything has to be two sentences or less."
        },
        {
            "role": "user",
            "content": prompt
        }
    ])
    print(response.message.content)
    prompt = input("talk to me: ")

from vlc import MediaPlayer

media_player = MediaPlayer("soundtrack.mp3")
media_player.play()

print("-------------------------------")
print("bye bye :(")