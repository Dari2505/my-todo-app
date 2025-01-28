import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +"\n" #session_state is some kind of dictionary
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo APP.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
   checkbox = st.checkbox(todo, key = todo) #every element of todo.txt has a key.
                                            # In this way we can manipulate an item by
                                            # grabbing at its key
   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.rerun()  #No explanation what it does. But it is needed for checkboxes


st.text_input(label="Enter a todo: ", placeholder = "Add new todo...",
              on_change = add_todo, key = "new_todo")

st.session_state