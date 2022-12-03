# implementation-fastapi
**Purpose:** To use the knowledge of FastAPI framework and apply in creating API endpoints. Database used is PostgreSql

>**Outline of the Project:**

With the help of API endpoints, a user can get registered with the system. Able to login. Oauth2 is used for authorization. A user can see other user's
email id by the user's id. A user can create posts, see all posts created by other users, can see a post by its id, can update his own post created
previously. A user can also vote for a post and delete his own post.

>>**Running the project:**

In VsCode: Open the terminal and cd to the Project directory. Enable the python interpretor: "source venv/bin/activate". Run the server by the command:
uvicorn app.main:app --reload

>**Endpoints by Swagger UI which can be seen by hitting the "url/docs"**

**Users:**
![image](https://user-images.githubusercontent.com/26901597/205418725-75e15939-aafe-4913-84eb-acc706b6b1c7.png)

**Authentication:**
![image](https://user-images.githubusercontent.com/26901597/205418762-3d99c873-59ea-469d-bfef-15253abf5933.png)

**Posts:**
![image](https://user-images.githubusercontent.com/26901597/205418779-cb1fde96-904d-4735-98d3-841b5c317852.png)

**Vote:**
![image](https://user-images.githubusercontent.com/26901597/205418805-3c9c7498-12ab-494e-b8f6-100eb82776fd.png)

>>**Using Postman and setting up Environment Variables**

The API endpoints are accessible only after a successful login. A user get a JWT token. And this token is to be used for each request to endpoint.
To automate this process a little so that you don't have to provide the JWT token in each request, please do the following:

1) Goto Enviornments in PostMan and create a New environment with a name to it. Set the URL, Type, Initial Value and Current Value as below and hit save:
![image](https://user-images.githubusercontent.com/26901597/205419297-6992f1ae-2c49-4782-a90b-8c07d0e9f13d.png)

2) Not goto to your collections and at each endpoint, mask the api url like http://127.0.0.1:8000 to {{URL}} which is environment variable. And from the
environment at the top right , select the newly created environment. Replace all endpoint urls with {{URL}}
![image](https://user-images.githubusercontent.com/26901597/205419429-f2c18c92-f12f-46f6-aecb-abf957578f44.png)

3) Now goto Login endpoint in the collections and click on "Tests" tab on the top and on the right select "Set and environment variable" as below:
![image](https://user-images.githubusercontent.com/26901597/205419663-305e69e5-d8bf-45d3-b519-7c68f374440a.png)

4) Now at every endpoint in the collection, goto "authorization tab" and select the type to be "Bearer Token" and in "Token" field , enter {{JWT}} as it is.
![image](https://user-images.githubusercontent.com/26901597/205419771-fdc8846e-bdae-4a8d-99a4-fa9e3c1f6d98.png)











