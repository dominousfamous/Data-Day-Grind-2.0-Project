from flask import Blueprint, render_template, redirect, render_template
import requests

#Configure blueprint
views = Blueprint("views", __name__)

#Contacting API method
def contact():
    try:
        url = "https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true"
        response = requests.get(url)
        response.raise_for_status()
    except:
        return None

    try:
        quote = response.json()
        return quote

    except:
        return None


#Start of Routes
@views.route("/impact")
def index():
    
    #Immediately get updated COVID data 
    table = contact()
    length = len(table)
    return render_template("impact.html", length = length, table = table)

    



