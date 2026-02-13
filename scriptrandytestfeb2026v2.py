
import openai
import os
import dotenv

#import dotenv
dotenv.load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("API_KEY")

#enable below if you use Azure Open AI
# openai.api_type = 'azure'
# openai.api_version = '2023-05-15'
# openai.api_base = os.getenv("API_BASE")

#add your completion code
prompt = "Complete the following: Once upon a time there was a"

#engine
#engine = "davinci-001"  # for OpenAI is outdated, use model instead

#use modern API based on help from Claude on Feb 12 2026
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    max_tokens=100
)
#print the response
print(response.choices[0].message.content)