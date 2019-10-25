# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:45:59 2019

@author: kbuzz
"""
import pyodbc
import datetime

############################ USER METHODS #####################################

# INSERTS A NEW USER INTO THE SYSTEM
def newUser(userName, password, commonName, email, phone, birthday, description):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT MAX(UserId) FROM UserTable")
    
    userId = cursor.fetchone()[0]
    if userId is None: 
        userId = 1
    else:
        userId = userId + 1
        
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO UserTable (UserID, UserName, Password, CommonName, Email, Phone, Birthday, Description)" + 
    " VALUES (" + str(userId) + ",'" + userName + "',ENCRYPTBYPASSPHRASE('team25','" + password + "'),'" + commonName + 
    "','" + email + "','" + phone + "','" + birthday + "'" + ",'" + description + "')")
    cnxn.commit()
    
    newUserTopic(userId, "All")


#VALIDATES A USERNAME AND PASSWORD
def validateLogin(username, password):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT UserId FROM UserTable WHERE UserName='" + username + "' AND " +
    "CONVERT(varchar(50), DECRYPTBYPASSPHRASE('team25', Password))='" + password + "'")
    
    ret = cursor.fetchone()
    if ret is None:
        return -1
    else:
        return ret[0]
    
   
# UPDATES A USER PROFILE COMMON NAME
def updateCommonName(userId, newCommonName):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET CommonName = '" + newCommonName +
                   "' WHERE UserId = '" + str(userId) + "'")
    cnxn.commit()
    
  
# UPDATES A USER PROFILE PHONE NUMBER
def updatePhone(userId, newPhone):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET Phone = '" + newPhone +
                   "' WHERE UserId = '" + str(userId) + "'")
    cnxn.commit()
    

# UPDATES A USER PROFILE DESCRIPTION
def updateDescription(userId, newDescription):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET Description = '" + newDescription +
                   "' WHERE UserId = '" + str(userId) + "'")
    cnxn.commit()


# UPDATES A USER PASSWORD
def updatePassword(userId, newPassword):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET Password=ENCRYPTBYPASSPHRASE('team25','" + newPassword + "') " +
    "WHERE UserId=" + str(userId))
    cnxn.commit()

    
# ADDS A TOPIC TO THE USERS PROFILE
def newUserTopic(userId, topic):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO TopicTable (UserId, Topic)" +
                   " VALUES ("  + str(userId) + ",'" + topic + "')")
    cnxn.commit()
    

# SHOWS THE TIMELINE FOR A USER
def getUserTimeline(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT DISTINCT a.PostId,a.RetweetId,b.UserId,b.UserName,b.CommonName,a.PostText,a.Topics,a.Timestamp," +
	"(SELECT COUNT(*) FROM LikeTable AS c WHERE c.PostId = a.PostId OR c.PostId = a.RetweetId) AS Likes," +
	"(SELECT COUNT(*) FROM PostTable AS d WHERE d.RetweetId = a.PostId OR d.RetweetId = a.RetweetId) AS Retweets," +
	"COALESCE(a.RetweetTimestamp, a.Timestamp) " +
    "FROM PostTable AS a " +
	"LEFT JOIN UserTable AS b ON a.UserId = b.UserId " +
	"LEFT JOIN FollowerTable AS e ON a.UserId = e.FollowingId AND " +
	"(a.Topics LIKE CONCAT(e.Topic, ',%') OR a.Topics LIKE CONCAT('%,', e.Topic) OR a.Topics LIKE CONCAT('%,', e.Topic, ',%') OR a.Topics LIKE e.Topic) " +
    "WHERE e.UserId=" + str(userId) +
    "ORDER BY COALESCE(a.RetweetTimestamp, a.Timestamp) DESC")
    
    return cursor.fetchall()


# GETS ALL POSTS MADE BY A PARTICULAR USER
def getUserPosts(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT a.PostId,a.RetweetId,b.UserId,b.UserName,b.CommonName,a.PostText,a.Topics,a.Timestamp," +
    "(SELECT COUNT(*) FROM LikeTable AS c WHERE c.PostId = a.PostId OR c.PostId = a.RetweetId) AS Likes," +
    "(SELECT COUNT(*) FROM PostTable AS d WHERE d.RetweetId = a.PostId OR d.RetweetId = a.RetweetId) AS Retweets " +
    "FROM PostTable AS a LEFT JOIN UserTable AS b ON a.UserId = b.UserId " +
    "WHERE b.UserId=" + str(userId) + " AND NOT EXISTS (SELECT 1 FROM PostTable as e WHERE a.RetweetId = e.PostId)" +
    "ORDER BY COALESCE(a.RetweetTimestamp, a.Timestamp) DESC")
    
    return cursor.fetchall()


# GETS ALL TOPICS FOR A PARTICULAR USER
def getUserTopics(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT Topic FROM TopicTable WHERE UserId=" + str(userId))
    
    topics = []
    for topic in cursor.fetchall():
        topics.append(topic[0])

    return topics


# REMOVES A USER AND ALL THEIR DATA FROM THE DATABASE
def deleteUser(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM UserTable WHERE UserId=" + str(userId))
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM PostTable WHERE UserId=" + str(userId))
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM DMTable WHERE SenderId=" + str(userId) + " OR RecieverId=" + str(userId))
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM FollowerTable WHERE UserId=" + str(userId) + " OR FollowingId=" + str(userId))

    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM TopicTable WHERE UserId=" + str(userId))
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM LikeTable WHERE UserId=" + str(userId))    

    cnxn.commit()


# GETS USER PROFILE INFORMATION FROM THE DATABASE
def getUser(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT UserName,CommonName," +
	   "(SELECT COUNT(*) FROM FollowerTable WHERE UserId=x.UserId) as Following," +
	   "(SELECT COUNT(*) FROM FollowerTable WHERE FollowingId=x.UserId) as Followers," +
	   "(SELECT COUNT(*) FROM PostTable WHERE UserId=x.UserId) as Posts," +
	   "CASE WHEN BdayIsPublic=1 THEN Birthday ELSE NULL END as Birthday," +
	   "CASE WHEN DescIsPublic=1 THEN Description ELSE NULL END as Description " +
       "FROM UserTable as x WHERE UserId=" + str(userId) + " FOR JSON AUTO")

    return cursor.fetchone()[0]


# SETS USER BIRTHDAY TO PRIVATE
def setBdayPrivate(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET BdayIsPublic=0 WHERE UserId=" + str(userId))
    cnxn.commit()


# SETS USER BIRTHDAY TO PUBLIC
def setBdayPublic(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET BdayIsPublic=1 WHERE UserId=" + str(userId))
    cnxn.commit()


# SETS USER DESCRIPTION TO PRIVATE
def setDescPrivate(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET DescIsPublic=0 WHERE UserId=" + str(userId))
    cnxn.commit()


# SETS USER DESCRIPTION TO PUBLIC
def setDescPublic(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET DescIsPublic=1 WHERE UserId=" + str(userId))
    cnxn.commit()
    
###############################################################################


############################ FOLLOW METHODS ###################################

# ALLOWS A USER TO FOLLOW ANOTHER USER-TOPIC COMBINATION
def newFollow(userId, followingId, topic):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO FollowerTable (UserId, FollowingId, Topic)" +
                   " VALUES ("  + str(userId) + "," + str(followingId) + ",'" + topic + "')")
    cnxn.commit()
    

# ALLOWS A USER TO COMPLETELY UNFOLLOW ANOTHER USER
def unfollowUser(userId, followingId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM FollowerTable WHERE UserId=" + str(userId) +
                   " AND FollowingId=" + str(followingId))
    cnxn.commit()
    

# ALLOWS A USER TO UPDATE TOPICS THEY FOLLOW FOR A PARTICULAR USER
def updateFollow(userId, followingId, topics = []):
    unfollowUser(userId, followingId)
    
    for topic in topics:
        newFollow(userId, followingId, topic)

###############################################################################


############################ GENERAL METHODS ##################################

# VALIDATES NEW EMAILS FOR NEW USERS; RETURNS TRUE IF NOT IN THE DATABASE    
def validateEmail(email):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 1 UserId FROM UserTable WHERE Email = '" + email + "'")
    
    if cursor.fetchone() is None:
        return True
    else:
        return False
    
    
def validateUsername(username):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 1 UserId FROM UserTable WHERE UserName = '" + username + "'")
    
    if cursor.fetchone() is None:
        return True
    else:
        return False
    

# RETURNS USER ID FROM ACCOUNT EMAIL
def getUserId(email):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 1 UserId FROM UserTable WHERE Email = '" + email + "'")
    
    ret = cursor.fetchone()
    if ret is None:
        return -1
    else:
        return ret[0]

###############################################################################


############################ POST METHODS #####################################

# CREATES A NEW POST
def newPost(userId, postText, topics):    
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT MAX(PostId) FROM PostTable")
    
    postId = cursor.fetchone()[0]
    if postId is None:
        postId = 1
    else:
        postId = postId + 1
    
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO PostTable (PostId, UserId, PostText, Topics, Timestamp)" +
                   " VALUES (" + str(postId) + "," + str(userId) + ",'" + postText + "','" +
                   topics + ",All','" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "')")
    cnxn.commit()


# GETS ALL POSTS ON THE PLATFORM
def getAllPosts():
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT a.PostId,a.RetweetId,b.UserId,b.UserName,b.CommonName,a.PostText,a.Topics,a.Timestamp," +
	"(SELECT COUNT(*) FROM LikeTable AS c WHERE c.PostId = a.PostId OR c.PostId = a.RetweetId) AS Likes," +
	"(SELECT COUNT(*) FROM PostTable AS d WHERE d.RetweetId = a.PostId OR d.RetweetId = a.RetweetId) AS Retweets " +
    "FROM PostTable AS a LEFT JOIN UserTable AS b ON a.UserId = b.UserId " +
    "WHERE a.RetweetId IS NULL " +
    "ORDER BY a.Timestamp DESC FOR JSON AUTO")
    
    return cursor.fetchall()[0][0]


# GETS ALL POST ON THE PLATFORM WITH A SPECIFIC TOPIC
def getAllTopicPosts(topic):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT a.PostId,a.RetweetId,b.UserId,b.UserName,b.CommonName,a.PostText,a.Topics,a.Timestamp," +
	"(SELECT COUNT(*) FROM LikeTable AS c WHERE c.PostId = a.PostId OR c.PostId = a.RetweetId) AS Likes," +
	"(SELECT COUNT(*) FROM PostTable AS d WHERE d.RetweetId = a.PostId OR d.RetweetId = a.RetweetId) AS Retweets " +
    "FROM PostTable AS a LEFT JOIN UserTable AS b ON a.UserId = b.UserId " +
    "WHERE a.RetweetId IS NULL AND (Topics LIKE '" + topic + ",%' OR ""Topics LIKE '%," + topic + "' OR ""Topics LIKE '%," + topic + ",%' OR ""Topics LIKE '" + topic + "') " +
    "ORDER BY a.Timestamp DESC")
    
    return cursor.fetchall()


# DELETES A POST ON THE PLATFORM
def deletePost(postId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM PostTable WHERE PostId=" + str(postId) + " OR RetweetId=" + str(postId))
    cnxn.commit()


# ADDS A LIKE TO A POST
def like(userId, postId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")

    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO LikeTable (UserId,PostId)" +
                    " VALUES (" + str(userId) + "," + str(postId) + ")")
    cnxn.commit()


# REMOVES A LIKE FROM A POST
def unlike(userId, postId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")

    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM LikeTable WHERE UserId=" + str(userId) +
    " AND PostId=" + str(postId))
    cnxn.commit()


# RETWEETS A POST
def retweet(userId, postId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")

    cursor = cnxn.cursor()
    cursor.execute("SELECT MAX(PostId) FROM PostTable")
    
    newPostId = cursor.fetchone()[0]
    if newPostId is None:
        newPostId = 1
    else:
        newPostId = newPostId + 1

    cursor = cnxn.cursor()
    oldPost = cursor.execute("SELECT * FROM PostTable WHERE PostId=" + str(postId)).fetchone()
    
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO PostTable (PostId,UserId,PostText,Topics,Timestamp,RetweetId,RetweetTimestamp) " +
    "VALUES (" + str(newPostId) + "," + str(userId) + ",'" + oldPost[2] + "','" + oldPost[3] + "','" + str(oldPost[4]) + "'," + str(oldPost[0]) + ",'" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "')")
    cnxn.commit()


# REMOVES A RETWEET FROM A POST
def unretweet(userId, postId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")

    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM PostTable WHERE UserId=" + str(userId) + " AND RetweetId =" + str(postId))
    cnxn.commit()

###############################################################################  
    

############################## DM METHODS #####################################
  
# CREATES A NEW DM MESSAGE  
def newDM(senderId, recieverId, message):    
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO DMTable (SenderId, RecieverId, Message, Timestamp)" +
                   " VALUES (" + str(senderId) + "," + str(recieverId) + ",'" +
                   message + "','" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "')")
    cnxn.commit()


# DELETES DMS FOR A PARTICULAR USER
def deleteDMs(userId, recieverId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("UPDATE DMTable SET SenderDeleted=1 WHERE " +
    "SenderId=" + str(userId) + " AND RecieverId=" + str(recieverId))

    cursor = cnxn.cursor()
    cursor.execute("UPDATE DMTable SET RecieverDeleted=1 WHERE " +
    "SenderId=" + str(recieverId) + " AND RecieverId=" + str(userId))

    cnxn.commit()

    clearDMs()


# WIPES THE DATABASE OF ANY UNUSED DMS
def clearDMs():
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM DMTable WHERE SenderDeleted=1 AND RecieverDeleted=1")
    cnxn.commit()

# GETS A DM CONVERSATION BETWEEN TWO USERS
def getDMConvo(userId, recieverId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT SenderId,RecieverId,Message,TimeStamp FROM DMTable " +
    "WHERE (SenderId=" + str(userId) + " AND RecieverId=" + str(recieverId) + " AND SenderDeleted=0) OR " +
    "(SenderId=" + str(recieverId) + " AND RecieverId=" + str(userId) + " AND RecieverDeleted=0) " +
    "ORDER BY TimeStamp FOR JSON AUTO")

    return cursor.fetchall()[0][0]


# GETS LIST OF DM CONVOS FOR A USER
def getDMList(userId):
    cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};" +
                      "Server=tcp:twistter-dns.eastus.cloudapp.azure.com,1401;" +
                      "Database=Twistter-Database;" +
                      "Uid=kbuzza;" +
                      "Pwd=TestTwistter1;" +
                      "Encrypt=no;" +
                      "TrustServerCertificate=no;" +
                      "Connection Timeout=60;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT a.UserId,a.UserName,a.CommonName FROM " +
    "(SELECT TOP 50 CASE WHEN y.Id1=" + str(userId) + " THEN y.Id2 ELSE y.Id1 END AS UserId FROM " +
    "(SELECT TOP 50 MAX(x.SenderId) AS Id1,MIN(x.RecieverId) AS Id2,x.Val FROM " +
    "(SELECT TOP 50 SenderId,RecieverId,MAX(TimeStamp) AS TimeStamp," +
	"CASE WHEN SenderId > RecieverId THEN CONCAT(SenderId,RecieverId) ELSE CONCAT(RecieverId,SenderId) END AS Val " +
	"FROM DMTable WHERE (SenderId=" + str(userId) + " AND SenderDeleted=0) OR (RecieverId=" + str(userId) + " AND RecieverDeleted=0) " +
	"GROUP BY SenderId,RecieverId ORDER BY MAX(TimeStamp) DESC, SenderId,RecieverId" +
    ") AS x GROUP BY Val) AS y) AS z LEFT JOIN UserTable AS a ON z.UserId = a.UserId")

    return cursor.fetchall()

###############################################################################