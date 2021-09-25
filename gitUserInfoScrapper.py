from bs4 import BeautifulSoup
from collections import defaultdict
import requests

username = input()




def getUserRepos(username):
    url = "http://www.github.com/"+username+"?tab=repositories";
    r =  requests.get(url);
    soup = BeautifulSoup(r.content,"html5lib")
    
    Repos = []

    for data in soup.find_all("div",class_= "col-10 col-lg-9 d-inline-block"):

        name = data.find('a',itemprop="name codeRepository").getText().strip()
        typee = data.find('span',class_= "Label Label--secondary v-align-middle ml-1 mb-1").getText()
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
        repo["Type"] = typee;
        repo["Description"] = description;
        repo["LastUpdatedOn"] = lastUpdatedOn;
        repo["WrittenIn"] = writtenIn;
        repo["Likes"] = likes;
        repo["Forks"] = forks;
        repo["License"] = license;

        Repos.append(repo)


    return Repos






        




ans = getUserRepos(username)

for i in ans:
    print(i,"\n----------------------------------\n")
  

  
    
    
    





# def getUserInfo(soup):
#     userInfo = dict()
#     userInfo["name"] = soup.find("span",class_= "p-name vcard-fullname d-block overflow-hidden" ).text.strip()
#     userInfo["username"] = soup.find("span",class_= "p-nickname vcard-username d-block" ).text.strip()
#     userInfo["linkdinprofie"] = soup.find("a",class_= "Link--primary" ).text.strip()

#     print(userInfo["name"],userInfo["username"],userInfo["linkdinprofie"])



# def getUserContributions(soup):
#     userContributions = ""

#     for data in soup.find_all("h2",class_= "f4 text-normal mb-2"):
#         userContributions += data.text.strip()
#     return userContributions


    

    

