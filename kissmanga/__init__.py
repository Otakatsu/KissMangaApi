from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

def Filter(text: str):
    K = text.split(" ")
    K.remove(K[0])
    result = " ".join(K)
    return result
       
def get_search_results(query):  
        try:
            mangalink = f"http://kissmanga.nl/search?q={query}"
            response = requests.get(mangalink)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'lxml')
            source_url = soup.findAll("div", {"class": "media-body"})
            res_search_list = []
            for links in source_url:
                a = links.find('a')
                title = a.find('h4').text
                mangaId = a['href']
                mangaid = mangaId.split("/").pop()
                res_search_list.append({"title":f"{title}","mangaid":f"{mangaid}"})
            if res_search_list == []:
                return {"status":"204", "reason":"No search results found for the query"}
            return res_search_list
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}


def get_manga_details(mangaid):  
        try:
            mangalink = f"http://kissmanga.nl/manga/{mangaid}"
            response = requests.get(mangalink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            mangainfo = soup.find("div", {"class": "media-body"})
            manga = soup.find("p", {"class": "description-update"}).text
            image = soup.find("div", {"class": "media-left cover-detail"})
            imageurl = image.find('img')['src']
            description = soup.find("div", {"class": "manga-content"}).p.text.strip()
            title = mangainfo.h1.text
            manSplit = manga.split("\n")
            genres = []          
            status = []
            alternative = []
            view = []
            author = []
            status = []
            for i in manSplit:
                if "Alternative" in i:
                    alternative.append(Filter(i.strip()))
                if "View" in i:
                    view.append(Filter(i.strip()))
                if "Author(s)" in i:       
                    author.append(Filter(i.strip()[:-1]))
                if "Status" in i:               
                    status.append(Filter(i.strip()))
                if "\r" in i:
                    genres.append(i.strip()[:-1])
                genrek = ", ".join(genres)
                statusk = ", ".join(status)
                alternativek = ", ".join(alternative)
                viewk = ", ".join(view)
                authork = ", ".join(author)
                res_search_list = {"title":f"{title}","description":f"{description}","image":f"{imageurl}","status":f"{statusk}","view":f"{viewk}","author":f"{authork}","alternative":f"{alternativek}","genre":f"{genrek}"}          
            return res_search_list
        except AttributeError:
            return "Wrong Mangaid"
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}



def get_manga_episode(mangaid):  
        try:
            animelink = f"http://kissmanga.nl/manga/{mangaid}"
            response = requests.get(animelink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            source_url = soup.findAll("div", {"class": "chapter-list"})[1].find_all('h4')
            titleUrl = soup.find("div", {"class": "media-left cover-detail"})
            title = titleUrl.find('img')['alt']
            lastChapList = []
            for links in source_url:
                chap = links.find('a')['title']
                chapSplit = chap.split(" ")
                chapterNumber = chapSplit.pop()
                lastChapList.append(chapterNumber)
            lastChapterNo = len(lastChapList)
            res_search_list = {"title":f"{title}","totalchapter":f"{lastChapterNo}"}          
            return res_search_list
        except AttributeError:
            return "Wrong MangaId"
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}


def get_manga_chapter(mangaid, chapNumber):  
        try:
            mangalink = f"http://kissmanga.nl/{mangaid}-chapter-{chapNumber}"
            response = requests.get(mangalink)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'lxml')
            source_url = soup.find("p", id="arraydata")
            totalPages = source_url.text.split(",")
            res_search_list = {"totalPages":f"{totalPages}"}
            return res_search_list
        except AttributeError:
            return "Invalid Mangaid or chapter number"
        except requests.exceptions.ConnectionError:
            return {"status":"404", "reason":"Check the host's network Connection"}
