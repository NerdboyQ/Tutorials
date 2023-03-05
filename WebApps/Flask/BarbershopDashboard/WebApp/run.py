from flask import Flask, render_template

app = Flask("Fades to Twists")


@app.route('/')
def hello():
    return render_template('main_dashboard.html')

# This run my webapp and it starts it with my compatur as the server.
app.run(host="0.0.0.0",port=5000,debug=True)