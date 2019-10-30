from flask import Flask, url_for, redirect, render_template, request, jsonify
import time
import inspect
import DatabaseLibrary as db

app = Flask(__name__)

# Constants
invalid_json_format_string = "Invalid json format for this request\n"

log_file = open("logs.log", "w+")

def log(message):
  log_file.write("{}: {}\n".format(time.asctime(time.localtime(time.time())),
                                   message))
  log_file.flush()


log("Starting API")


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def display_home_page():
  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))
  return "API is running great\n"


@app.route("/user-create-new-user", methods=['POST'])
def create_user():
  """
  This function is used to create a new user and push it to the database. In
    order to use this function, make a POST request to function url above and
    send a json file with the appropriate information.
  :return: Display information about the newly created user.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  #  Get the from the json file sent with the request
  data = request.get_json()

  try:
    username = data['username']
    password = data['password']
    commonName = data['commonName']
    email = data['email']
    description = data['description']
  except KeyError:
    return invalid_json_format_string

  #  Push the info to the database
  db.newUser(username, password, commonName, email, description)

  return '''
Created User!
  username: {}
  commonName: {}
  email: {}
  description: {}
'''.format(username, commonName, email, description)


@app.route("/validate-login", methods=['POST'])
def validate_login():
  """
  This function is used to validate login information from the
    database.
  :return: -1 if no user exists, if the user exists it returns the userId
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with POST request
  data = request.get_json()

  try:
    username = data['username']
    password = data['password']
  except KeyError:
    return invalid_json_format_string

  return str(db.validateLogin(username, password)) + "\n"
  # return "Validated"


@app.route("/user-update-common-name", methods=['POST'])
def update_common_name():
  """
  This function is used to update a user's common name in the database.
  :return: Display information about about the call.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
    newCommonName = data['newCommonName']
  except KeyError:
    return invalid_json_format_string

  #  Push the info to the database
  db.updateCommonName(userId, newCommonName)

  return """
Updated Users Common Name!
  userID: {}
  newCommonName: {}
""".format(userId, newCommonName)


@app.route("/user-update-description", methods=['POST'])
def update_description():
  """
  This function is called to update a user's description.
  :return: Display information about the updated information.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data["userId"]
    newDescription = ["newDescription"]
  except KeyError:
    return invalid_json_format_string

  # Send the info to the database
  db.updateDescription(userId, newDescription)

  return """
Updated Description!
  userId: {}
  newDescription: {}
""".format(userId, newDescription)


@app.route("/update-password", methods=['POST'])
def update_password():
  """
  This function is used to update the database with new password info.
  :return: Information about the update
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
    newPassword = data['newPassword']
  except KeyError:
    return invalid_json_format_string

  db.updatePassword(userId, newPassword)

  return """
Updated Password!
  userId: {}
  newPassword: {}
""".format(userId, newPassword)


@app.route("/user-add-new-user-topic", methods=['POST'])
def add_user_topic():
  """
  This function is used to add a new topic to the user's profile.
  :return: Display information about the function call.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
    newTopic = data['newTopic']
  except KeyError:
    return invalid_json_format_string

  db.newUserTopic(userId, newTopic)

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

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
  except KeyError:
    return invalid_json_format_string

  return db.getUserTimeline(userId)

#    return """
#  Retireved Timeline!
#    userId: {}
#  """.format(userId)


@app.route("/user-get-user-posts", methods=['POST'])
def get_user_posts():
  """
  This function is used to get all of the posts of the specific user.
  :return: Display information about the posts.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
  except KeyError:
    return invalid_json_format_string

  return db.getUserPosts(userId)

#    return """
#  Retrieved User Posts!
#    userId: {}
#  """.format(userId)


@app.route("/get-user-topics", methods=['POST'])
def get_user_topics():
  """
  This function is used to retrieve the user posts from the database.
  :return: List of user topics
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  data = request.get_json()

  try:
    userId = data['userId']
  except KeyError:
    return invalid_json_format_string

  return db.getUserTopics(userId)
#   return "Got Posts"


@app.route("/user-delete", methods=['POST'])
def delete_user():
  """
  This function is called in order to delete a user.
  :return: Display information about deleted user
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
  except KeyError:
    return invalid_json_format_string

  db.deleteUser(userId)

