import pandas as pd
import requests
import re
from openai import OpenAI
import instructor
from instructor import patch
from pydantic import BaseModel
from typing import Dict

client = patch(OpenAI())
df = pd.read_csv('train.csv')
row = df.iloc[0]

test_item = row['prompt']  + ' ' + row['A'] + ' ' + row['B'] + ' ' + row['C'] + ' ' + row['D'] + ' ' + row['E'] + ' ' + row['answer']

client = instructor.patch(client)

class SearchTerms(BaseModel):
    first: str
    second: str
    third: str
    
resp = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {
            "role": "user", 
            "content": f"Read the MCQ and give the top three terms you would use to search for an answer: {test_item}",
        },
    ],
    response_model=SearchTerms
)
resp
print(resp)

def clean_string(s):
  # Remove everything inside parentheses
  s = re.sub(r'\([^()]*\)', '', s)
  
  # Remove all non-alphabetical characters except spaces
  s = re.sub(r'[^a-zA-Z ]', '', s)
  
  # Remove spaces from the end of the string
  s = s.rstrip()
  
  return s

search_term = clean_string(resp.first)
print(search_term)

def print_first_two_wikipedia_pages_content(search_query):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    SEARCHQUERY = search_query

    PARAMS = {
        "action": "opensearch",
        "format": "json",
        "search": SEARCHQUERY,
        "limit": 2,
    }

    response = S.get(url=URL, params=PARAMS)
    data = response.json()

    page_titles = data[1]

    content = ""
    for title in page_titles:
        PARAMS = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "explaintext": True,
        }

        response = S.get(url=URL, params=PARAMS)
        data = response.json()

        pages = data["query"]["pages"]

        for k, v in pages.items():
            content += v["extract"]
    
    return content
print_first_two_wikipedia_pages_content(search_term)
def find_terms_in_same_paragraph(text, term1, term2):
  paragraphs = re.split(r'\s*\n\s*', text)
  matching_paragraphs = []
  for paragraph in paragraphs:
      if re.search(fr'\b{term1}\b', paragraph, re.IGNORECASE) and re.search(fr'\b{term2}\b', paragraph, re.IGNORECASE):
          matching_paragraphs.append(paragraph)
  if not matching_paragraphs:
      return "No paragraph found containing the specified terms."
  return matching_paragraphs

text = print_first_two_wikipedia_pages_content(search_term)

paragraphs = find_terms_in_same_paragraph(text, resp.second, resp.third)
for i, paragraph in enumerate(paragraphs):
    print(f"Paragraph {i+1}:\n{paragraph}\n")