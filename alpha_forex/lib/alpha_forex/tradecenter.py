# -------------------------------------------------------------------------------------------------
# TradeCenter Module
# -------------------------------------------------------------------------------------------------
# Author: Maxime Sirois
# -------------------------------------------------------------------------------------------------
"""
The Trade Center where user can buy or sell currencies.
"""
# -------------------------------------------------------------------------------------------------


class TradeCenter:
    def __init__(self, user, api_client):
        self.user = user
        self.client = api_client
        self.std_unit = 100000
        self.leverage = 33
        self.position_required = 1 / self.leverage

    def buy(self, from_currency, to_currency, lot_size):
        quote = self.client.get_rate(from_currency, to_currency)
        rate = float(quote.get('ASK_PRICE'))
        price = self.get_price(rate, lot_size)
        if price > self.user.wallet.balance:
            print(f"Not enough funds (Current balance: {self.user.wallet.balance}$, "
                  f"tried to buy {price}$)")
        else:
            print(f"You just bought currencies for {price}$")

    def get_price(self, rate, lot_size):
        return round(rate * (self.std_unit * lot_size) * self.position_required, 2)

    def sell(self, from_currency, to_currency, lot_size):
        pass

    def close(self, transaction_id):
        pass

    def _calculate_pips(self, rate):
        weight = 0.01 if (float(rate) / 100) > 1 else 0.0001
        pass
