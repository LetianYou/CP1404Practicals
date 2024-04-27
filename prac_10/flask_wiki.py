from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the main page with a search form or process the search query if method is POST."""
    if request.method == 'POST':
        query = request.form['query']
        try:
            page = wikipedia.page(query)
            title = page.title
            summary = page.summary
            return render_template('result.html', title=title, summary=summary)
        except wikipedia.exceptions.PageError:
            return render_template('error.html', message="Page not found.")

    return render_template('index.html')


app.run(debug=True)
