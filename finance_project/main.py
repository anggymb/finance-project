"""Main module of Finance Application."""
from typing import List
from fastapi import FastAPI
from finance_project.models.stocks import Stock
from finance_project.schemas.stock_schemas import Stockchema


app = FastAPI()

stocks: List[Stock] = [
    Stock("Apple Company", 102, "AAPL.US"),
    Stock("Microsoft Company", 78, "MICRO.US"),
    Stock("Google Company", 92, "GGLE.US")
]

@app.get("/stocks")
def  get_stocks():
    print(str(stocks))
    return stocks

@app.post("/stocks/create-stock")
def create_stocks(stock_body: Stockchema):
    stock = Stock(**stock_body.model_dump) 
    stocks.append(stock)

#código adicional tarea
@app.get("/strocks/{name}")
def get_stocks_name(name: str):
    for item in stocks:
        if name ==item.name:
            return item
    return None    



