from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Assuming this is how the Ollama model is initialized (verify this with the docs)
ollama_model = Ollama(model="llama3.2")

# Define a prompt template for the financial analysis
prompt = PromptTemplate(
    input_variables=["query"], 
    template="Analyze the financial data based on the following query: {query}"
)

# Create the LangChain pipeline
financial_chain = LLMChain(llm=ollama_model, prompt=prompt)

# Example function to run a query through the financial analyst system
def run_financial_query(query):
    return financial_chain.run(query=query)

# Test with a sample query
result = run_financial_query("What are the latest trends in the stock market?")
print(result)


# Check if Ollama uses a different import pattern
from ollama import LlamaModel  # Hypothetical class name, replace with correct one

llama_model = LlamaModel(model="llama3.2")


