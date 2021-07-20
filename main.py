from AIFactoryDS.AbstractProcesses import Preprocessor


class SamplePreprocessor(Preprocessor):
    def load_original_data(self, **kwargs):
        pass

    def save_processed_data(self, **kwargs):
        pass

    def process(self, **kwargs):
        pass

    def split_dataset(self, **kwargs):
        pass

    def __repr__(self):
        self.representation += 'This is sample class.'
        return self.representation


if __name__=='__main__':
    s = SamplePreprocessor()
    print(s)
    del s
