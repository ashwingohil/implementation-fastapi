from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange
from fastapi import Response, status, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None



while True:
    try:
        conn = psycopg2.connect(host = 'localhost',database = 'fastapi',
                                user = 'postgres', password = 'nopassword', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break

    except Exception as error:
        print("Connecting to database failed")
        print("Error", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def root():
    return {"message": "Welcome to fastapi!!!"}

@app.get("/posts")
def get_posts():

    print("In get_posts: retrieving 1st")
    i = 0
    for x in my_posts:
        
        if i == 0:
            print(x["title"])
            print(x["content"])
            print(x["id"])
            print()
        else:
            break
        i = i+1
    #   or you can simple do print(x)
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):    # payload is variable of type dict
    print(payLoad)
    return {"new_post": f"TITLE {payLoad['title']} CONTENT: {payLoad['content']}"}

@app.post("/createposts_validated")
def create_posts(newpost: Post):
    print(newpost.title)
    print(newpost.content)
    print(newpost.published)
    print(newpost.rating)
    outputdic = newpost.dict()
    print(outputdic)
    # return {"data" : "new post"}    # in postman remove one entry and see the error
    return {"data": newpost}

# the above can be just copied with name change
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(newpost: Post):

    print(newpost.title)
    print(newpost.content)
    print(newpost.published)
    print(newpost.rating)

    post_dict = newpost.dict()
    post_dict['id'] = randrange(0,100000)
    my_posts.append(post_dict)
    print(post_dict)
    # return {"data" : "new post"}    # in postman remove one entry and see the error
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latestpost():
    latestpost = my_posts[len(my_posts)-1]
    return {"detail": latestpost}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):  # as this is int here . below typecasting int is not required

    post = find_post(int(id))
    if not post:
        # response.status_code = 404
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id {id} was not found"}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post with id {id} is not found")
    print(id) # here print(type(id)) will give the type of variable
    return {"post_detail": f"Here is post {id} {post} "}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    # find index in array with the required ID
    # my_posts.pop(index)

    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} not found")

    my_posts.pop(index)
    # return {"message": "post deleted successfully"} # this will not work because of 204 rule
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} not found")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    
    return {"data": post_dict}


