from pathlib import Path
import string as st
import pandas as pd
import yfinance as yf
import ffin.utils as f_ut
import ffin


class TickerDownloader(yf.Tickers):
    def __init__(self, tickers: str):
        self.last_download = None

    def update_last_download(self, last_download):
        pass

    def download_info(self, ticker) -> dict:
        pass

    def download_history(self, ticker) -> pd.DataFrame:
        pass


class TickerIOHandler:
    def __init__(self, home_dir: Path = ffin.HOME_DIR):
        self.home = home_dir

    def verify_filename(self, name: str) -> bool:
        """
        Returns true if the given name contains ONLY
        ascii digits and ascii uppercase/lowercase letters
        before the extension dot
        """
        FOLDER_SEPARATOR = '/'
        NAME_SPACING = "_"

        is_valid = True
        first_letter = True

        for letter in name:
            if letter not in (st.ascii_letters + st.digits + FOLDER_SEPARATOR + NAME_SPACING):
                if letter != '.':
                    is_valid = False
                break
            first_letter = False

        return (is_valid and not first_letter)


class TickerWriter(TickerIOHandler):
    def __init__(self, home_dir: Path):
        pass

    def write_df(self, ticker: pd.DataFrame, filename: str):
        pass

    def write_info(self, ticker: dict, filename: str):
        pass

    def write(self, ticker: f_ut.TICKER_DATA_TYPES, filename: str):
        # make different writes for dict & DataFrame
        pass


class TickerReader(TickerIOHandler):
    def __init__(self, home_dir: Path):
        pass

    def read_df(self, file) -> pd.DataFrame:
        pass

    def read_info(self, file) -> dict:
        pass

    def read(self, file) -> f_ut.TICKER_DATA_TYPES:
        pass


class TickerChecker(TickerReader):
    def __init__(self, home_dir: Path):
        pass

    def update(self, filename: str) -> bool:
        # download latest ticker data for dict or DataFrame
        pass

    def needs_update_check(self, filename: str) -> bool:
        # check how old is file's content, if too old, update
        pass
