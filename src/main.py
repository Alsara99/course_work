from src.views import main_view
from src.services import return_search
from src.reports import spending_by_weekday
import pandas as pd


def main(): # pragma: no cover
    path = "../data/operations.xlsx"
    df = pd.read_excel(path)
    main_view(path, "2019.5.17 0:0:0")
    return_search(df)
    spending_by_weekday(df)

main()