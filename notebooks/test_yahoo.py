from data.sources.yahoo import YahooFinanceAdapter


def main():
    adapter = YahooFinanceAdapter()

    stock_data = adapter.get_stock_data(
        stock_ticker="NESTLEIND.NS",
        start_date="2023-01-01",
    )

    if stock_data is not None:
        print(stock_data.tail())
        print("\n✅ Download Successful!")
    else:
        print("\n❌ Download Failed.")


if __name__ == "__main__":
    main()
