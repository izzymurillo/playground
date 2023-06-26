from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/play')
def three_blue():
    return render_template("index.html") * 3

@app.route('/play/<int:num_times>')
def display_x_times(num_times):
    return render_template("index.html") * (num_times)

#GOT STUCK :(

if __name__=="__main__":
    app.run(debug=True)