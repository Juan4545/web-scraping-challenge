from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")



@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", dict_mars=destination_data)


@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_scrap = scrape_mars.nasa_mars_news()
    mars_scrap = scrape_mars.featured_image_url()
    mars_scrap = scrape_mars.mars_weather()
    mars_scrap = scrape_mars.Mars_facts()
    mars_scrap = scrape_mars.Mars_Hemispheres()


    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_scrap, upsert=True)
    

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
