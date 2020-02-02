from src.project_utils import remove_punctuation, get_word_count
import pytest
import os


@pytest.mark.parametrize("input_str, output_str",[
    ('hello!123.', 'hello123'),
    ('Goodbye!!!!!!', 'Goodbye'),
    ('YOLO! Hey! I am back.', 'YOLO Hey I am back'),
])
def test_remove_punctuation(input_str, output_str):
    assert remove_punctuation(input_str) == output_str


def test_get_word_count():
    curr_dir = os.getcwd()
    input_filename = os.path.join(curr_dir, 'test_file.txt')
    actual_word_dict = get_word_count(input_filename)
    expected_word_dict = {'Hello': 1,
                          'I': 2,
                          'am': 2,
                          'a': 1,
                          'string': 2,
                          'test': 1}
    assert actual_word_dict == expected_word_dict
