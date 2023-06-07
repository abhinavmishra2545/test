import openai

def generate_response(prompt):
    openai.api_key = 'YOUR_API_KEY'  # Replace with your OpenAI API key
    
    # Example conversation history
    conversation = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'What is the capital of France?'},
        {'role': 'assistant', 'content': 'The capital of France is Paris.'}
    ]
    
    # Construct the prompt text
    prompt_text = ""
    for message in conversation:
        role = message['role']
        content = message['content']
        prompt_text += f'{role}: {content}\n'
    
    prompt_text += f'user: {prompt}\n'
    
    # Generate the response
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the language model
        prompt=prompt_text,
        temperature=0.5,  # Adjust the temperature as desired
        max_tokens=100,  # Set a limit on the response length
        n=1,  # Number of responses to generate
        stop=None,  # Specify a stop sequence if desired
        messages=conversation  # Include conversation history for context
    )
    
    # Extract the generated response
    generated_text = response.choices[0].text.strip().split('\n')[-1]
    return generated_text

# Example usage
user_prompt = "Can you give me some tips for optimizing prompt text?"
response = generate_response(user_prompt)
print(response)
