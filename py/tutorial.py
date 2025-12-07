TIPS = {
    "price": "Economics 101: Law of Demand. Generally, as price goes up, demand goes down. This is called 'Price Elasticity'.",
    "inventory": "Supply Chain: Carrying too much stock ties up your cash (Liquidity). Carrying too little leads to 'Stockouts' and lost revenue.",
    "marketing": "Marketing creates brand awareness, shifting the demand curve to the right. However, it has diminishing returns.",
    "cash": "Cash Flow vs Profit: You can be profitable (making money on each unit) but still go bankrupt if you run out of cash to pay bills today.",
    "employees": "Labor is a cost, but also a driver of capacity. In this game, more staff suggests stability, though we simplify their output.",
    "loan": "Leverage: Using borrowed money to grow. Good if your Return on Investment (ROI) > Interest Rate. Bad if you can't pay it back."
}
def get_tip(topic):
    return TIPS.get(topic, "Buy low, sell high.")