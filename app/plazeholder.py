import requests as reqs

#Get plaze_hoder information to https://jsonplaceholder.typicode.com/posts/
#If title or body not exist or request error set with  ""
def plazeHolder(number):
    try:
        response = reqs.get("https://jsonplaceholder.typicode.com/posts/"+str(number),timeout=2)
        if  response.json().get("title"):
            title = response.json()["title"]
        else:
            title = ""
        if response.json().get("body"):
            body = response.json()["body"]
        else:
            body = ""
        return title, body
    except reqs.exceptions.RequestException as e:
        title, body = "", ""
        print(e)
        return title, body