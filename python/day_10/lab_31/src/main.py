#main.py

#from pydantic import BaseModel  # type: ignore
from time import sleep
import requests  # type: ignore
import urllib.request



def get_url(url: str) -> None:
    """
    Make a GET request to a URL and print the response content.

    Args:
        url (str): The URL to make the request to.
    """
    response = requests.get(url)
    print(response.text)

get_url('https://www.google.com')

print("\n\n\n")

#4. Create a function called `post_url` that makes a POST request to a URL with a payload and prints the response content.
def post_url(url: str, payload: dict) -> None:
    """
    Make a POST request to a URL with a payload and print the response content.

    Args:
        url (str): The URL to make the request to.
        payload (dict): The payload to send in the request.
    """
    response = requests.post(url, data=payload)
    print(response.text)

post_url('https://httpbin.org/post', {'key': 'value'})

print("\n\n\n")

#6. Now let's create a function called `get_json` that makes a GET request to a URL and returns the response JSON content.
def get_json(url: str) -> dict:
    """
    Make a GET request to a URL and return the response JSON content.

    Args:
        url (str): The URL to make the request to.

    Returns:
        dict: The JSON content of the response.
    """
    response = requests.get(url)
    print(response.text)
    return response.json()

print(get_json('https://jsonplaceholder.typicode.com/posts/1'))


print("\n\n\n")

#8. Create a Pydantic model called `Post` with the following fields: `userId`, `id`, `title`, and `body`.

from pydantic import BaseModel

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str
    
def get_json2(url: str) -> Post:
    """
    Make a GET request to a URL and return the response JSON content as a Post object.

    Args:
        url (str): The URL to make the request to.

    Returns:
        Post: The Post object representing the JSON content of the response.
    """
    response = requests.get(url)
    return Post(**response.json())

print(get_json2('https://jsonplaceholder.typicode.com/posts/1'))



print("\n\n\n11")

#11. Create a `__str__` method in the `Post` class that returns a formatted string representation of the object.

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

    def __str__(self) -> str:
        return f'Post(userId={self.userId}, id={self.id}, title={self.title}, body={self.body})'
    
    
post = Post(userId=1, id=101, title="My First Post", body="This is the content of my first post.")
print(post)
