import sys
import subprocess
import ssl
subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])

'''
Feel free to delete the lines above here once you have installed the necessary packages
'''

from openai import OpenAI
import base64
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
with open('api_key.txt', 'r') as file:
    key = base64.b64decode(file.read().strip()).decode('utf-8')

client = OpenAI(api_key=key)

'''
In this lab you'll experiment with the OpenAI API.
An API is a way for one program to talk to another program. Sometimes over the internet!
In this case, we're going to use the OpenAI API to make our program talk to their GPT large language models.

There are many different things you can do with these models, but we'll focus on two main things:
    1. Completions: Generating text completions given a prompt.
    2. Chat: Having a conversation with the model.

In either case, the basic idea is the same: You send a request to the API, and it sends a response back.
The request is just a bundle of information about what we want, and the necessary info,
and the response is another bundle of information that hopefully contains what we want.

Normally, to use an API you may need to write a lot of code to handle the request and response.
But OpenAI has made it very easy to use their API by providing a Python package that does all the hard work for you.

The package is called "openai", and it should have already been installed by the code at the top of this file.

In order to use the API you need an API key, which is a long string of characters that identifies you to the API.
We have provided you with an API key that you should have saved in a file called "api_key.txt".
The "api_key.txt" file should be in the same directory as this file (or wherever you're running this from).
If you have it in the right place, it will automatically load when you run this file.

Go ahead and run this program now to install the openai package, and to check for any errors.
Once it runs without error (the warning to upgrade pip is not an error!) then continue to Part 1.
'''


###########################################################################################
# PART 1a: Completions
# 
# The original GPT model was trained to predict the next word in a sentence, given all the previous words.
# This is called "autoregressive" language modeling, and it's the same thing that the "predictive text" feature
# on your phone does. The GPT-3 model is a very large and powerful version of this, and it can generate very
# realistic text completions.
#
###########################################################################################

try:
    # The model is the name of the model you want to use.
    model = "gpt-3.5-turbo-instruct"

    # The prompt is the input to the model. It should be a string of text.
    prompt = "Once upon a time"
    
    # Number of tokens determines the maximum length of the response
    max_tokens = 10

    # Number of options to generate
    n = 1

    # Temperature of the sampling. Higher values means the model will take more risks.
    temperature = 0.0
 
    # Now with a single line we can call the API to get the completion!
    response = client.completions.create(model=model,prompt=prompt, max_tokens=max_tokens, n=n, temperature=temperature)
    
    # What comes back is an object with a lot of information.
    # Feel free to print it out to see what it looks like:
    #   print(response)

    # It looks something like this:

    '''
    Completion(id='cmpl-8zS6ggu1R7p4lVkHOackG45DRUPRY', 
               choices=[CompletionChoice(finish_reason='length', 
                                         index=0, 
                                         logprobs=None,
                                         text=', a powerful king decided')],
               created=1709656742,
               model='gpt-3.5-turbo-instruct',
               object='text_completion',
               system_fingerprint=None, 
               usage=CompletionUsage(completion_tokens=5,
                                     prompt_tokens=4,
                                     total_tokens=9))
    '''

    # Notice that the actual completion ', a powerful king decided' is nested deep inside there.
    #
    # Where is it exactly?... Starting with the Completion object inside the 'response' variable...
    # Inside the 'choices' attribute is a list...
    # Inside that list is a single CompletionChoice object (because we set n=1 to generate one option)...
    # Inside that object is a 'text' attribute...
    # That's the completion!
    #
    # Whew! So how do we get it out?
    #
    # To access an attribute of an object, you use the dot operator. (i.e. object.attribute)
    # To access an element of a list, you use the square brackets. (i.e. list[index])
    # So to get the completion, you would do this:
    #
    #   completion = response.choices[0].text
    #
    # Go ahead and try it out!

    ''' TODO: Get the completion text from the response and print it out. '''

    # Maybe even more interesting is to combine the original prompt and the completion into a single string.
    # For example, if the prompt was "Once upon a time" and the completion was ", a powerful king decided",
    # then the combined string would be "Once upon a time, a powerful king decided".
    # This can be done with the '+' operator.

    ''' TODO: Print out the prompt and the completion together.'''

    # Now you can try different prompts and see what the model comes up with!

    ''' TODO: Try some other prompts, followed by API calls, and printing out the combined result.'''
    
    prompt = "???"  # Try another prompt
    response = client.completions.create(model=model,prompt=prompt, max_tokens=max_tokens, n=n, temperature=temperature)
    # TODO: Print out the prompt and the completion together.

    prompt = "???"  # Try another prompt
    response = client.completions.create(model=model,prompt=prompt, max_tokens=max_tokens, n=n, temperature=temperature)
    # TODO: Print out the prompt and the completion together.

    prompt = "???"  # Try another prompt
    response = client.completions.create(model=model,prompt=prompt, max_tokens=max_tokens, n=n, temperature=temperature)
    # TODO: Print out the prompt and the completion together.

    # Great! Now...
    # Just for fun let's play with some other parameters of the API call.
    # Copy/paste the three prompts you just tried, and change all of their max_tokens to 50.

    ''' TODO: Copy/paste the three prompts you just tried, and change all of their max_tokens to 50.'''

    # Now you can see how the length of the completion changes with the max_tokens parameter.

    # Another interesting parameter is the temperature. Try setting it to 0.9 and see what happens.

    ''' TODO: Copy/paste the three (including longer response length), and change all of their temperatures to 0.9.'''

    # What happened? Can you describe the change?
    # Once you have all of those set up, trying running this program a couple of times in a row.
    # Do you notice anything?

    # We'll leave the completions API there for now.
    # There are many other parameters you can play with. Check out the documentation for more information:
    # https://platform.openai.com/docs/api-reference/completions/create

    # When you're ready, move on to Part 1b below.

