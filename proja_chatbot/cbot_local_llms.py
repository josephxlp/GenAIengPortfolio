import gradio as gr
import ollama

# Mock function to simulate fetching a list from a database
def List_from_db():
    # Simulate fetching data from a database
    # Example: ['deepscaler:latest', 'deepseek-r1:1.5b', 'phi4:latest', ...]
    updated_list = [
        "deepscaler:latest",
        "deepseek-r1:1.5b",
        "phi4:latest",
        "llama3.2-vision:11b",
        "nomic-embed-text:latest",
        "codellama:latest",
        "llama3:8b",
        "llama3.2:1b"
    ]
    return updated_list

# Function to update the dropdown choices
def updatedList_from_db():
    list_info = List_from_db()
    return gr.Dropdown(choices=list_info, label="Select Model", value=list_info[0])

# Function to interact with the selected model
def chat_with_bot(user_message, model_choice):
    response = ollama.chat(model=model_choice, messages=[{"role": "user", "content": user_message}])
    return response["message"]["content"]

# Gradio Blocks interface
with gr.Blocks() as app:
    with gr.Row():
        # Dropdown for model selection
        dropdown_info = gr.Dropdown(choices=List_from_db(), label="Select Model", value=List_from_db()[0])
        # Button to update the dropdown
        update_btn = gr.Button("Update Dropdown")

    with gr.Row():
        # Textbox for user input
        user_input = gr.Textbox(label="Chat Message")
        # Textbox for bot response
        bot_output = gr.Textbox(label="Bot Response")

    # Button to trigger the chat function
    chat_btn = gr.Button("Send Message")

    # Update dropdown when the update button is clicked
    update_btn.click(updatedList_from_db, inputs=[], outputs=dropdown_info)

    # Trigger the chatbot function when the send button is clicked
    chat_btn.click(chat_with_bot, inputs=[user_input, dropdown_info], outputs=bot_output)

# Launch the app
if __name__ == "__main__":
    app.launch(share=True)