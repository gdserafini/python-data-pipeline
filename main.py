from pipeline.pipeline import Pipeline
from pipeline.data_handler import DataHandler


def main() -> None:
    data_handler = DataHandler()
    pipeline = Pipeline(data_handler)
    pipeline.run()


if __name__ == '__main__':
    main()
