from flask import Flask, url_for, redirect, render_template
import DatabaseLibrary as db


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def display_home_page():
	return render_template('sample.html', **locals())


@app.route("/user-create-new-user")
def create_user():
	# Get the info form the frontend
	username = "username"
	commonName = "commonname"
	email = "email"
	phone = "111-111-1111"
	birthday = "December 25, 0000"
	description = "this is a description"
	db.newUser(username, commonName, email, phone, birthday, description)

	return render_template('sample.html', **locals())


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

# TODO: Add skeletons to the rest of the functions


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


@app.route("/get-user-id-from-email")
def get_id_from_email():
	return render_template('sample.html', **locals())


@app.route("/create-post")
def post():
	return render_template('sample.html', **locals())


@app.route("/get-all-posts")
def get_all_posts():
	return render_template('sample.html', **locals())


@app.route("/get-topic-posts")
def get_all_topic_posts():
	return render_template('sample.html', **locals())


@app.route("/delete-post")
def delete_post():
	return render_template('sample.html', **locals())


@app.route("/dm-user")
def dm_user():
	return render_template('sample.html', **locals())




if __name__ == '__main__':
	app.run(debug=True)