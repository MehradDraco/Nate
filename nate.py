from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.widgets import TextArea
from prompt_toolkit.layout import Layout
import os

def load_file(filename):
    """Load existing file content or create a new one."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    return ""

def save_file(filename, text):
    """Save file content."""
    with open(filename, 'w') as file:
        file.write(text)
    print("\nSaved successfully! Exiting...")

def nate_text_editor(filename):
    """Interactive CLI-based text editor using prompt_toolkit."""
    text = load_file(filename)
    
    # Create a TextArea for interactive editing
    text_area = TextArea(text=text, scrollbar=True)

    # Define key bindings
    bindings = KeyBindings()

    @bindings.add("c-x")  # Ctrl+X to Save & Exit
    def _(event):
        save_file(filename, text_area.text)
        event.app.exit()

    # Create application with layout
    app = Application(
        layout=Layout(container=text_area),
        key_bindings=bindings,
        full_screen=True
    )

    print(f"Editing: {filename} (Press Ctrl+X to Save & Exit)")
    app.run()

if __name__ == "__main__":
    filename = input("Enter filename to edit: ").strip()
    nate_text_editor(filename)
