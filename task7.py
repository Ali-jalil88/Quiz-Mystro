# Importing the Ollama integration from langchain
from langchain_ollama.llms import OllamaLLM

# Initialize the Ollama LLM model for summarization
llm = OllamaLLM(model="llama3.2")  # Adjust model as necessary

# Define the function to perform summarization
def summarize_text(text):
    # Prompt wrapped in a list
    prompt = [f"Summarize the following text in a concise way:\n\n{text}"]
    
    # Using the generate method with a list of prompts
    response = llm.generate(prompts=prompt)
    
    # Accessing the text from the response
    return response.generations[0][0].text

# Sample text input to be summarized
input_text = """
LangChain is a powerful framework for developing applications powered by language models. 
It enables connections between models like OpenAI, Hugging Face, and Ollama with various tools, agents, 
and data structures to build more capable applications. 
LangChain excels in creating chains, structured pipelines for NLP tasks such as summarization, information retrieval, 
and question-answering.
"""

# Get and print the summary
summary = summarize_text(input_text)
print("******* Summary ******* :", summary)
