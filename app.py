from flask import Flask
from datetime import datetime

from fizzbuzz import fizzbuzz

app = Flask(__name__)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        pre {{
            background: #ffBF00;
            background: #CCCCCC;
        }}
        </style>
        <title>TRABALHO ANDRE WOHLFAHRT</title>
    </head>
    <body>
        <h1>Metodos Ageis Uniritter - Professor Daniel Wildt</h1>
        <p>
        <p>
        <p>Teste de Deploy {time}.</p>

        <pre>
{result}
        </pre>
    </body>
    </html>
    """.format(time=the_time,
               # result="\n".join([fizzbuzz(i) for i in range(1, 101)]),
               result="\n".join(list(map(fizzbuzz, range(1, 101))))
               )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
