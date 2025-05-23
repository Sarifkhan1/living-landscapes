from flask import Flask, render_template, request
from generate_image import generate_image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    image_path = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        image_path = generate_image(prompt)
    return render_template("index.html", image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
