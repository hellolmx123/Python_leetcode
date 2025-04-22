class BrowserHistory:

    def __init__(self, homepage: str):
        self.Stack = [homepage]
        self.tag = 0
        self.top = 1

    def visit(self, url: str) -> None:
        self.Stack = self.Stack[0:self.tag+1]
        self.Stack.append(url)
        self.tag += 1
        self.top = self.tag+1

    def back(self, steps: int) -> str:
        if steps > self.tag:
            self.tag = 0
        else:
            self.tag -= steps
        print(self.Stack[self.tag])
        return self.Stack[self.tag]

    def forward(self, steps: int) -> str:
        if steps >= self.top - self.tag:
            self.tag = self.top-1
        else:
            self.tag += steps
        print(self.Stack[self.tag])
        return self.Stack[self.tag]

BrowserHistory.__init__(BrowserHistory,"LeetCode.com")
BrowserHistory.visit(BrowserHistory,"google.com")
BrowserHistory.visit(BrowserHistory,"facebook.com")
BrowserHistory.visit(BrowserHistory,"youtube.com")
BrowserHistory.back(BrowserHistory,1)
BrowserHistory.back(BrowserHistory,1)
BrowserHistory.forward(BrowserHistory,1)
BrowserHistory.visit(BrowserHistory,"linkedin.com")
BrowserHistory.forward(BrowserHistory,2)
BrowserHistory.back(BrowserHistory,2)
BrowserHistory.back(BrowserHistory,7)