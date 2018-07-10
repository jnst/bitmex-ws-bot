from bitmex_websocket import BitMEXWebsocket
import configparser
import logging
from time import sleep


# Basic use of websocket.
def run():
    logger = setup_logger()

    config = configparser.ConfigParser()
    config.read('config/config.ini')

    ws = BitMEXWebsocket(endpoint=config['bitmex']['endpoint'], symbol="XBTUSD",
                         api_key=config['bitmex']['api_key'], api_secret=config['bitmex']['api_secret'])

    logger.info("Instrument data: %s" % ws.get_instrument())

    # Run forever
    while(ws.ws.sock.connected):
        logger.info("Ticker: %s" % ws.get_ticker())
        if ws.api_key:
            logger.info("Funds: %s" % ws.funds())
        logger.info("Market Depth: %s" % ws.market_depth())
        logger.info("Recent Trades: %s\n\n" % ws.recent_trades())
        sleep(10)

def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    run()
