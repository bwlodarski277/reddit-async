import requests
import aiohttp
import asyncio

oauth_url = 'https://oauth.reddit.com/'
base_url = 'https://www.reddit.com/'


class Reddit(object):
    """The class for interacting with the Reddit API.

    To begin using this class, the ``init`` function needs to be called::

        reddit = await Reddit.init('your', 'args', 'go', 'here')

    :raises ValueError: if the ``init`` function fails to authenticate the bot.
    """
    @classmethod
    async def init(cls, username: str, password: str, app_id: str, app_secret: str):
        """Authenticates the bot given the user's and bot's details.

        :param username: Bot owner's Reddit account username.
        :type username: str
        :param password: Bot owner's Reddit account password.
        :type password: str
        :param app_id: Reddit application ID.
        :type app_id: str
        :param app_secret: Reddit application secret.
        :type app_secret: str
        :raises ValueError: if the bot fails to authenticate.
        :return: An authenticated Reddit class instance.
        :rtype: Reddit
        """
        self = Reddit
        async with aiohttp.ClientSession() as session:
            data = {'grant_type': 'password',
                    'username': username, 'password': password}
            auth = aiohttp.BasicAuth(app_id, app_secret)
            async with session.post(url=base_url + 'api/v1/access_token',
                                    data=data,
                                    auth=auth) as response:
                self.auth = await response.json()
                if 'error' in self.auth:
                    msg = f'Failed to authenticate: {self.auth["error"]}'
                    if 'message' in self.auth:
                        msg += ' - ' + self.auth['message']
                    raise ValueError(msg)
                return self


async def main():
    reddit = await Reddit.init()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
