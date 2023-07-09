import os
import tkinter as tk
import openai

# Set your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_content():
    # Get input words from the entry widget
    input_words = entry.get()

    # Generate content using the OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input_words,
        max_tokens=500,
        top_p=0.7,
        n=1,
        logprobs=0
    )

    # # Print the response JSON for debugging
    # print(response)

    try:
        # Get the generated content from the API response
        completions = response.choices
        completions.sort(key=lambda c: c.logprobs.token_logprobs[0], reverse=True)
        generated_content = completions[0].text.strip()

        # Display the generated content in the text widget
        text.delete('1.0', tk.END)
        text.insert(tk.END, generated_content)
    except (AttributeError, IndexError) as e:
        print(f"Error: {e}")
        # Handle the error or display an appropriate message to the user

window = tk.Tk()

window.title("Content Generator")
window.configure(bg='#36454F')
label = tk.Label(window, foreground='white', text='Enter the Keyword', background='#36454F')
label.pack(pady=5)
entry = tk.Entry(window, width=50, background='#28282B', foreground='white')
entry.pack(pady=5)

button = tk.Button(window, text="Generate", command=generate_content)
button.pack(pady=10)

text = tk.Text(window, height=10, width=50, background='#36454F', foreground='white')
text.pack()

window.mainloop()
