# Import libraries
from flask import Flask, request
from like_db import LikeDB
# Create an instance of Flask
app = Flask(__name__)
likeDB = LikeDB('like_api/like_db.json')
@app.route("/")
def home():
    return "Hello World!"

@app.route('/api/add-like/', methods=['POST'])
def addLike():
    # get data from request
    data = request.get_json(force=True)

    # user_id, img_id
    user_id = data['user_id']
    img_id = data['image_id']

    # like img
    likeDB.add_like(user_id, img_id)

    return {'status': 200}


@app.route('/api/add-dislike/', methods=['POST'])
def addDislike():
    # get data from request
    data = request.get_json(force=True)

    # user_id, img_id
    user_id = data['user_id']
    img_id = data['image_id']

    # dislike img
    likeDB.add_dislike(user_id, img_id)

    return {'status': 200}



@app.route('/api/<img_id>')
def get_data(img_id):
    data = likeDB.get_likes_dislike(img_id)


    return {
        "like": data[0],
        "dislike": data[1]
    }



# End point for getting image
@app.route("/api/addImage", methods=["POST"])
def addImage():
    # Get the image from the request
    if request.method == "POST":
        # Get json data from request
        data = request.get_json(force=True)
        # Get the image id from data
        image_id = data["image_id"]
        # Get the message id from data
        message_id = data["message_id"]
        likeDB.add_image(image_id, message_id)
        print(f'Image id: {image_id} Message id: {message_id}')

    return {}
        

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

