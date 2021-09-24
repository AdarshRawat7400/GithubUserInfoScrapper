from bs4 import BeautifulSoup
#from collections import defaultdict
import requests
import json
from flask import Flask


app = Flask(__name__)

def checkUser(user):
    url = f"https://api.github.com/users/{user}"
    r = requests.get(url.format(user)).json()
    try:
        return r['login']
    except:
        return False


def getUserRepos(uname):
    url = "http://www.github.com/"+uname+"?tab=repositories";
    r =  requests.get(url);
    soup = BeautifulSoup(r.content,"html5lib")
    
    Repos = []

    for data in soup.find_all("div",class_= "col-10 col-lg-9 d-inline-block"):

        name = data.find('a',itemprop="name codeRepository").getText().strip()
        access_type = data.find('span',class_= "Label Label--secondary v-align-middle ml-1 mb-1").getText()
        description = data.find('p',itemprop="description")

        if description == None:
            description = "Not Available"
        else:
            description = description.getText().strip()

        lastUpdatedOn = "Last Updated On"+data.find("relative-time",class_="no-wrap").getText()
        
        writtenIn = data.find("span",itemprop="programmingLanguage")
        if writtenIn == None:
            writtenIn == "UnKnown"
        else:
            writtenIn = writtenIn.getText()

        likes = data.find(class_='octicon octicon-star')
        if likes == None:
            likes = "0"
        else:
            likes = likes.parent.text.strip()

        forks = data.find(class_="octicon octicon-repo-forked")
        if forks == None:
            forks = "0"
        else:
            forks = forks.parent.text.strip()
        
        license = data.find(class_="octicon octicon-law mr-1");
        if license == None:
            license = "Not Licensed";
        else:
            license = license.parent.text.strip()
        
        repo = dict()

        repo["Name"] = name;
        repo["Access"] = access_type;
        repo["Description"] = description;
        repo["LastUpdatedOn"] = lastUpdatedOn;
        repo["WrittenIn"] = writtenIn;
        repo["Likes"] = likes;
        repo["Forks"] = forks;
        repo["License"] = license;

        Repos.append(repo)

    return Repos



def getUserInfo(soup):

    userInfo = dict()
    
    for data in soup.find_all("div",class_="js-profile-editable-replace"):
        name = data.find("span",itemprop="name").getText().strip();
        uname = data.find("span",itemprop = "additionalName").getText().strip();
        bio = data.find("div",class_ = "d-flex flex-items-center p-2 width-full")
        if bio == None:
            bio = "Not Available";
        else:
            bio = " ".join(bio.getText().strip().split())
        
        organisation = data.find(class_="octicon octicon-organization")
        if organisation == None:
            organisation = "Not Available"
        else:
            organisation = organisation.parent.text.strip()

        location = data.find(class_="octicon octicon-location")
        if location == None:
            location = "Not Available"
        else:
            location = location.parent.text.strip()
        
        mail = data.find(class_="octicon octicon-mail")
        if mail == None:
            mail = "Not Available"
        else:
            mail = mail.parent.text.strip()

        website = data.find(class_="octicon octicon-link")
        if website == None:
            website = "Not Available"
        else:
            website = website.parent.text.strip()
        
        followers = data.find(class_="octicon octicon-people")
        if followers == None:
            followers = "0"
        else:
            followers = " ".join(followers.parent.text.strip().split())

        following = data.find("span",href = "https://github.com/fabpot?tab=followers")
        if following == None:
            following = "0"
        else:
            following = following.getText().strip()+" followers"

        
        rating = data.find(class_="octicon octicon-star")
        if rating == None:
            rating = "0"
        else:
            rating = rating.parent.text.strip()+" rating"

        highlights = data.find(class_="octicon octicon-cpu color-text-tertiary mr-1")
        if highlights == None:
            highlights = "Not Available"
        else:
            highlights = highlights.parent.text.strip()

        twitter = data.find(class_="vcard-detail pt-1 css-truncate css-truncate-target hide-sm hide-md",itemprop="twitter")
        if twitter == None:
            twitter = "Not Available"
        else:
            twitter = twitter.getText().split()[1]


        # achivements = data.find("img",alt=True,class_="d-flex")
        # if achivements != None:
        #     print(achivements)
        
        userInfo["Name"] = name;
        userInfo["UserName"] = uname;
        userInfo["Bio"] = bio;
        userInfo["Organisation"] = organisation;
        userInfo["Location"] = location;
        userInfo["Mail"] = mail;
        userInfo["Website"] = website;
        userInfo["Followers"] = followers;
        userInfo["Follwing"] = following;
        userInfo["Rating"] = rating;
        userInfo["HighLights"] = highlights;
        userInfo["TwitterId"] = twitter;

    return userInfo;




def getUserContributions(soup):

    contributedTo = []
    
    for data in soup.find_all("div",class_="select-menu-list"):
         contributedTo = ["https://github.com/"+i[1:] for i in data.getText().strip().split()[:-3]]

    return contributedTo;

    
    
#ans = getUserRepos(username)

@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/uname/<string:username>")
def scrapper(username):
    if checkUser(username) == False:
        return "Github User Not Exist"
    try:
        url = "http://www.github.com/"+username;
        r =  requests.get(url);
        soup = BeautifulSoup(r.content,"html5lib")

        Response = dict()
        Response["UserInformation"] = getUserInfo(soup);
        Response["Repositories"] = getUserRepos(username);
        Response["ContributionForOrganistions"] = getUserContributions(soup);

        Response = json.dumps(Response,indent=6);
    except Exception:
        print(Exception)
    return  Response;


if __name__ == "__main__":
    app.run(debug=True)


#username = input("Enter UserName :- ")












#getUserContributions(soup)
# for key,val in ans.items():
#     print(key,"  - - - > ",val)

# for i in ans:
#    print(i,"\n----------------------------------\n")
  

  
    
    
    






    

    

