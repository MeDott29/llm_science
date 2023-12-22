
Work Log
---
### 2023/12/22
```
"""Here's a comprehensive response to the prompt, incorporating insights from the provided experiments and addressing potential challenges:
 
1. Define Purpose and Scope:
 
 
Clarity on Intended Use: Specify whether the software is for general text editing, content filtering, language translation, code obfuscation, privacy protection, or other specialized tasks. This will guide design choices.
 
Input/Output Formats: Determine the supported text formats (e.g., plain text, HTML, code) and output preferences (e.g., in-place editing, creation of new files).
 
Target Platforms: Specify the intended operating systems and devices for compatibility.
 
 
2. Choose Implementation Strategy:
 
 
Rule-Based Systems: Create replacement rules using regular expressions or dictionaries for straightforward word substitutions.
 
Machine Learning: Train models on large text corpora to learn replacement patterns for more complex word transformations.
 
Hybrid Approaches: Combine rule-based and ML techniques for greater flexibility and adaptability.
 
 
3. Design Core Algorithm:
 
 
Text Preprocessing: Clean and tokenize input text to prepare for word analysis.
 
Word Identification: Employ linguistic techniques (e.g., part-of-speech tagging) to accurately locate target words.
 
Word Replacement: Apply specified rules or model predictions to substitute words effectively.
 
Text Reconstruction: Reassemble the modified text while preserving grammar and fluency.
 
 
4. Address Specific Requirements:
 
 
Custom Replacement Rules: Allow users to define their own word pairs for personalized modifications.
 
Preservation of Formatting and Structure: Maintain original text formatting and structural elements (e.g., headings, paragraphs).
 
Performance Optimization: Ensure efficient processing of large text files for practical use.
 
User Interface Design: Create a user-friendly interface for specifying replacement rules, selecting text sources, and viewing results.
 
 
5. Conduct Rigorous Testing:
 
 
Evaluate Accuracy: Measure the software's ability to correctly identify and replace target words.
 
Assess Fluency: Ensure that the generated text is grammatically correct and semantically coherent.
 
Test Performance: Evaluate processing speed and resource usage for different input sizes and complexity.
 
 
6. Additional Considerations:
 
 
Integration with Other Systems: Explore integration with text editors, content management systems, or other relevant tools.
 
Ethical Implications: Consider potential misuse of the software for deceptive or harmful purposes, and implement safeguards if necessary.
 
Privacy Protection: Address potential privacy concerns if handling sensitive text data.
 
 
I'm ready to provide more specific guidance as you refine your software's goals and requirements."""
```
How would you describe the structure and function of this document? Is it like an executive summary?
 ---
 Yes, this document can be considered an executive summary of a broader plan or proposal for developing a text manipulation software. It provides a high-level overview of the key stages involved, from defining the software's purpose and scope to testing and additional considerations. 

Here's how it resembles an executive summary:

* **Conciseness:** The document summarizes a complex topic in a clear and concise way, without getting bogged down in technical details.
* **Key Points:** It identifies the main aspects of the software development process, including purpose, implementation strategies, core algorithms, and specific requirements.
* **Structured format:** The document is well-organized, with numbered sections and subheadings for ease of navigation.
* **Actionable insights:** It concludes with an offer for further guidance, implying a readiness to delve deeper into specific details.

While not as comprehensive as a full-fledged plan, this executive summary effectively conveys the essence of the project and its potential. It allows readers to grasp the overall approach and key challenges without reading a lengthier document.

However, there are some nuances to consider:

* **Level of detail:** Compared to a traditional executive summary, this one is more detailed and technical, likely targeting an audience with some understanding of software development.
* **Specific context:** The summary mentions insights from experiments, suggesting it might be part of a larger research or development project.

Overall, this document serves as a valuable overview of a text manipulation software development plan, functioning effectively as a concise and informative executive summary tailored to its intended audience.

---

So I am trying to reason through a way to automate the processes involved in deciphering all the meaningful, useful directions one gets from an LLM when asking questions and designing software.  I ask a question like "I want to design a program that ..." and I get a list of tasks.  
### 2023/11/22

I want to learn these libraries by utilizing them in my projects:
```
import pytest
import pydantic
import fastapi 
import openai #high prio
import asyncio #high prio
import tenacity #high prio
import chroma
import logging #high prio
```
Yesterday I learned it was important to break my task up into small goals in service of achieving an objective.
Yesterday the objective was getting an emulation of human techniques for MCQ answering.  [Improved Retrieval with LLMs](/home/m/llm_science/improved_retrieval.ipynb)
### 2023/11/21
## Thoughts
This is at once the most mundane, plain Jane bullshit and the coolest thing I've ever done in my life. The sweet spot.
### Notes
I made some real progress today. https://github.com/MeDott29/llm_science/blob/main/improved_retrieval.ipynb
I decided it's mandatory to find all the reference chunks for the data in 'train.csv'.  I want to emulate the exact process I follow when I'm looking through wikipedia for the paragraph that was used to generate a test question.  I was able to do that today.


## Summary
Ask for advice:
```
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
```
Use first term to search Wikipedia API. Use second and third terms to find a paragraph that contains both terms.  
Reference paragraph found.

