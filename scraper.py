from bs4 import BeautifulSoup as BS
import os
import requests
import sys

def get_page_text(url):
    file = url.split("/")[-1]
    if os.path.isfile(file):
        html_text = open(file).read()
        return html_text
    else:
        resp = requests.get(url)
        fout = open(file, "wt")
        fout.write(resp.text)
        return resp.text

def get_page_text_huffpo(url):
    file = url[url.find('entry/') + 6: url.find('_us_')]
    if os.path.isfile(file):
        html_text = open(file).read()
        return html_text
    else:
        resp = requests.get(url)
        fout = open(file, "wt")
        fout.write(resp.text)
        return resp.text

def fox_article(html_text):
    soup = BS(html_text, "html.parser")
    article = soup.body.find('div', attrs={'class': 'article-body'})
    article_text = ""
    for p in article.find_all('p'):
        article_text += '' + p.text
    return article_text

def npr_article(html_text):
    soup = BS(html_text, "html.parser")
    article = soup.body.find('div', attrs={'id': 'storytext', 'class':'storytext storylocation linkLocation'})
    article_text = ""
    for p in article.find_all('p'):
        article_text += ' ' + p.text
    return article_text

def newyorker_article(html_text):
    soup = BS(html_text, "html.parser")
    article = soup.body.find('div', attrs={'class': 'SectionBreak__sectionBreak___1ppA7'})
    article_text = ""
    for p in article.find_all('p'):
        article_text += ' ' + p.text
    return article_text

def huffpo_article(html_text):
    soup = BS(html_text, "html.parser")
    article = soup.body.find('div', attrs={'id': 'entry-text', 'class': 'entry_text js-entry-text bn-entry-text yr-entry-text', 'data-beacon':'{p:{mlid:entry_text}}', 'data-beacon-parsed': 'true', 'data-rapid-parsed': 'sec'})
    article_text = ""
    for p in article.find_all('p'):
        for tag in p:
            article_text += ' ' + tag.text
    return article_text

if __name__=="__main__":
    fox_text = get_page_text("http://www.foxnews.com/politics/2018/03/01/trumps-punching-bag-how-much-longer-will-sessions-endure-thrashing.html")
    fox2_text = get_page_text("http://www.foxnews.com/entertainment/2018/03/08/disney-boss-tells-shareholders-that-view-star-joy-behar-apologized-for-anti-christian-remarks-report-says.html")

    newy_text = get_page_text("https://www.newyorker.com/magazine/2018/03/19/donald-trump-and-the-stress-test-of-liberal-democracy")
    print(newyorker_article(newy_text))

    npr_text = get_page_text("https://www.npr.org/sections/thesalt/2018/03/08/591568943/hennessy-hauls-raise-concerns-about-new-hampshire-s-tax-free-liquor-business")
    npr2_text = get_page_text("https://www.npr.org/2018/03/08/591524460/trumps-cabinet-scandals-is-abuse-of-office-contagious")
    #print(npr_article(npr2_text))

    #print(get_page_text_huffpo("https://www.huffingtonpost.com/entry/trump-universal-background-checks_us_5aa59af2e4b086698a9ef64d"))


    # TODO change file naming convention for breitbart/ny times


# google web servies API
# maybe better for static location
# pandas for table manipulation
#
