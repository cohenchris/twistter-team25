# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:45:59 2019

@author: kbuzz
"""
import pyodbc

############################ USER METHODS #####################################

# INSERTS A NEW USER INTO THE SYSTEM
def newUser(userName, commonName, email, phone, birthday, description):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT MAX(UserId) FROM UserTable")
    
    userId = cursor.fetchone()[0] + 1
        
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO UserTable (UserID, UserName, CommonName, Email, Phone, Birthday, Description)" + 
    " VALUES (" + str(userId) + ",'" + userName + "','" + commonName + 
    "','" + email + "','" + phone + "','" + birthday + "'" + ",'" + description + "')")
    cnxn.commit()
    
    newUserTopic(userId, "All")
    
   
# UPDATES A USER PROFILE COMMON NAME
def updateCommonName(userId, newCommonName):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET CommonName = '" + newCommonName +
                   "' WHERE UserId = '" + str(userId) + "'")
    cnxn.commit()
    
  
# UPDATES A USER PROFILE PHONE NUMBER
def updatePhone(userId, newPhone):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET Phone = '" + newPhone +
                   "' WHERE UserId = '" + str(userId) + "'")
    cnxn.commit()
    

# UPDATES A USER PROFILE DESCRIPTION
def updateDescription(userId, newDescription):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("UPDATE UserTable SET Description = '" + newDescription +
                   "' WHERE UserId = '" + str(userId) + "'")
    cnxn.commit()
    
# ADDS A TOPIC TO THE USERS PROFILE
def newUserTopic(userId, topic):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO TopicTable (UserId, Topic)" +
                   " VALUES ("  + str(userId) + ",'" + topic + "')")
    cnxn.commit()
    

# SHOWS THE TIMELINE FOR A USER
def getUserTimeline(userId):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT DISTINCT a.PostId,a.UserId,a.PostText,a.Topics,a.Timestamp " +
                   "FROM PostTable as a INNER JOIN FollowerTable as b " + 
                   "ON b.FollowingId = a.UserId AND (" +
		           "a.Topics LIKE CONCAT(b.Topic, ',%') OR " +
		           "a.Topics LIKE CONCAT('%,', b.Topic) OR " +
		           "a.Topics LIKE CONCAT('%,', b.Topic, ',%') OR " +
		           "a.Topics LIKE b.Topic OR " +
		           "a.Topics LIKE 'All') " +
                   "WHERE b.UserId=" + str(userId) + " ORDER BY a.Timestamp DESC")
    return cursor.fetchall()


# GETS ALL POSTS MADE BY A PARTICULAR USER
def getUserPosts(userId):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM PostTable WHERE UserId = " + str(userId))
    
    return cursor.fetchall()


def deleteUser(userId):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM UserTable WHERE UserId=" + str(userId))
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM PostTable WHERE UserId=" + str(userId))
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM DMTable WHERE UserId=" + str(userId) + " OR FollowingId=" + str(userId))
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM FollowerTable WHERE UserId=" + str(userId) + " OR FollowingId=" + str(userId))
    
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM LikeTable WHERE UserId=" + str(userId))    

    cnxn.commit()
    
###############################################################################


############################ FOLLOW METHODS ###################################

# ALLOWS A USER TO FOLLOW ANOTHER USER-TOPIC COMBINATION
def newFollow(userId, followingId, topic):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO FollowerTable (UserId, FollowingId, Topic)" +
                   " VALUES ("  + str(userId) + "," + str(followingId) + ",'" + topic + "')")
    cnxn.commit()
    

# ALLOWS A USER TO COMPLETELY UNFOLLOW ANOTHER USER
def unfollowUser(userId, followingId):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM FollowerTable WHERE UserId=" + str(userId) +
                   " AND FollowingId=" + str(followingId))
    cnxn.commit()
    

# ALLOWS A USER TO UNFOLLOW A USER-TOPIC COMBINATION
def updateFollow(userId, followingId, topics = []):
    unfollowUser(userId, followingId)
    
    for topic in topics:
        newFollow(userId, followingId, topic)

###############################################################################


############################ GENERAL METHODS ##################################

# VALIDATES NEW EMAILS FOR NEW USERS    
def validateEmail(email):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 1 UserId FROM UserTable WHERE Email = '" + email + "'")
    
    if cursor.fetchone() is None:
        return True
    else:
        return False
    
    
def validateUsername(username):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 1 UserId FROM UserTable WHERE UserName = '" + username + "'")
    
    if cursor.fetchone() is None:
        return True
    else:
        return False
    

# RETURNS USER ID FROM ACCOUNT EMAIL
def getUserId(email):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
    
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 1 UserId FROM UserTable WHERE Email = '" + email + "'")
    
    return cursor.fetchone()[0]

###############################################################################


############################ POST METHODS #####################################

# CREATES A NEW POST
def newPost(userId, postText, topics):
    import datetime
    
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT MAX(PostId) FROM PostTable")
    
    PostId = cursor.fetchone()[0] + 1
    
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO PostTable (PostId, UserId, PostText, Topics, Timestamp)" +
                   " VALUES (" + str(PostId) + "," + str(userId) + ",'" + postText + "','" +
                   topics + "','" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "')")
    cnxn.commit()


# GETS ALL POSTS ON THE PLATFORM
def getAllPosts():
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM PostTable")
    
    return cursor.fetchall()


# GETS ALL POST ON THE PLATFORM WITH A SPECIFIC TOPIC
def getAllTopicPosts(topic):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM PostTable WHERE " +
          "Topics LIKE '" + topic + ",%' OR "
          "Topics LIKE '%," + topic + "' OR "
          "Topics LIKE '%," + topic + ",%' OR "
          "Topics LIKE '" + topic + "'")
    
    return cursor.fetchall()


# DELETES A POST ON THE PLATFORM
def deletePost(postId):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM PostTable WHERE PostId=" +str(postId))
    cnxn.commit()
    
###############################################################################  
    

############################## DM METHODS #####################################
  
# CREATES A NEW DM MESSAGE  
def newDM(senderId, recieverId, message):
    import datetime
    
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-JLT30RP\SQLEXPRESS;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
        
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO DMTable (SenderId, RecieverId, Message, Timestamp)" +
                   " VALUES (" + str(senderId) + "," + str(recieverId) + ",'" +
                   message + "','" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "')")
    cnxn.commit()
    
###############################################################################