### 2023/11/20
Have you seen it? https://www.kaggle.com/competitions/kaggle-llm-science-exam
The competition is over but I'm working on a system that will hopefully improve on the high score.
The highest scoring notebook as of right now uses 2.5TB of reference data and takes 9 hours to complete.  Each of the top 50 teams have a score between 93% and 91%.  They all used top_k and RAG.

I just read https://jxnl.github.io/instructor/blog/2023/11/18/validate-citations/ and I figured I'd reach out in hopes that our interests might align on this project.

I'm still grasping at straws but I think the play right now is to create a dataset for training a model that excels at answering difficult science questions.  This repo gets you started on looking at the data and brainstorming schemas. https://github.com/MeDott29/llm_science

Can we use instructor to create a dataset that teaches a model to find the exact chunk of text a MCQ was generated from?
I see this work as one of the most important areas in the field right now. I believe it promises to unlock an unprecedented degree of dependability and confidence for both parties in the LLM + person partnership.

# Looking Forward

- [ ] Emulate test question reference chunk retrieval
    - [x] retrieve reference chunk with one train data row
    - [ ]retrieve reference chunk across multiple train data rows
    - [ ]retrieve reference chunk with one test data row
    - [ ]retrieve reference chunk across multiple test data rows
- [ ] Automate test question reference chunk retrieval
    - [ ]
- [ ] Automate training data acquisition
- [ ] Generate test questions
- [ ] Automate and optimize test model

# Daunting Tasks Include but are not limited to 
- [ ] create and test different methods for generating test item options (key plus distractors)
    - [ ] "given the following chunk, do you think this MCQ was generated using more than one sentence as a reference or do you think it could be generated using a single sentence from the reference material?" (decision tree architecture?)
    - [ ] two-prompt, "ask a MCQ based on {chunk}" --> "generate five options including four distractors and one key based on {{chunk} + {MCQ}} "
    - [ ] iterative/waterfall "given {chunk} extract a key fact for use in a MCQ" --> for option in options ():"given {distractor_list} + {key} + {chunk} generate a distractor"
- [ ] the dirty work of sentence level MCQ generation over sentences in wikipedia.  I'm getting the feeling the questions were not chunked on paragraphs but individual sentences were used, at least in some cases...

# Next Steps

1. **Refine the Search Function**: Enhance the search function to consider all the terms for a more accurate search.
    - Use More Search Terms: Modify the function to use all the terms, or a combination of them, to get more accurate search results.
    - Advanced Search Techniques: Consider using advanced search techniques such as phrase search, OR search, and NOT search.
    - Ranking Search Results: Implement a ranking system for the search results based on relevance.
    - Filtering Search Results: Add filters to your search function to narrow down the results.
    - Iterative Search: If the initial search does not yield satisfactory results, perform additional searches using different combinations of the search terms.
    - Use a Search API: Consider using a search API that provides more advanced search capabilities.

How should the search function be refined? Yesterday, I was able to observe the effect of removing 'answer' from 'messages.  It appears to cause the model to respond with search phrases instead of individual terms. Providing the answer appears to give GPT confidence to narrowly focus on specific search terms. Therefor, I fear including all possible relevant terms from a test_item will have a negative impact on the end result.
In its current form, we are including a predefinde answer in our messages to GPT.

2. **Improve the Paragraph Selection**: Improve the `find_terms_in_same_paragraph` function to select the most relevant paragraph instead of just the first one that contains the terms.
    `find_terms_in_same_paragraph` is meant to emulate the way I search for the most relevant content to the question.  I read the question, search for the best topic/subject/object I can think of and ctrl+f the most relelvant terms on that page.  I think the best option on this step is to create more options to select from.
3. **Test the Functions**: Write unit tests for the functions to ensure they are working as expected.

4. **Integration**: Once the individual functions are working as expected, integrate them and test the whole system.

5. **Iterate and Improve**: Based on the results, iterate and improve the functions. Tweak the search terms generation or the paragraph selection process as needed.

6. **Scale Up**: Once satisfied with the performance on a single test item, scale up the process to handle multiple test items.

7. **Performance Optimization**: Look for ways to optimize the performance of the system, such as parallel processing or caching search results.

8. **Documentation**: Document the code and the system architecture for code maintenance and for other team members who might join the project.

## File/Function Descriptions
### `improved_retrieval.py`
Data Loading: The script begins by loading a CSV file into a pandas DataFrame, a data structure that's ideal for data manipulation and analysis. It then selects a single row from this DataFrame for further processing.
Test Item Creation: The script constructs a test item by combining various elements from the selected row. This includes the prompt and all the options (A, B, C, D, E), as well as the answer.
Search Term Extraction: The script leverages the capabilities of the OpenAI GPT-3.5-turbo model to generate the top three search terms from the test item. This is a crucial step as it determines the keywords that will be used for the subsequent information retrieval process.
Data Cleaning: The script includes a function that cleans the first search term. This involves removing everything inside parentheses, all non-alphabetical characters except spaces, and spaces from the end of the string. This step ensures that the search term is in a suitable format for the next stage.
Wikipedia Search: The script then searches Wikipedia using the cleaned search term and retrieves the content of the first two pages. This is done using a function that interacts with the Wikipedia API.
Paragraph Extraction: Finally, the script includes a function that finds paragraphs in the Wikipedia content that contain the second and third search terms. This is a key step in pinpointing the most relevant information related to the test item.
The script concludes by printing out the paragraphs that contain both search terms, providing a concise summary of the most relevant information.
