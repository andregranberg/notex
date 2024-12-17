import streamlit as st
import json
import os

# Define the file path to store notes
NOTES_FILE = "notes.json"

# Function to load notes from a file
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save notes to a file
def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

# Load existing notes
notes = load_notes()

# Custom CSS to style the text area
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 150px; /* Adjust the height as needed */
        width: 100%;   /* Adjust the width as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Add Note", "Search Notes"])

if page == "Add Note":
    # Streamlit app title
    st.title("Add a New Note")

    # Input for new note
    new_note = st.text_area("Write a new note:")

    # Button to add a new note
    if st.button("Add Note"):
        if new_note.strip():
            notes.append(new_note.strip())
            save_notes(notes)
            st.success("Note added successfully!")
            st.rerun()
        else:
            st.warning("Please write something in the note field.")

elif page == "Search Notes":
    # Streamlit app title
    st.title("Search Notes")

    # Input for search query
    search_query = st.text_input("Search for a note:")

    # Display matching notes
    if search_query:
        st.subheader("Search Results:")
        found_notes = [note for note in notes if search_query.lower() in note.lower()]
        if found_notes:
            for i, note in enumerate(found_notes):
                st.text(f"Note {i+1}: {note}")
        else:
            st.info("No notes found matching your query.")
    else:
        st.subheader("Your Notes:")
        for i, note in enumerate(notes):
            st.text(f"Note {i+1}: {note}")
            if st.button(f"Delete Note {i+1}", key=f"delete_{i}"):
                notes.pop(i)
                save_notes(notes)
                st.success("Note deleted successfully!")
                st.rerun()

# Footer
st.markdown("---")