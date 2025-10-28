class Pipeline:
    def __init__(self):
        self._filters = []

    def add_filter(self, filter_instance):
        self._filters.append(filter_instance.filtering)
        return self

    def process(self, input_text):
        processed_text = input_text
        for filtering_function in self._filters:
            processed_text = filtering_function(processed_text)
        return processed_text
