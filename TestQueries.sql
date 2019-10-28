--SELECT a.PostId,
--	   a.RetweetId,
--	   b.UserId,
--	   b.UserName,
--	   b.CommonName,
--	   a.PostText,
--	   a.Topics,
--	   a.Timestamp,
--	   (SELECT COUNT(*) FROM LikeTable AS c WHERE c.PostId = a.PostId OR c.PostId = a.RetweetId) AS Likes,
--	   (SELECT COUNT(*) FROM PostTable AS d WHERE d.RetweetId = a.PostId OR d.RetweetId = a.RetweetId) AS Retweets
--FROM PostTable AS a LEFT JOIN UserTable AS b ON a.UserId = b.UserId
--WHERE b.UserId = 1 AND NOT EXISTS (SELECT 1 FROM PostTable as e WHERE a.RetweetId = e.PostId)
--ORDER BY COALESCE(a.RetweetTimestamp, a.Timestamp)


--SELECT a.PostId,
--	   a.RetweetId,
--	   b.UserId,
--	   b.UserName,
--	   b.CommonName,
--	   a.PostText,
--	   a.Topics,
--	   a.Timestamp,
--	   (SELECT COUNT(*) FROM LikeTable AS c WHERE c.PostId = a.PostId OR c.PostId = a.RetweetId) AS Likes,
--	   (SELECT COUNT(*) FROM PostTable AS d WHERE d.RetweetId = a.PostId OR d.RetweetId = a.RetweetId) AS Retweets
--FROM PostTable AS a LEFT JOIN UserTable AS b ON a.UserId = b.UserId
--WHERE a.RetweetId IS NULL AND (a.Topics LIKE 'News,%' OR a.Topics LIKE '%,News' OR a.Topics LIKE '%,News,%' OR a.Topics LIKE 'News')
--ORDER BY a.Timestamp





select distinct a.postid,
	   a.retweetid,
	   b.userid,
	   b.username,
	   b.commonname,
	   a.posttext,
	   a.topics,
	   a.timestamp,
	   (
	   select count(*)
	   from liketable as c
	   where c.postid = a.postid
	       or c.postid = a.retweetid
	   ) as likes,
	   (
	   select count(*)
	   from posttable as d
	   where d.retweetid = a.postid
		   or d.retweetid = a.retweetid
	   ) as retweets,
	   coalesce(a.retweettimestamp, a.timestamp)
from posttable as a
	left join usertable as b
		on a.userid = b.userid
	left join followertable as e
		on a.userid = e.followingid and
		(
		a.topics like concat(e.topic, ',%') or
		a.topics like concat('%,', e.topic) or
		a.topics like concat('%,', e.topic, ',%') or
		a.topics like e.topic
		)
where e.userid = 1
order by coalesce(a.retweettimestamp, a.timestamp) desc
SELECT * FROM PostTable



SELECT a.UserId,a.UserName,a.CommonName FROM
(
SELECT TOP 50 CASE
	       WHEN y.Id1=1 THEN y.Id2
		   ELSE y.Id1
	   END AS UserId
FROM
(
SELECT TOP 50 MAX(x.SenderId) AS Id1,MIN(x.RecieverId) AS Id2,x.Val FROM
(
	SELECT TOP 50
		   SenderId,
		   RecieverId,
		   MAX(TimeStamp) AS TimeStamp,
		   CASE
		       WHEN SenderId > RecieverId THEN CONCAT(SenderId,RecieverId)
			   ELSE CONCAT(RecieverId,SenderId)
		   END AS Val
	FROM DMTable
	WHERE (SenderId=1 AND SenderDeleted=0) OR
	(RecieverId=1 AND RecieverDeleted=0)
	GROUP BY SenderId,RecieverId
	ORDER BY MAX(TimeStamp) DESC, SenderId,RecieverId
) AS x
GROUP BY Val
) AS y
) AS z LEFT JOIN UserTable AS a ON z.UserId = a.UserId

SELECT * FROM DMTable
SELECT * FROM PostTable