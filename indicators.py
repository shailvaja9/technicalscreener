class Indicators:
    def __init__(self, indicators, stocks):
        self.indicators = indicators
        self.stocks = stocks

    def evaluate_indicators(self):
        for indicator in self.indicators:
            if indicator == "BolingerBands":
                bollinger_band = self.bollinger_bands(self.stocks)

    def bollinger_bands(self, stocks):
        pass


