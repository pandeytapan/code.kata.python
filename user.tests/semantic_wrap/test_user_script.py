import unittest
from textwrap import dedent
import re
SENTENCE_END_CHARS = ('.', '?', '!')


# def semantic_wrap(text):
#     for char in SENTENCE_END_CHARS:
#         text = text.replace(f'{char}  ', f'{char}\n')
#         text = text.replace(f'{char} ', f'{char}\n')
#     return text


def semantic_wrap(input_string):
    pattern = re.compile(r'([.?!])[ ]+')
    return pattern.sub(r'\1\n', input_string)

class SemanticWrapTests(unittest.TestCase):

    """Tests for semantic_wrap"""

    maxDiff = None

    # def test_wrap_with_quotes(self):
    #     text = dedent("""
    #         I prefer putting quotes "inside the period". But not everyone does.

    #         Some put "quotes outside punctuation." It's quite common actually.
    #     """).lstrip()
    #     expected = dedent("""
    #         I prefer putting quotes "inside the period".
    #         But not everyone does.

    #         Some put "quotes outside punctuation."
    #         It's quite common actually.
    #     """).lstrip()
    #     self.assertEqual(semantic_wrap(text), expected)

    # def test_multiple_sentences_and_multiple_paragraphs(self):
    #     text = (
    #         "Multiple assignment (also known as tuple unpacking or iterable "
    #         "unpacking) allows you to assign multiple variables at the same "
    #         "time in one line of code. This feature often seems simple after "
    #         "you've learned about it, but **it can be tricky to recall "
    #         "multiple assignment when you need it most**."
    #         "\n\n"
    #         "In this article we'll see what multiple assignment is, we'll "
    #         "take a look at common uses of multiple assignment, and then "
    #         "we'll look at a few uses for multiple assignment that are "
    #         "often overlooked."
    #     )
    #     wrapped = (
    #         "Multiple assignment (also known as tuple unpacking or iterable "
    #         "unpacking) allows you to assign multiple variables at the same "
    #         "time in one line of code.\n"
    #         "This feature often seems simple after you've learned about it, "
    #         "but **it can be tricky to recall multiple assignment when you "
    #         "need it most**."
    #         "\n\n"
    #         "In this article we'll see what multiple assignment is, we'll "
    #         "take a look at common uses of multiple assignment, and then "
    #         "we'll look at a few uses for multiple assignment that are "
    #         "often overlooked."
    #     )
    #     self.assertEqual(semantic_wrap(text).strip(), wrapped)

    # def test_multiple_sentences_and_multiple_paragraphs(self):
    #     text = (
    #         "Multiple assignment (also known as tuple unpacking or iterable "
    #         "unpacking) allows you to assign multiple variables at the same "
    #         "time in one line of code. This feature often seems simple after "
    #         "you've learned about it, but **it can be tricky to recall "
    #         "multiple assignment when you need it most**."
    #         "\n\n"
    #         "In this article we'll see what multiple assignment is, we'll "
    #         "take a look at common uses of multiple assignment, and then "
    #         "we'll look at a few uses for multiple assignment that are "
    #         "often overlooked."
    #     )
    #     wrapped = (
    #         "Multiple assignment (also known as tuple unpacking or iterable "
    #         "unpacking) allows you to assign multiple variables at the same "
    #         "time in one line of code.\n"
    #         "This feature often seems simple after you've learned about it, "
    #         "but **it can be tricky to recall multiple assignment when you "
    #         "need it most**."
    #         "\n\n"
    #         "In this article we'll see what multiple assignment is, we'll "
    #         "take a look at common uses of multiple assignment, and then "
    #         "we'll look at a few uses for multiple assignment that are "
    #         "often overlooked."
    #     )
    #     self.assertEqual(semantic_wrap(text).strip(), wrapped)

    def test_different_punctuation_and_spacing(self):
        text = dedent("""
            This is a sentence.  It's followed by another sentence.

            This is a paragraph.  With three sentences.  Three?  Four!  Five.

            But this paragraph just has one sentence, a long one.
        """).lstrip()
        expected = dedent("""
            This is a sentence.
            It's followed by another sentence.

            This is a paragraph.
            With three sentences.
            Three?
            Four!
            Five.

            But this paragraph just has one sentence, a long one.
        """).lstrip()
        self.assertEqual(semantic_wrap(text), expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)
