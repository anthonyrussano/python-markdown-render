from flask import Flask, render_template
import mistune

app = Flask(__name__)

@app.route('/')
def render_markdown():
    with open('your_file.md') as file:
        markdown_text = file.read()
    html = mistune.markdown(markdown_text)
    return render_template('index.html', content=html)

if __name__ == '__main__':
    app.run(host='10.32.25.124', port=8080)