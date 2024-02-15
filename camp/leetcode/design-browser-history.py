class Node:
    
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.home_page = Node(homepage)
        self.current_page = self.home_page

    def visit(self, url: str) -> None:
        node = Node(url)
        self.current_page.next = node
        node.prev = self.current_page
        self.current_page = node

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.current_page == self.home_page:
                return self.home_page.value
            steps -= 1
            self.current_page = self.current_page.prev
        return self.current_page.value

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.current_page.next is None:
                return self.current_page.value
            steps -= 1
            self.current_page = self.current_page.next
        return self.current_page.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)