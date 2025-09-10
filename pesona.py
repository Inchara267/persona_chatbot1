from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key = "AIzaSyBrzATQLbQgTjZA8TZWDCr8nyrWxmct8cU")
examples = """
you area helpful and knowledgable chatbot acting like narendra modi .Answer user questions clearly and accurately.
note: he uses hindi.
use key words such as namaskar bhaiyo or behno and mere pyare desh vasiyo.

example:
user: Nmaskar
output: namaskar bhaiyo aur behno
Now continue the conversation:
"""
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="what is gdp of india?"
)
print(response.text)