#    return """
#  Deleted User!
#    userId: {}
#  """.format(userId)


@app.route("/get-user", methods=['POST'])
def get_user():
  """
  This function is used to get a user's profile information.
  :return:
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  try:
    data = request.get_json()

    try:
      userId = data['userId']
    except KeyError:
      log(invalid_json_format_string)
      return invalid_json_format_string

    try:
      val = db.getUser(userId)
    except TypeError:
      log("Invalid User Id")
      return "Invalid User Id"

    log("Got User")
    return val
  except Exception as e:
    log(str(e))


@app.route("/follow-user", methods=['POST'])
def follow_new_user():
  """
  This function is used to follow a new user.
  :return: Display information about the update.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
    followingId = data['followingId']
  except KeyError:
    return invalid_json_format_string

  db.newFollow(userId, followingId)

  return """
Followed a new user!
  userId: {}
  followingId: {}
""".format(userId, followingId)


@app.route("/unfollow", methods=['POST'])
def unfollow_user():
  """
  This function is used to unfollow a user.
  :return: Display information about the action.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
    followingId = data['followingId']
  except KeyError:
    return invalid_json_format_string

  db.unfollowUser(userId, followingId)

  return """
Unfollowed User!
  userId: {}
  followingId: {}
""".format(userId, followingId)


@app.route("/follow-users-topics", methods=['POST'])
def follow_user_topics():
  """
  This function is used to update the database to include following a user's
    topics.
  :return: Display information about the action.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
    followingId = data['followingId']
    topicsSelected = data['topicsSelected']
  except KeyError:
    return invalid_json_format_string

  db.updateFollow(userId, followingId, topics=topicsSelected)

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

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    email = data['email']  # The user ID requesting a new follow
  except KeyError:
    return invalid_json_format_string

  db.validateEmail(email)

  return """
  Email successfully validated!
    email: {}
  """.format(email)


@app.route("/validate-username", methods=['POST'])
def validate_username():
  """
  This function is used to validate a given user's username.
  :return: Return a boolean that determines validation
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    username = ['user']
  except KeyError:
    return invalid_json_format_string

  db.validateUsername(username)

  return """
  Username successfully validated!
  username: {}
  """.format(username)


@app.route("/get-user-id-from-email", methods=['POST'])
def get_id_from_email():
  """
  This function is used to determine a user's Id based on
  a given email.
  :return: Return's the userId of the given email user.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    email = ['email']
  except KeyError:
    return invalid_json_format_string

  userId = db.getUserId(email)

  #  return """
  # Retrieved UserId from given email!
  # userId: {}
  # """.format(userId)

  return "UserId found"


@app.route("/create-post", methods=['POST'])
def post():
  """
  This function is used to add a created post to the database.
  :return: Return a boolean that determines successful creation.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    userId = data['userId']
    postText = data['postText']
    topics = data['topics']
  except KeyError:
    return invalid_json_format_string

  db.newPost(userId, postText, topics)

  return "Post successfully created!"


@app.route("/get-all-posts", methods=['POST'])
def get_all_posts():
  """
  This function is used to get all of the posts from all of the topics from
    the database.
  :return: Display Information about the action.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  val = db.getAllPosts()
  return jsonify(val)

@app.route("/get-topic-posts", methods=['POST'])
def get_all_topic_posts():
  """
  This function is used to retrieve all of the posts of a certain topic
    from the database.
  :return: Display information about the action.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    topic = data['topic']
  except KeyError:
    return invalid_json_format_string

  return db.getAllTopicPosts(topic)

#  return """
#Retrieved posts from topic!
#  topic: {}
#""".format(topic)


@app.route("/delete-post", methods=['POST'])
def delete_post():
  """
  This function is used to delete a post from the database.
  :return: Display information about the action.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    postId = data['postId']
  except KeyError:
    return invalid_json_format_string

  db.deletePost(postId)
  return """
