posts = [
  {
  "title": "About the importance of functional programming",
  "body": "Functional programming is ....." 
  },
  {
  "title": "OOP programming brings classes and objects into the code",
  "body": "OOP is  ....." 
  },
]

def addPost(postlist, posttitle, postbody):
    
    new_dict = {
        "title": posttitle, 
        "body": postbody
        }

    
    # Add the new dict to the beginning of the posts list
    postlist.insert(0, new_dict)

# TESTING
#the function does not return anything, modifies the posts list.
addPost(posts, "Programming", "Programming is ...")
print (posts)

