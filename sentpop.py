import json
from transformers import BertTokenizer
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
x = tokenizer.tokenize("看看是啥")
y = tokenizer.convert_tokens_to_string(x)


class sentpop:
    def __init__(self):
        self.data = {}

    def add_block(self, date, text, total_score, scores):
        if date not in self.data:
            self.data[date] = {}
        self.data[date][text] = {
            'normalized_score': total_score,
            'scores': scores
        }

    def to_json_string(self):
        return json.dumps(self.data)

    #for deserializing JSON data into Python objects
    #cls is a convention for referring to the class itself within a class method
    def from_json_string(cls, json_string):
        instance = cls()
        instance.data = json.loads(json_string)
        return instance


#for testing purposes
sent_data = sentpop()
sent_data.add_block('2023-12-19', 'block 1 text', 200, [{'score1': 100, 'score2': 100}])
sent_data.add_block('2023-12-19', 'block 2 text', 200, [{'score1': 100, 'score2': 100}])
print(sent_data.data)

def block_split(file_path, token_limit=512):
    #returns a string of split blocks
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Splitting by blocks (bullet points)
    blocks = text.split('\n- ')

    # Further splitting large blocks
    split_blocks = []
    for block in blocks:
        # Prepend the bullet point for all but the first block
        if block != blocks[0]:
            block = '- ' + block

        # nltk module that split the block into sentences
        sentences = sent_tokenize(block)
        current_chunk = ""
        for sentence in sentences:
            # Check if adding the next sentence exceeds the token limit
            if len(tokenizer.tokenize(current_chunk + sentence)) > token_limit:
                # If the current chunk is full, add it to the split_blocks list
                split_blocks.append(current_chunk.strip())
                current_chunk = sentence
            else:
                current_chunk += " " + sentence

        # Add the last chunk if it's not empty
        if current_chunk:
            split_blocks.append(current_chunk.strip())

    return split_blocks


# Example usage
#file_path = ""
#blocks = block_split(file_path)

'''
for i, block in enumerate(blocks):
    print(f"Block {i+1}:\n{block}\n---\n")
'''

def split_text_by_percentage(old_text, text, split_percentage):
    """
    Splits a block of text into two parts based on the given percentage.

    :param text: The text to be split.
    :param split_percentage: The percentage at which to split the text. 
                             Should be a float between 0.0 and 1.0.
    :return: A tuple containing the two parts of the text.
    """
    # Calculate the split index
    split_index = int(len(old_text) * split_percentage)

    # Split the text
    part1 = text[:split_index]

    return part1
