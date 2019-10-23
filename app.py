from flask import Flask, url_for, redirect, render_template, request
import DatabaseLibrary as db


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def display_home_page():
    return render_template('sample.html', **locals())


@app.route("/user-create-new-user", methods=['POST'])
def create_user():
    # Get the info form the frontend
    data = request.get_json()
    username = data['username']
    commonName = data['commonName']
    email = data['email']
    phone = data['phone']
    birthday = data['birthday']
    description = data['description']
    # db.newUser(username, commonName, email, phone, birthday, description)

    return '''
    Created User!
    username: {}
    commonName: {}
    email: {}
    phone: {}
    birthday: {}
    description: {}
    '''.format(username, commonName, email, phone, birthday, description)


@app.route("/user-update-common-name")
def update_common_name():
    # Get the info from the frontend
    userId = 0  # Stored in the background of the front end
    newCommonName = "new Common Name"

    db.updateCommonName(userId, newCommonName)

    return render_template('sample.html', **locals())


@app.route("/user-update-phone")
def update_phone_number():
    # Get the info from the database
    userId = 0  # Stored in the background of the front end
    newPhoneNumber = "222-222-2222"

    db.updatePhone(userId, newPhoneNumber)

    return render_template('sample.html', **locals())


@app.route("/user-update-description")
def update_description():
    # Get the info from the database
    userId = 0  # Stored in the background of the front end
    newDescription = "new description"

    db.updateDescription(userId, newDescription)

    return render_template('sample.html', **locals())


@app.route("/user-add-new-user-topic")
def add_user_topic():
    # Get the info from the database
    userId = 0  # Stored in the background of the front end
    newTopic = "Topic"

    db.newUserTopic(userId, newTopic)

    return render_template('sample.html', **locals())


@app.route("/user-get-user-timeline")
def get_user_timeline():
    # Get the info from the database
    userId = 0  # The user ID of the timeline to show

    db.getUserTimeline(userId)

    return render_template('sample.html', **locals())


@app.route("/user-get-user-posts")
def get_user_posts():
    # Get the info from the database
    userId = 0  # The user ID of the posts to show

    db.getUserPosts(userId)

    return render_template('sample.html', **locals())


@app.route("/user-delete")
def delete_user():
    # Get the info from the database
    userId = 0  # The user ID to delete

    db.deleteUser(userId)

    return render_template('sample.html', **locals())


@app.route("/follow-user")
def follow_new_user():
    # Get the info from the database
    userId = 0  # The user ID requesting a new follow
    followingId = 1  # The id of the user who userId wants to follow

    db.newFollow(userId, followingId)

    return render_template('sample.html', **locals())



@app.route("/unfollow")
def unfollow_user():
    # Get the info from the database
    userId = 0  # The user ID requesting a new follow
    followingId = 1  # The id of the user who userId wants to unfollow

    db.unfollowUser(userId, followingId)

    return render_template('sample.html', **locals())


@app.route("/follow-users-topics")
def follow_user_topics():
    # Get the info from the database
    userId = 0  # The user ID requesting a new follow
    followingId = 1  # The id of the user who userId wants to follow
    topicsSelected = []

    db.updateFollow(userId, followingId, topics=topicsSelected)

    return render_template('sample.html', **locals())


@app.route("/validate-email")
def validate_email():
    # Get the info from the database
    email = "email"  # The user ID requesting a new follow

    db.validateEmail(email)

    return render_template('sample.html', **locals())


@app.route("/validate-username")
def validate_usernmae():
    # Get info
    username = "user"
    db.validateUsername(username)

    return render_template('sample.html', **locals());


@app.route("/get-user-id-from-email")
def get_id_from_email():
    email = "email"
    db.getUserId(email)
    return render_template('sample.html', **locals())


@app.route("/create-post")
def post():
    userId = 0;
    postText = "This is a post"
    topics = "topics"
    db.newPost(userId, postText, topics)
    return render_template('sample.html', **locals())


@app.route("/get-all-posts")
def get_all_posts():
    db.getAllPosts()
    return render_template('sample.html', **locals())


@app.route("/get-topic-posts")
def get_all_topic_posts():
    topic = "topic"
    db.getAllTopicPosts(topic)
    return render_template('sample.html', **locals())


@app.route("/delete-post")
def delete_post():
    postId = 0;
    db.deletePost(postId)
    return render_template('sample.html', **locals())


@app.route("/dm-user")
def dm_user():
    senderId = 0;
    receiverId = 1;
    message = "This is a message"
    db.newDm(senderId, receiverId, message)
    return render_template('sample.html', **locals())




if __name__ == '__main__':
    app.run(debug=True)
