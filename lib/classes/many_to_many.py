class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author,Author):
            raise Exception("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be of type str with 50 characters")
        
        self._author = author
        self._magazine = magazine
        self._title = title

        author.articles.append(self)
        magazine.articles.append(self)
        Article.all.append(self)

    @property
    def author(self):
        return self._author
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        raise Exception("Title is immutable anf cannot be changed")
        
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of type Magazine")
        if self._magazine != value:
            raise Exception("Cannot change the magazine once an article has been published")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a non-empty str")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @property
    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})



class Magazine:
    all = []
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2<= len(name) <= 16):
            raise Exception("Name must be of type str with 2-16 characters")
        if not isinstance(category, str) or len(category) <= 0:
            raise Exception("Category must be a non-empty str")
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return [author for author, count in author_count.items() if count > 2 ] or None