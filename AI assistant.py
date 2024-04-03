from openai import OpenAI

client =  OpenAI(api_key = 'API_key')

# Create the assistant

assistant = client.beta.assistants.create(name = "Comp Sci tutor",
                                          instructions = "You are a computer science tutor. Write and run code to answer computer science questions",
                                          tools = [{'type' : 'code_interpreter'}],
                                          model = 'gpt-4-1106-preview'
)


# Create a Thread

thread = client.beta.threads.create()


# Add message to a thread

message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role = 'user',
    content = 'Solve this problem : Write a script that retrieves all file names in a folder'
)

# Run the assistant

run = client.beta.threads.runs.create(
    thread_id= thread.id,
    assistant_id= assistant.id
)

# Display assistant's response

run = client.beta.threads.runs.retrieve(
    thread_id= thread.id,
    run_id= run.id
)

messages = client.beta.threads.messages.list(
    thread_id= thread.id
)

for message in reversed(messages.data):   #reversed as we want to first print out the oldest message first
    print(message.role + ': ' + message.content[0].text.value)
    
