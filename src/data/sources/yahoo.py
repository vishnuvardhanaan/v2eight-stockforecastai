import logging
from datetime import date, timedelta

import pandas as pd
import yfinance as yf

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)


class YahooFinanceAdapter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_stock_data(
        self, stock_ticker: str, start_date: str, end_date: str, interval: str = "1d"
    ):
        """
        Downloads historical stock price data from Yahoo Finance.

        Args:
            stock_ticker (str): Stock symbol (e.g., 'AAPL').
            start_date (str): Start date in 'YYYY-MM-DD' format.
            end_date (str): End date in 'YYYY-MM-DD' format.
            interval (str): Data interval (e.g., '1d', '1wk', '1mo').

        Returns:
            pd.DataFrame: Stock data as a Pandas DataFrame.
        """

        try:
            self.logger.info(
                f"Downloading Stock: {stock_ticker} Data from {start_date} to {end_date}"
            )

            stock_data = yf.download(
                stock_ticker,
                start=start_date,
                end=end_date,
                interval=interval,
                auto_adjust="True",
            )

            if stock_data.empty:
                self.logger.warning(
                    f"Stock Data for {stock_ticker} is not downloaded. Check if ticker is correct."
                )

            else:
                self.logger.info(
                    f"Stock Data for {stock_ticker} is downloaded successfully. Shape: {stock_data.shape}"
                )

                return stock_data

        except Exception as e:
            self.logger.error(f"Error downloading stock data for {stock_ticker}: {e}")
            return None
