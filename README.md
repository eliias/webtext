# webtext

> Uniform web text processing

The _webtext_ library offers a uniform interface for online text processing.
It allows developers to abstract text from e.g. a website, so that it can be
easily pre-processed, analysed, filtered, and transformed. A common use case
is pre-processing and filtering for NLP use cases (and LLMs).

## Usage

```bash
pip install webtext
```

### Parts


```python
from webtext import WebText

text = WebText("This is some text.\n\nAnother paragraph.")
text.paragraphs()
text.sentences()
text.words()
```

## Contributing

### Tests

```bash
python -m pytest
```

### Release

```bash
poetry build
poetry publish
```
