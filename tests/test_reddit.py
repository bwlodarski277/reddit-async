import pytest

from reddit import Reddit


class TestInit:
    @pytest.mark.asyncio
    async def test_invalid_input(self):
        with pytest.raises(ValueError):
            reddit = await reddit.init('', '', '', '')

    async def test_valid_input(self):
        reddit = await reddit.init()
        assert 'error' not in reddit.auth
