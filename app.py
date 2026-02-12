import os
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 1. Configuration (Must come before db initialization)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waste_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. Initialize Database
db = SQLAlchemy(app)

# Create upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# 3. Database Model
class WasteItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    image_path = db.Column(db.String(200), nullable=False)

# Create the database file
with app.app_context():
    db.create_all()

# 4. Simple HTML Template
HTML_TEMPLATE = '''
<!doctype html>
<html>
<head><title>Waste Collector</title></head>
<body style="font-family: sans-serif; padding: 20px;">
  <h2>Waste Category Data Collector</h2>
  <form method="post" enctype="multipart/form-data">
    <input type="file" name="file" required><br><br>
    <label>Select Category:</label><br>
    <select name="category" style="padding: 5px;">
      <option value="Plastic">Plastic</option>
      <option value="Paper">Paper</option>
      <option value="Metal">Metal</option>
      <option value="Organic">Organic</option>
      <option value="Glass">Glass</option>
    </select><br><br>
    <button type="submit" style="padding: 10px 20px; cursor: pointer;">Upload & Save</button>
  </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        category = request.form['category']
        
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Save metadata to SQLite
            new_item = WasteItem(category=category, image_path=filepath)
            db.session.add(new_item)
            db.session.commit()
            
            return f"<h3>Success!</h3><p>Uploaded as <b>{category}</b>. <a href='/'>Upload another?</a></p>"
            
    return HTML_TEMPLATE

if __name__ == '__main__':
    app.run(debug=True)