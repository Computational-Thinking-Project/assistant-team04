# Chat UI placeholder

`index.html` is a static preview of the Smart Virtual Assistant's chat page. It shows a question input and an answer area, but it is *not connected to the backend yet*. The Send button is intentionally disabled.

## Open the preview

Open `ui/index.html` in a web browser. No server or Streamlit installation is needed. You can type in the input box; the answer area currently displays placeholder text.

## Planned backend connection

A future Streamlit page will take the user's question, call the existing Python function, and display the returned answer:
```bash
from assistant.rules import reply

answer = reply(message)
```
`reply(message)` returns a text response using the project's rules and office data. The static HTML page cannot call this Python function directly. Connecting them and building a working Streamlit app are outside issue #39.

## Preview image

See [the chat-page screenshot](../docs/ui-chat-placeholder.png).