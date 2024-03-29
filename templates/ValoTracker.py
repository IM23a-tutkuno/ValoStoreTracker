import valorantstore
import requests
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, request

app = Flask(__name__, )
app.secret_key = "  "
app = Flask(__name__, template_folder='templates')

def login_apirequest(username, password, region):
    valorant_store = valorantstore.ValorantStore(
        username=username,
        password=password,
        region=region,
        sess_path=None,
        proxy=None)
    valostore = valorant_store.store(True)
    del valostore['bundles']
    valostore = valostore['daily_offers']
    image_links = [data['image'] for data in valostore['data']]
    skins = []
    for skin in image_links:
        skins.append(skin)


    return render_template('skinsscreen.html',
                           image_links=image_links)



@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        region = request.form.get("region")
        return login_apirequest(username, password, region)
    return render_template('ValoTrackerSite.html')



def getimg(link, counter):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }
    images = []
    images.append(link)
    response = requests.get(f'{images[0]}', headers=headers)
    image = Image.open(BytesIO(response.content))
    image.show()


if __name__ == "__main__":
    app.run(debug=True)