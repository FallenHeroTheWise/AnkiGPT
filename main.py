# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from openai import OpenAI
from pprint import pprint
client = OpenAI(
        api_key=""
    )





def compute(word):


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer",
             "content": "Der Benutzer möchte immer drei Beispielsätze und eine kurze Bedeutung, in dem Teil Bedeutung sollte das Wort selbst nicht erwähnt sein"},
            {
                "role": "user",
                "content": word
            }
        ],
        max_completion_tokens=300,
        n=1,

    )
    pprint(response)
    return response.choices[0].message.content

def ankii():
    with open("Selected Notes.txt", "r") as file:
        text = file.read()


    lines = text.split('\n')
    edited_lines=[]
    for line in lines:
        split_line=line.split('\t')
        if len(split_line) == 6:

            word=split_line[4]

            if True:
                example_sentence = compute(word).replace('\n', '   ')



            edited_split_line = [split_line[0], split_line[1], split_line[2], split_line[3], word, example_sentence]
            edited_line = '\t'.join(edited_split_line)
            edited_lines.append(edited_line)
        else:
            edited_lines.append(line)

    with open("EditedNotes.txt", "w") as file:
        file.write('\n'.join(edited_lines))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
    ankii()
