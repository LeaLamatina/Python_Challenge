from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
  mars = mongo.db.collection.find()
  return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraper():
  mars = mongo.db.mars
  mars_data = scrape_mars.scrape()
  mars.update({}, mars_dictionary, upsert=True)
  return redirect("/", code=302)

if __name__ == "__main__":
  app.run(debug=True)