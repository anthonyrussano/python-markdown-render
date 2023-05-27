from flask import Flask, render_template, send_from_directory
import mistune
import os

app = Flask(__name__)
markdown_directory = 'source'  # Replace with the path to your directory containing markdown files


@app.route('/')
def render_index():
    tree = get_folder_structure(markdown_directory)
    return render_template('index.html', tree=tree)


@app.route('/view/<path:filename>')
def render_markdown(filename):
    filepath = os.path.join(markdown_directory, filename)
    if os.path.isfile(filepath):
        with open(filepath) as file:
            markdown_text = file.read()
        html = mistune.markdown(markdown_text)
        return render_template('markdown.html', content=html, filename=filename)
    return 'File not found'


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


def get_folder_structure(directory):
    tree = {}
    for root, dirs, files in os.walk(directory):
        current_dir = tree
        path = root.replace(directory, '').lstrip(os.path.sep)
        if path:
            for folder in path.split(os.path.sep):
                current_dir = current_dir.setdefault(folder, {})
        for file in files:
            current_dir[file] = ''
    return tree

if __name__ == '__main__':
    app.run(host='10.32.25.124', port=8080)
