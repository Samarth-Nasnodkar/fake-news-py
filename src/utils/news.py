import newspaper

class News:
  def __init__(self) -> None:
    pass

  @staticmethod
  def fetchNewsContent(url: str) -> str:
    article = newspaper.Article(url)
    article.download()
    article.parse()
    return article.text