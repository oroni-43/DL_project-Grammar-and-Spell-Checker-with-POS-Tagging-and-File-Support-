from flask import Flask, request, render_template, send_file
from checker_model import GrammarSpellChecker

app = Flask(__name__)
checker = GrammarSpellChecker()

@app.route('/')
def home():
    examples = checker.dataset.sample(5).to_dict(orient='records')
    return render_template('index.html', examples=examples)

@app.route('/spell', methods=['POST'])
def process_text():
    text = request.form['text']
    results = checker.full_correction(text)
    pos_info = checker.pos_tagging(results['final_corrected'])
    examples = checker.dataset.sample(5).to_dict(orient='records')

    return render_template('index.html',
        spelling_corrected=results['spelling_corrected'],
        grammar_corrected=results['grammar_corrected'],
        corrected_text=results['final_corrected'],
        corrected_grammar=results['grammar_issues'],
        pos_info=pos_info,
        examples=examples
    )

@app.route('/grammar', methods=['POST'])
def process_file():
    file = request.files['file']
    content = file.read().decode('utf-8')

    results = checker.full_correction(content)
    pos_info = checker.pos_tagging(results['final_corrected'])
    examples = checker.dataset.sample(5).to_dict(orient='records')

    with open('corrected_output.txt', 'w', encoding='utf-8') as f:
        f.write(results['final_corrected'])

    return render_template('index.html',
        spelling_corrected=results['spelling_corrected'],
        grammar_corrected=results['grammar_corrected'],
        corrected_text=results['final_corrected'],
        corrected_grammar=results['grammar_issues'],
        pos_info=pos_info,
        examples=examples
    )

@app.route('/download_corrected')
def download():
    return send_file('corrected_output.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
