from openai import OpenAI
import base64
with open('1202/api_key.txt', 'r') as file:
    key = base64.b64decode(file.read().strip()).decode('utf-8')

client = OpenAI(api_key=key)

###########################################################################################
# PART 2: Command Line Chat
###########################################################################################

'''
Now that you've got a handle on making API calls, saving messages, and understanding the structure
of API responses, maybe you can see where this is going... 

Let's actually make a real-time chat interface in our console using print() and input() !

The chat will be a simple back-and-forth between the user and the AI. The user will input a message,
the AI will respond, and so on. The conversation will be saved in a list of messages, and the AI's
response will be based on the context of the conversation.

This is actually really easy, you've already done most of this in the previous parts, now you just
put it inside a loop and handle the user input.

We've already set up most of the structure for you, you just need to fill in the blanks.
We've also made it so that the chat will end when the user types 'exit'.

Follow along with the TODO comments to complete the console based chat app.
'''

# Start of the chat session
print("This is a chat with OpenAI's GPT model. Type 'exit' to end the chat.")

messages = []  # List to keep track of the conversation

for _ in range(10):
    # User input
    user_message = input("You: ")
    if user_message.lower() == 'exit':
        break

    ''' TODO: Append the user's message to the messages list with the appropriate role 
              remember, the message should be in a dictionary with the format:
                    {"role": "user", "content": user_message}
    '''
    messages.append({"role": "user", "content": user_message})

    try:
        ''' TODO: Use the OpenAI API to get a response based on the current conversation context. Specify the model and messages '''
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        ''' TODO: Extract the response text from the API response and print it '''
        ai_message = response.choices[0].message.content
        print("AI:", ai_message)
        ''' TODO: Append the AI's response to the messages list with the appropriate role '''
        messages.append({"role": "assistant", "content": ai_message})
        # All done, back to the top of the loop!
        
    except Exception as e:
        print(f"An error occurred: {e}")
        break

print("Chat ended.")
