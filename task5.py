from langchain_ollama.llms import OllamaLLM # using langchain

# Initialize the Ollama model
llm = OllamaLLM(model="llama3.2")

# Function to interact with the model
def ask_model(prompt):
    return llm(prompt)

# Main loop to ask questions
while True:
    user_input = input("Enter Your Question Please ? (or type 'exit' to stop): ")
    
    # Exit condition
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    respons=llm(user_input)
    print(respons)