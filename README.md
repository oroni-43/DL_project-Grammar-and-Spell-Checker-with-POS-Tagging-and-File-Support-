This project, titled "Grammar and Spell Checker with POS Tagging and File Support," is an intelligent,
web-based application designed to assist users in writing more accurately by automatically detecting and 
correcting grammar and spelling mistakes. Developed using Python and the Flask web framework, the system 
provides two main options: users can either type a sentence directly into a text area or upload a .txt file
for bulk correction. Once the input is submitted, it undergoes a two-phase correction process. First, 
TextBlob, a popular NLP library, performs spelling correction by analyzing and suggesting the most likely 
correct form of misspelled words. Then, the corrected text is passed to GingerIt, which applies rule-based 
grammar correction, identifying grammatical inconsistencies and improving sentence structure in context.

To enhance the grammatical understanding of each sentence, the system also incorporates Part-of-Speech (POS) 
tagging using spaCy, a powerful NLP library that assigns grammatical roles (such as nouns, verbs, adjectives,
etc.) to each word. This feature is useful for both learners and professionals who want to understand sentence 
structure more deeply. The corrected outputs are displayed in a clean, user-friendly interface built with HTML, 
CSS, and Bootstrap, separated into well-labeled sections such as Spelling Correction, Grammar Correction, Final 
Corrected Output, and POS Tags. Furthermore, the application includes a dataset example section, where users 
can view pairs of incorrect and corrected sentences. This gives insight into how the model was trained and 
builds trust in the correction engine.

For longer documents, users can upload .txt files, which are read and processed in the same way as direct text 
inputs. Once the corrections are completed, users can download a fully corrected version of their file. The 
system is particularly valuable for students, content creators, and professionals who require quick yet 
reliable grammar feedback. To run the project locally, the user must install several Python libraries including 
flask, textblob, gingerit, and spacy, and must also download the English language model (en_core_web_sm) and text 
corpora. By combining rule-based techniques and machine learning-trained logic, this project demonstrates how 
natural language processing can effectively support intelligent text correction in real-world use cases.
