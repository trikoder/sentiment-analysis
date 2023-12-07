import re

from pydantic import BaseModel, validator


def remove_html_tag(raw_html: str) -> str:
    """
    Removes HTML tags from string input
    """
    cleaner = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
    clean_text = re.sub(cleaner, "", raw_html)
    return clean_text


def limit_string_length(text: str, max_length: int = 10000) -> str:
    return text[:max_length]


class Sentiment(BaseModel):
    """
    Class represents request body
    """

    user_review: str

    @validator("user_review", allow_reuse=True)
    def _check_empty_and_numeric_title(cls, text: str) -> str:
        if not text:
            raise ValueError("Must NOT be an empty string!")
        if text.isnumeric():
            raise ValueError("Must contain letters!")
        return text

    @validator("user_review")
    def _preprocess_text(cls, text: str) -> str:
        text = remove_html_tag(text)
        text = limit_string_length(text)
        return text
