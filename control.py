from functools import partial

class QControl:
    def __init__(self, viewUI, model):
        self.view = viewUI
        self.evaluate = model
        self.connectSignals()

    def buildExpression(self, subExpression):
        expression = self.view.displayText() + subExpression
        self.view.setDisplayText(expression)

    def connectSignals(self):
        for key, value in self.view.buttons.items():
            if key not in {'=', 'C'}:
                value.clicked.connect(partial(self.buildExpression, key))
            #if
        #for
        self.view.buttons['C'].clicked.connect(self.view.clearDisplay)

    def calculateResult(self):
        result = self.evaluate(expression = self.view.displayText())
        self.view.setDisplayText(result)

