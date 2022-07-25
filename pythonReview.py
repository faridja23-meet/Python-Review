def createYouTubeVideo(title, description):
    return {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments" : {}}

def like(video):
    video["likes"] += 1
    return video

def dislike(video):
    video["dislikes"] += 1
    return video

def addComment(video, username, comment):
    video["comments"][username] = comment
    return video

bob = createYouTubeVideo("whatever", "skdnfkl")
# print(bob)
# like(bob)
# dislike(bob)
# like(bob)
# print(bob)
# addComment(bob,"farid","anything")
# print(bob)
# addComment("b")


 
for i in range (496):
	like(bob)

print(bob)
