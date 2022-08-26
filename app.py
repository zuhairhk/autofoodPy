from flask import Flask, render_template, request
import locate
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def display():
    data = request.form['query']

    rlists = locate.main(data)[0]
    links = locate.main(data)[1]
    photo_refs = locate.main(data)[3]

    rannum = random.randint(0, len(rlists) - 1)

    rlist = rlists[rannum]
    link = links[rannum]
    loc_name = locate.main(data)[2][rannum]

    open_now = locate.main(data)[4][rannum]

    if open_now['open_now'] == True:
        open_status = 'Open'
    else:
        open_status = 'Closed'
    
    try:
        photo_ref = photo_refs[rannum][0]['photo_reference']
    except:
        photo_ref = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png'
        print('No image available')

    return render_template(
        'passed.html', 
        query = data, 
        list = rlist, 
        link = link,
        photo_ref = photo_ref,
        loc_name = loc_name,
        API_KEY = os.environ['API_KEY'],
        open_status = open_status,
        rating = locate.main(data)[5][rannum],
        vicinity = locate.main(data)[6][rannum],
    )

if __name__ == '__main__':
    app.run(debug=True)