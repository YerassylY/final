>>> from newspaper import Article

>>> url = u'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
>>> article = Article(url)
>>> article.download()

>>> article.html
u'<!DOCTYPE HTML><html itemscope itemtype="http://...'
>>> article.parse()

>>> article.authors
[u'Leigh Ann Caldwell', u'John Honway']

>>> article.publish_date
datetime.datetime(2013, 12, 30, 0, 0)

>>> article.text
u'Washington (CNN) -- Not everyone subscribes to a New Year's resolution...'

>>> article.top_image
u'http://someCDN.com/blah/blah/blah/file.png'

>>> article.movies
[u'http://youtube.com/path/to/link.com' ...]
>>> article.nlp()

>>> article.keywords
[u'New Years', u'resolution', ...]

>>> article.summary
u'The study shows that 93% of people ...'
>>> import newspaper

>>> cnn_paper = newspaper.build(u'http://cnn.com')

>>> for article in cnn_paper.articles:
>>>     print(article.url)
http://www.cnn.com/2013/11/27/justice/tucson-arizona-captive-girls/
http://www.cnn.com/2013/12/11/us/texas-teen-dwi-wreck/index.html
...

>>> for category in cnn_paper.category_urls():
>>>     print(category)

http://lifestyle.cnn.com
http://cnn.com/world
http://tech.cnn.com
...

>>> cnn_article = cnn_paper.articles[0]
>>> cnn_article.download()
>>> cnn_article.parse()
>>> cnn_article.nlp()
...
>>> from newspaper import fulltext

>>> html = requests.get(...).text
>>> text = fulltext(html)