from flask import Flask, url_for, redirect, render_template, request
import DatabaseLibrary as db


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def display_home_page():
    return render_template('sample.html', **locals())

# TODO: Un-comment all the calls to the database

@app.route("/user-create-new-user", methods=['POST'])
def create_user():
    """
    This function is used to create a new user and push it to the database. In
      order to use this function, make a POST request to function url above and
      send a json file with the appropriate information.
    :return: Display information about the newly created user.
    """

    #  Get the from the json file sent with the request
    data = request.get_json()

    username = data['username']
    commonName = data['commonName']
    email = data['email']
    phone = data['phone']
    birthday = data['birthday']
    description = data['description']

    #  Push the info to the database
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


@app.route("/user-update-common-name", methods=['POST'])
def update_common_name():
    """
    This function is used to update a user's common name in the database.
    :return: Display information about about the call.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']
    newCommonName = data['newCommonName']

    #  Push the info to the database
    # db.updateCommonName(userId, newCommonName)

    return """
Updated Users Common Name!
  userID: {}
  newCommonName: {}
""".format(userId, newCommonName)


@app.route("/user-update-phone", methods=['POST'])
def update_phone_number():
    """
    This function is used to update a user's phone number.
    :return: Display information about the updated information.
    """
    #  Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']
    newPhoneNumber = data['newPhoneNumber']

    #  Push the info to the database
    # db.updatePhone(userId, newPhoneNumber)

    return """
Updated User Phone Number!
  userId: {}
  newPhoneNumber: {}
""".format(userId, newPhoneNumber)


@app.route("/user-update-description", methods=['POST'])
def update_description():
    """
    This function is called to update a user's description.
    :return: Display information about the updated information.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data["userId"]
    newDescription = ["newDescription"]

    # Send the info to the database
    # db.updateDescription(userId, newDescription)

    return """
Updated Description!
  userId: {}
  newDescription: {}
""".format(userId, newDescription)


@app.route("/user-add-new-user-topic", methods=['POST'])
def add_user_topic():
    """
    This function is used to add a new topic to the user's profile.
    :return: Display information about the function call.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']
    newTopic = data['newTopic']

    # db.newUserTopic(userId, newTopic)

    return """
Added a new Topic!
  userId: {}
  newTopic: {}
""".format(userId, newTopic)


@app.route("/user-get-user-timeline", methods=['POST'])
def get_user_timeline():
    """
    This function is used to get the timeline of a specific user
    :return: Display information about the timeline
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']

    # TODO: Figure out what how to send all of the rows back to the front end
    #  for display

    # rows = db.getUserTimeline(userId)

    return """
Retireved Timeline!
  userId: {}
""".format(userId)


@app.route("/user-get-user-posts")
def get_user_posts():
    """
    This function is used to get all of the posts of the specific user.
    :return: Display information about the posts.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']

    # rows = db.getUserPosts(userId)

    return """
Retrieved User Posts!
  userId: {}
""".format(userId)


@app.route("/user-delete")
def delete_user():
    """
    This function is called in order to delete a user.
    :return: Display information about deleted user
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']

    # db.deleteUser(userId)

    return """
Deleted User!
  userId: {}
""".format(userId)


@app.route("/follow-user")
def follow_new_user():
    """
    This function is used to follow a new user.
    :return: Display information about the update.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']
    followingId = data['followingId']

    # db.newFollow(userId, followingId)

    return """
Followed a new user!
  userId: {}
  followingId: {}
""".format(userId, followingId)



@app.route("/unfollow")
def unfollow_user():
    """
    This function is used to unfollow a user.
    :return: Display information about the action.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']
    followingId = data['followingId']

    # db.unfollowUser(userId, followingId)

    return """
Unfollowed User!
  userId: {}
  followingId: {}
""".format(userId, followingId)


@app.route("/follow-users-topics")
def follow_user_topics():
    """
    This function is used to update the database to include following a user's
      topics.
    :return: Display information about the action.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']
    followingId = data['followingId']
    topicsSelected = data['topicsSelected']

    # db.updateFollow(userId, followingId, topics=topicsSelected)

    return """
Followed a user's topics!
  userId: {}
  followingId: {}
  topicsSelected: {}
""".format(userId, followingId, topicsSelected)


@app.route("/validate-email", methods=['POST'])
def validate_email():
    """
    This function is used to validate a given user's email.
    :return: Return a boolean that determines validation
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    email = data['email']  # The user ID requesting a new follow

    # db.validateEmail(email)

    return """
Email successfully validated!
  email: {}
""".format(email)


@app.route("/validate-username")
def validate_usernmae():
    """
    This function is used to validate a given user's username.
    :return: Return a boolean that determines validation
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    username = ['user']
    # db.validateUsername(username)

    return """
    Username successfully validated!
    username: {}
    """.format(username)


@app.route("/get-user-id-from-email")
def get_id_from_email():
    """
    This function is used to determine a user's Id based on
    a given email.
    :return: Return's the userId of the given email user.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    email = ['email']
    # userId = db.getUserId(email)
    return """
    Retrieved UserId from given email!
    userId: {}
    """.format(userId)

@app.route("/create-post")
def post():
    """
    This function is used to add a created post to the database.
    :return: Return a boolean that determines successful creation.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    userId = data['userId']
    postText = data['postText']
    topics = data['topics']

    # db.newPost(userId, postText, topics)

    return "Post successfully created!"


@app.route("/get-all-posts", methods=['POST'])
def get_all_posts():
    """
    This function is used to get all of the posts from all of the topics from
      the database.
    :return: Display Information about the action.
    """
    # rows = db.getAllPosts()
    return "Success"


@app.route("/get-topic-posts", methods=['POST'])
def get_all_topic_posts():
    """
    This function is used to retrieve all of the posts of a certain topic
      from the database.
    :return: Display information about the action.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    topic = data['topic']
    # rows = db.getAllTopicPosts(topic)
    return"""
Retrieved posts from topic!
  topic: {}
""".format(topic)


@app.route("/delete-post", methods=['POST'])
def delete_post():
    """
    This function is used to delete a post from the database.
    :return: Display information about the action.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    postId = data['postId']
    # db.deletePost(postId)
    return """
Deleted Post!
  postId: {}
""".format(postId)


@app.route("/dm-user", methods=['POST'])
def dm_user():
    """
    This function is used to send a DM to the database
    :return: Display information message about the action.
    """
    # Get the info from the json file sent with the request
    data = request.get_json()

    senderId = data['senderId']
    receiverId = data['receiverId']
    message = data['Message']

    # db.newDM(senderId, receiverId, message)

    return """
DM Sent!
  senderId: {}
  receiverId: {}
  message: {}
""".format(senderId, receiverId, message)




if __name__ == '__main__':
    app.run(debug=True)
