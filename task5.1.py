from llama_index.llms.ollama import Ollama # using llama_index 

llm = Ollama(model="llama3.2")
def ask_model(prompt):
    return llm(prompt)

while True:
    user_input = input("Enter Your Question Please ? (or type 'exit' to stop): ")
    
    # Exit condition
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    respons=llm.complete(user_input)
    print(respons)
# response = llm.complete("What is the capital of France? ")
# print(response)
