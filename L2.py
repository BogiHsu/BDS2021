class Strategy():
    # option setting needed
    def __setitem__(self, key, value):
        self.options[key] = value

    # option setting needed
    def __getitem__(self, key):
        return self.options.get(key, '')

    def __init__(self):
        # strategy property
        self.subscribedBooks = {
            'Binance': {
                'pairs': ['BTC-USDT'],
            },
        }
        self.period = 10 * 60
        self.options = {}

        # user defined class attribute

    def on_order_state_change(self,  order):
        Log("on order state change message: " + str(order) + " order price: " + str(order["price"]))

    # called every self.period
    def trade(self, information):
        exchange = list(information['candles'])[0]
        pair = list(information['candles'][exchange])[0]
        target_currency = pair.split('-')[0]  #BTC
        base_currency = pair.split('-')[1]  #USDT
        target_currency_amount = self['assets'][exchange][target_currency] 
        base_currency_amount = self['assets'][exchange][base_currency] 

        if True: # buy
            return [
                {
                    'exchange': exchange,
                    'amount': 1 ,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                }
            ]
        else: #sell
            return [
                {
                    'exchange': exchange,
                    'amount': -target_currency_amount,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                }
            ]
