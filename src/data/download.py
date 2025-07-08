# download raw stock data

import logging
from pathlib import Path

from data.sources.yahoo import YahooFinanceAdapter

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


def download_and_save_stock(
    ticker: str, start_date: str, end_date: str, interval: str = "1d"
) -> None:
    stock_data = YahooFinanceAdapter()
    stock_df = stock_data.get_stock_data(
        stock_ticker=ticker, start_date=start_date, end_date=end_date, interval=interval
    )

    if stock_df is not None:
        raw_dir = Path("data") / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)

        output_path = raw_dir / f"{ticker}.csv"
        stock_df.to_csv(output_path)
        logger.info(f"✅ Stock Data saved to {output_path} successfully")

    else:
        logger.warning("⚠️ Download Failed. No File Saved")


if __name__ == "__main__":
    ticker = input("Enter Stock Name: ")
    start_date = input("Enter Start Date: ")
    end_date = input("Enter End Date: ")

    download_and_save_stock(ticker=ticker, start_date=start_date, end_date=end_date)
