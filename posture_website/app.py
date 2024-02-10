from flask import Flask, render_template, jsonify
import os
import time
import json

app = Flask(__name__)

# Route to serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch new images
@app.route('/new_images')
def new_images():
    image_names = os.listdir('static/images')
    image_names = [name for name in image_names if name.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    # Get the modification time (timestamp) of each image
    image_info = [{'name': name, 'timestamp': os.path.getmtime(os.path.join('static/images', name))} for name in image_names]

    # # Convert image_info to a JSON string and print it
    # json_str = json.dumps(image_info, indent=4)  # Convert to JSON string with pretty print
    # print(json_str)


    return jsonify(image_info)

if __name__ == '__main__':
    app.run(debug=True)
