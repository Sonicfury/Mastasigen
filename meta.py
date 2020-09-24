from author import Author

class Meta:

    def __init__(self, author: Author, title, short_description,
            long_description, lang, charset, theme, stylesheet, javascript):
        self.title = title
        self.short_description = short_description
        self.long_description = long_description
        self.lang = lang
        self.charset = charset
        self.theme = theme
        self.author = author
        self.stylesheet = stylesheet
        self.javascript = javascript

    def get_meta(self):

        return [self.author.get_author(), self.title, self.short_description,
                self.long_description, self.lang, self.charset, self.theme,
                self.stylesheet, self.javascript]