except Exception as e:
    print("An error occurred, which might indicate an invalid token or other issues:")
    print(e)


###########################################################################################
# PART 1b: Chat
#
# Starting with a text completion model, which was not itself new, one of OpenAI's big innovations
# was to fine-tune the model in a way that they hoped would allow it to be more conversational.
# This was done by training it on a large dataset of conversations, and then using a technique called
# RLHF (Reinforcement Learning from Human Feedback) to further improve its conversational abilities.
#
# The result was surprising to many in the AI community: the model was able to have conversations that
# were often very realistic and helpful. It was able to answer questions, provide information, and even
# sometimes give coherent advice. It was also able to remember things from earlier in the conversation,
# and to maintain a consistent personality and tone.
#
# The chat API is a way to interact with this model. You can send it a message, and it will send a response.
# There's a little more to it than that, but that's the basic idea. Let's take a look.
#
###########################################################################################
    
try:
    # The model is the name of the model you want to use.
    model = "gpt-3.5-turbo"

    # The model itself doesn't keep track of the conversation, it just generates a response given an existing
    # conversation as a prompt. So you need to send the entire conversation each time you want to get a response!
    # This is why we maintain the conversation in a list of messages:

    # It should be a list of dictionaries, each with a "role" and "content".
    messages = [
        {"role": "user", "content": "Hello, how are you today?"}
    ]
    
    # Now again with a single line we can call the API to get the response!
    response = client.chat.completions.create(model=model, messages=messages)
    
    # Again, we can look at the response to see what it looks like:
    #   print(response)

    '''
    ChatCompletion(id='chatcmpl-8zog6tf0qsGHEyavwo4kc18Z2Umyc',
                   choices=[Choice(finish_reason='stop', 
                                   index=0, 
                                   logprobs=None, 
                                   message=ChatCompletionMessage(content="Hello! I'm just a computer program, so I don't have feelings, 
                                                                          but I'm here and ready to help you. How can I assist you today?",
                                                                 role='assistant', 
                                                                 function_call=None, 
                                                                 tool_calls=None))],
                   created=1709743506,
                   model='gpt-3.5-turbo-0125',
                   object='chat.completion',
                   system_fingerprint='fp_b9d4cef803',
                   usage=CompletionUsage(completion_tokens=33, prompt_tokens=14, total_tokens=47))
    '''

    # Again, the response has a lot of information, but the actual response is nested deep inside there.
    # It's inside the 'choices' attribute, which is a list...
    # Inside that list is a single Choice object...
    # Inside that object is a 'message' attribute containing a ChatCompletionMessage object...
    # Inside that object is a 'content' attribute...
    # That's the response!

    # Can you figure out how to get the text out of the response object?
    # Give it a try!

    ''' TODO: Get the chat completion content from the response and print it out. '''

    # Once you've got that working, you can try having a conversation with the model!
    # But remember! You need to send the entire conversation each time you want to get a response.
    # So before we add another user message to end, we should add the message we just received from the model.

    ''' TODO: Put the response text in a variable called "response_text" and add it to the messages list. '''

    # Uncomment the following line once you have the text in a variable called "response_text":
    #   messages.append({"role": "assistant", "content": response_text})

    # Now you can add another user message to the conversation, and get another response from the model.
    #   messages.append({"role": "user", "content": "???"})

    # And then you can get the response from the model again.
    #   response = client.chat.completions.create(model=model, messages=messages)

    # And then you can print out the response again...
    #   response_text = response.choices[0].message.content

    # And then you can add the response to the messages list again... etc, etc, etc!
    # Now that you've got the basic idea, move on to part 2 in the other Python file.
    # There, you'll put all of this inside a loop to make your own version of ChatGPT!

except Exception as e:
    print("An error occurred, which might indicate an invalid token or other issues:")
    print(e)