from langchain.prompts import PromptTemplate
from langchain.llms import Ollama

# Define a prompt template for sentiment analysis
template = "Classify the following text as positive, negative, or neutral: {text}"
prompt = PromptTemplate.from_template(template)

# Initialize the Ollama model
model = Ollama(model="llama3.2")  # Adjust this based on how you set up the Ollama model

# Define the input text
input_text1 = "I love using this product! It works great and I would highly recommend it."
input_text2 = "I had a terrible experience with this product. It broke after one use, and customer service was unhelpful."
input_text3 = "The product was delivered on time. I haven't had the chance to use it yet."
# Generate a prompt
formatted_prompt1 = prompt.format(text=input_text1)
formatted_prompt2 = prompt.format(text=input_text2)
formatted_prompt3 = prompt.format(text=input_text3)


# Get sentiment classification from the model
sentiment1 = model(formatted_prompt1)
print(f"***** Sentiment1 ***** : {sentiment1}")
sentiment2 = model(formatted_prompt2)
print(f"***** Sentiment2 ***** : {sentiment2}")
sentiment3 = model(formatted_prompt3)
print(f"***** Sentiment3 ***** : {sentiment3}")
