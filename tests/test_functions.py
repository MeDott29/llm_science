import re
from openai import OpenAI
from instructor import patch
from pydantic import BaseModel

class SearchTerms(BaseModel):
    first: str
    second: str
    third: str

client = patch(OpenAI())

def generate_search_terms(test_item):
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
    return resp

def search_wikipedia(search_term):
    text = print_first_two_wikipedia_pages_content(search_term)
    return text

def find_terms_in_same_paragraph(text, term1, term2):
    paragraphs = re.split(r'\s*\n\s*', text)
    matching_paragraphs = []
    for paragraph in paragraphs:
        if re.search(fr'\b{term1}\b', paragraph, re.IGNORECASE) and re.search(fr'\b{term2}\b', paragraph, re.IGNORECASE):
            matching_paragraphs.append(paragraph)
    if not matching_paragraphs:
        return "No paragraph found containing the specified terms."
    return matching_paragraphs

def get_reference_chunk(test_item):
    resp = generate_search_terms(test_item)
    text = search_wikipedia(resp.first)
    paragraphs = find_terms_in_same_paragraph(text, resp.second, resp.third)
    return paragraphs