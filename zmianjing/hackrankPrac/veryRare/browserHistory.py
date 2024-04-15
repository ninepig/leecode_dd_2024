'''
BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x,
you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x,
you will forward only x steps. Return the current url after forwarding in history at most steps.
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.visit(homepage)

    ## Visits url from the current page. It clears up all the forward history.
    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = [] ## clear all forward cache

    def back(self, steps: int) -> str:
        ## have to be this otherwise it will list out of range
        while len(self.history) > 1 and steps > 0:
            self.future.append(self.history.pop()) ## by default it will pop the top of the statc
            steps -= 1
        return self.history[-1]
    def forward(self, steps: int) -> str:
        while self.future and steps > 0 :
            self.history.append(self.future.pop())
            steps -= 1

        # self.visit(self.history[-1])
        return self.history[-1]

class Node:
  def __init__(self, url: str):
    self.prev = None
    self.next = None
    self.url = url
class BrowserHistoryList:
  def __init__(self, homepage: str):
    self.curr = Node(homepage)

  def visit(self, url: str) -> None:
    self.curr.next = Node(url)
    self.curr.next.prev = self.curr
    self.curr = self.curr.next

  def back(self, steps: int) -> str:
    while self.curr.prev and steps > 0:
      self.curr = self.curr.prev
      steps -= 1
    return self.curr.url

  def forward(self, steps: int) -> str:
    while self.curr.next and steps > 0:
      self.curr = self.curr.next
      steps -= 1
    return self.curr.url