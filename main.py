# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from openai import OpenAI
from pprint import pprint
client = OpenAI(
        api_key=""
    )
pattern = re.compile(r'<span class=clozed>(.+?)</span>')


def process_clozed_span(match):
    """
    This function is called for every match found by re.sub().
    It takes the content, splits it into words, and wraps each word
    in its own clozed span.
    """
    # group(1) contains the text captured inside the parentheses of our pattern
    # e.g., "bei Hempels unterm Sofa"
    content = match.group(1)

    # Split the content into a list of words
    # e.g., ['bei', 'Hempels', 'unterm', 'Sofa']
    words = content.split()



def compute_gemini(word):
    model = genai.GenerativeModel('gemini-2.5-flash')  # Or 'gemini-1.5-pro' for more advanced capabilities

    # Gemini's prompt structure is slightly different.
    # We'll use a chat-like format for turn-based conversation.
    messages = [
        {"role": "user",
         "parts": [
             "Der Benutzer möchte immer drei Beispielsätze, in denen das Beispielwort mit '<span class=clozed>' und '</span>' umgeben ist, und eine kurze Bedeutung, in dem Teil Bedeutung sollte das Wort selbst nicht erwähnt sein"]},
        {"role": "user",
         "parts": [
             "zuvorkommend"]},
        {"role": "model",
         "parts": [
             "1. Die Kellnerin war äußerst <span class=clozed>zuvorkommend</span> und las uns jeden Wunsch von den Lippen ab.<br><br>2. Er zeigte sich als sehr <span class=clozed>zuvorkommend</span>, indem er der alten Dame die Tür aufhielt.<br><br>3. Sein <span class=clozed>zuvorkommendes</span> Verhalten machte einen positiven Eindruck auf alle.<br><br><br><br>Bedeutung: Höflich, hilfsbereit und darauf bedacht, den Wünschen anderer entgegenzukommen."]},
        {"role": "user",
         "parts": [
             "im Begriff sein, etw. zu tun"]},
        {"role": "model",
         "parts": [
             "1. Er war <span class=clozed>im Begriff</span>, das Büro zu verlassen, als sein Telefon klingelte.\n\n2. Sie ist <span class=clozed>im Begriff</span>, die letzte Entscheidung zu treffen, also sei leise.\n\n3. Wir waren <span class=clozed>im Begriff</span>, die Sitzung zu beenden, als der Chef noch eine Ankündigung machte.\n\nBedeutung: Kurz davor stehen, eine Handlung auszuführen oder eine Entscheidung zu treffen."]},

        {"role": "user",
         "parts": [word]}
    ]

    response = model.generate_content(
        messages,
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=1000000,
            temperature=1  # You might want to adjust this for creativity/determinism
        )
    )


    # The way to access the generated text is different for Gemini

    return response.candidates[0].content.parts[0].text

def compute(word):


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer",
             "content": "Der Benutzer möchte immer drei Beispielsätze, in denen das Beispielwort mit '<span class=clozed>' und '</span>' umgeben ist, und eine kurze Bedeutung, in dem Teil Bedeutung sollte das Wort selbst nicht erwähnt sein"},

            {
                "role": "assistant",
                "content": [{"type": "text", "text": "1. Die Kellnerin war äußerst <span class=clozed>zuvorkommend</span> und las uns jeden Wunsch von den Lippen ab.<br><br>2. Er zeigte sich als sehr <span class=clozed>zuvorkommend</span>, indem er der alten Dame die Tür aufhielt.<br><br>3. Sein <span class=clozed>zuvorkommendes</span> Verhalten machte einen positiven Eindruck auf alle.<br><br><br><br>Bedeutung: Höflich, hilfsbereit und darauf bedacht, den Wünschen anderer entgegenzukommen."}]
            },

            {
                "role": "user",
                "content": word
            }
        ],
        max_completion_tokens=500,
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
                example_sentence = compute(word).replace('\n', '<br>')
                if len(word) == 1000:
                    example_sentence.replace(word, f'<span class=clozed>{word}</span>')



            edited_split_line = [split_line[0], split_line[1], split_line[2], split_line[3], word, example_sentence]
            edited_line = '\t'.join(edited_split_line)
            edited_lines.append(edited_line)
        else:
            edited_lines.append(line)

    with open("EditedNotes.txt", "w") as file:
        with open("EditedNotes.txt", "w", encoding="cp1252", errors="ignore") as file:
            file.write('\n'.join(edited_lines))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
    ankii()
