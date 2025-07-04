import pytest
from src.main import *

class TestCreateStory:
    def fails_with_no_title(self, story: Story):
        with pytest.raises(AttributeError) as e:
            assert story["title"] not in (None, "", " ")