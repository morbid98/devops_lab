import requests as req
import getpass

user = input("Your username ")
password = getpass.getpass()
rep_user = input("Someones git ")
rep = input("Repository ")
git = 'https://api.github.com/'
search = 'search/issues?q=+type:pr+repo:'
state = "+state:open+"
sort = "in:title&sort=created&order=asc"
pull_path = 'repos/' \
            + rep_user \
            + '/' \
            + rep \
            + '/pulls'
surname = input("Enter something to search in title ")
search_pat2 = req.get(
    git + search + rep_user + '/' + rep + state + surname + sort,
    auth=(user, password)).json()
found_total = search_pat2['total_count']
for i in range(found_total):
    number = search_pat2['items'][i]['number']
    pull_info = req.get(git + pull_path + '/' + str(number),
                        auth=(user, password)).json()
    data = req.get(
        git + pull_path + '/' + str(number) + '/files',
        auth=(user, password)).json()
    print("\nPull request %s info" % number)
    print("======================")
    print("Title: %s" % (str(pull_info['title'])))
    print("Create time: %s" % (str(pull_info['created_at'])))
    print("Update time: %s" % (str(pull_info['updated_at'])))
    print("Showing two last changes")
    for j in data:
        print("Changed %s file" % str(j['filename']))
        print("%s lines added" % str(j['additions']))
        print("%s lines deleted" % str(j['deletions']))
    else:
        print("=======================")
else:
    print("Done")