Deleted Post!
  postId: {}
""".format(postId)


@app.route("/like-post", methods=['POST'])
def like_post():
  """
  This function takes user and post Id and adds to the like
  counter in the database
  :return: Returns that the post was successfully liked
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  data = request.get_json()

  try:
    userId = data['userId']
    postId = data['postId']
  except KeyError:
    return invalid_json_format_string

  db.like(userId, postId)

  return """
Liked!
  userId: {}
  postId: {}
""".format(userId, postId)


@app.route("/dm-user", methods=['POST'])
def dm_user():
  """
  This function is used to send a DM to the database
  :return: Display information message about the action.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get the info from the json file sent with the request
  data = request.get_json()

  try:
    senderId = data['senderId']
    receiverId = data['receiverId']
    message = data['Message']
  except KeyError:
    return invalid_json_format_string

  db.newDM(senderId, receiverId, message)

  return """
DM Sent!
  senderId: {}
  receiverId: {}
  message: {}
""".format(senderId, receiverId, message)


@app.route("/unlike-post", methods=['POST'])
def unlike_post():
  """
  This function takes user and post Id and subtracts to the like
  counter in the database
  :return: Returns that the post was successfully unliked
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  data = request.get_json()

  try:
    userId = data['userId']
    postId = data['postId']
  except KeyError:
    return invalid_json_format_string

  db.unlike(userId, postId)

  return """
Unliked!
  userId: {}
  postId: {}
""".format(userId, postId)


@app.route("/retweet-post", methods=['POST'])
def retweet():
  """
  This function retweets a post and adds it to the database
  :return: Returns that the post was successfully retweeted
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  data = request.get_json()

  try:
    userId = data['userId']
    postId = data['postId']
  except KeyError:
    return invalid_json_format_string

  db.retweet(userId, postId)

  return """
  Retweeded!
  """


@app.route("/unretweet-post", methods=['POST'])
def unretweet():
  """
   This function unretweets a post and removes it from the database
   :return: Returns that the post was successfully unretweeted
   """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  data = request.get_json()

  try:
    userId = data['userId']
    postId = data['postId']
  except KeyError:
    return invalid_json_format_string

  db.retweet(userId, postId)

  return """
  Unretweeded!
  """


@app.route("/delete-dm", methods=['POST'])
def deleteDMs():
  """
  This function deletes the dms for a particular user
  :return: Returns that the dms were successfully deleted.
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  data = request.get_json()

  try:
    userId = data['userId']
    receiverId = data['receiverId']
  except KeyError:
    return invalid_json_format_string

  db.deleteDMs(userId, receiverId)

  return """
  DMs successfully deleted!
  """


@app.route("/clear-dm", methods=['POST'])
def clearDMs():
  """
  This function wipes the database of any unused dms
  :return: Returns that the dms were successfully wiped
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # db.clearDMs()

  return "DMs successfully cleared"


@app.route("/get-DMConvo", methods=['POST'])
def get_DMConvo():
  """
  This function gets a dm conversation between two users
  :return: Returns the conversation between the two users
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  data = request.get_json()

  try:
    userId = data['userId']
    receiverId = data['receiverId']
  except KeyError:
    return invalid_json_format_string

  convo = db.getDMConvo(userId, receiverId)
  # convo = "convo"

  return """
  convo: {}
  """.format(convo)


@app.route("/get-DMList", methods=['POST'])
def get_DMList():
  """
  This function is used to get a list of dms from the database
  :return: Returns the associated userId and a list of DMs
  """

  log("Request - {}".format(
    inspect.getframeinfo(inspect.currentframe()).function))

  # Get info from json file
  data = request.get_json()

  try:
    userID = data['userId']
  except KeyError:
    return invalid_json_format_string

  dmList = db.getDMLIST(userID)

  return """
userID: {}
DMList: {}
""".format(userID, dmList)


if __name__ == '__main__':
  app.run()
