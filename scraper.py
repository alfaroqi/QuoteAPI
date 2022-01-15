from requests_html import HTMLSession

class Scrap():

    def scrapData(self, tag):
        url = f'https://quotes.toscrape.com/tag/{tag}'
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

        qlist = []

        quotes = r.html.find('div.quote')

        for q in quotes:
            item = {
                'text': q.find('span.text', first=True).text.strip(),
                'Author': q.find('small.author', first=True).text.strip()   
            }
            # print for checker
            print(item) 
            qlist.append(item)

        return qlist

    # format the data json
    def formatData(self, data):
        formattedData = []
        for item in data:
            formattedData.append({
                'quotes': item['text'],
                'author': item['Author']
            })
        return formattedData


    


