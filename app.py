from flask import Flask, render_template, request
from PIL import Image, ImageOps
import os

from ascii import ascii_art  # or paste function directly here

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ascii_output = None

    if request.method == "POST":
        file = request.files["image"]
        img = Image.open(file.stream)

        width = int(request.form.get("width") or 100)
        width = max(20, min(width, 300))
        bg_color = request.form.get("invert")
        brightness = float(request.form.get("brightness") or 1.0)
        contrast = float(request.form.get("contrast") or 1.0)
        aspectratiomultiplier=float(request.form.get("multiplier") or 0.55)

        invert = request.form.get("invert")
        if invert:  # convert to True/False
            img = ImageOps.invert(img)

        dither = bool(request.form.get("dither"))
        if dither:
            img = img.convert("1").convert("L")

        ascii_output = ascii_art(img, width, bg_color, brightness=brightness, contrast=contrast, aspratm=aspectratiomultiplier)
        return ascii_output


    return render_template("index.html", ascii_output=ascii_output)

if __name__ == "__main__":
    app.run(debug=True)