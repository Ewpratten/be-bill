import re
import requests


def loadAllUrls():
    page = requests.get("https://billwurtz.com/notebook.html").text

    links = re.findall(r"HREF=\"(.*)\"style", page)

    return links

def dumpEach(urls):
    for url in urls:
        page = requests.get(f"https://billwurtz.com/{url}").text.strip().replace("</br>", "").replace("<br>", "").replace("\n", " ")

        data = re.findall(r"</head>(.*)", page, re.MULTILINE)
        
        # ensure data
        if len(data) == 0:
            continue;

        print(data[0])

urls = loadAllUrls()
print(f"Loaded {len(urls)} pages")
dumpEach(urls)