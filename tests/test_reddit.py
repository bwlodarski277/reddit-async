import pytest

from core.reddit import Reddit


class TestInit:
    @pytest.mark.asyncio
    async def test_invalid_input(self):
        with pytest.raises(ValueError):
            reddit = await Reddit.init('', '', '', '')

    @pytest.mark.asyncio
    async def test_valid_input(self):
        reddit = await Reddit.init()
        assert 'error' not in reddit.auth
