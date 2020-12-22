#https://finnhub.io/docs/api#websocket-trades

import websocket

def on_message(ws,message):
	print(message)
    
def on_error(we, error):
    print(error)

def on_close(ws):
    print("-----CLOSED-----")
  
def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"TSLA"}')
  
if __name__ = "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token="API TOKEN",
			on_message = on_message,
			on_error = on_error,
			on_close = on_close,
	ws.on_open = on_open
	ws.run_forever()
								 
#API TOKEN  =  your free api token from your finnhub account 
#note that this program runs forever, you can specify times more custom to your own needs
