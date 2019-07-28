from panflute import io

from stdio_mgr import stdio_mgr


def test_stdin():
    with open('./tests/1/api117/benchmark.json', encoding='utf-8') as f:
        input_data = f.read()

    with open('./tests/1/api117/panflute.json', encoding='utf-8') as f:
        output_data = f.read().strip()

    with stdio_mgr(input_data) as (in_, out_, err_):
        # The buffer will be detached, so capture it here
        # buffer_ = out_.buffer
        doc = io.load()
        io.dump(doc)
        # buffer_.seek(0, 0)
        assert out_.getvalue() == output_data
