import pandas as pd

class Pandas:
    def get_pandas_series(self, start, end):
        numbers = range(start, end + 1)
        return pd.Series(numbers)

    def add_panda_series(self, series1, series2):
        return series1 + series2
    def sub_panda_series(self, series1, series2):
        return series1 - series2
    def mul_panda_series(self, series1, series2):
        return series1 * series2
    def div_panda_series(self, series1, series2):
        return series1 / series2

    def lstrip_panda_series(self, series):
        striped_series = series.map(lambda s: str(s).lstrip())
        return striped_series

    def rstrip_panda_series(self, series):
        striped_series = series.map(lambda s: str(s).rstrip())
        return striped_series

    def strip_panda_series(self, series):
        striped_series = series.map(lambda s: str(s).strip())
        return striped_series

    def create_pandas_series(self, dictionary):
        return pd.Series(dictionary)

if __name__ == '__main__':
    pandas = Pandas()
    # series1 = pandas.get_pandas_series(1, 10)
    # series2 = pandas.get_pandas_series(11, 20)
    #
    # print(pandas.add_panda_series(series1, series2))
    # print(pandas.sub_panda_series(series1, series2))
    # print(pandas.mul_panda_series(series1, series2))
    # print(pandas.div_panda_series(series1, series2))

    #series = pd.Series([' Aron', 'Jackson  ', '  Ahree  ', 'Sam'])

    #print(list(pandas.lstrip_panda_series(series)))
    #print(list(pandas.rstrip_panda_series(series)))
    #print(list(pandas.strip_panda_series(series)))

    dictionary = {'Sam':89, 'Aron':82, 'Gray':78, 'Isla':93, 'Ahree':87}
    print(pandas.create_pandas_series(dictionary))