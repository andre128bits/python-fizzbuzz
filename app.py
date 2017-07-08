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
            background: #ffffff;
            background: #888888;
        }}
        </style>
        <title>TRABALHO ANDRE WOHLFAHRT</title>
    </head>
    <body backgroundcolor=#00ff00>
        <center><h1>Metodos Ageis Uniritter - Professor Daniel Wildt</h1></center>
        <br><br><br><br><br><br><br><br><br><br>
        <p><font color=red>Teste de Deploy {time}.</font></p>

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
