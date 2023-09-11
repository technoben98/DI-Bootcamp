class Pagination:
    def __init__(self, items = None, page_size = 10):
        self.items = [items[i:i + page_size] for i in range(0, len(items), page_size)]
        self.page_size = int(page_size)
        self.current_page = 1
        self.total_pages = int(len(items)/page_size)+1
        self.current_content = []
        

    def get_visible_items(self):
        self.current_content = self.items[self.current_page-1]
        print(self.current_content)
    
    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        else:
            self.current_page = self.total_pages
        return self

    
    def nextPage(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        else:
            self.current_page = 1
        return self
    
    def firstPage(self):
        self.current_page = 1
    
    def lastPage(self):
        self.current_page = self.total_pages

    def goToPage(self, pageNum):
        if 1 <= pageNum <= self.total_pages:
            self.current_page = pageNum
        elif pageNum <= 0:
            self.current_page = 1
        elif pageNum > self.total_pages:
            self.current_page = self.total_pages

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
p.get_visible_items()
p.nextPage().nextPage().nextPage()
p.nextPage().nextPage().nextPage()
p.nextPage().nextPage().nextPage()
p.get_visible_items()
p.nextPage().prev_page().nextPage().prev_page().nextPage()
p.get_visible_items()
p.firstPage()
p.get_visible_items()
p.lastPage()
p.get_visible_items()
p.goToPage(3)
p.get_visible_items()
p.goToPage(8)
p.get_visible_items()
p.goToPage(-3)
p.get_visible_items()