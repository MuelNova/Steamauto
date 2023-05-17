import requests
from apprise import logger
from apprise.decorators import notify


@notify(on="ftqq", name="Server酱通知插件")
def server_chan_notification_wrapper(body, title, notify_type, *args, **kwargs):
    token = kwargs['meta']['host']
    try:
        resp = requests.get(
            f'https://sctapi.ftqq.com/{token}.send?title={title}&desp={body}'
        )
        if resp.status_code == 200:
            if resp.json()['code'] == 0:
                logger.info('Server酱通知发送成功\n')
                return True
            else:
                logger.error('Server酱通知发送失败, return code = %d' % resp.json()['code'])
                return False
        else:
            logger.error(f'Server酱通知发送失败, http return code = {resp.status_code}')
            return False
    except Exception as e:
        logger.error('Server酱通知插件发送失败！')
        logger.error(e)
        return False

    # Returning True/False is a way to relay your status back to Apprise.
    # Returning nothing (None by default) is always interpreted as a Success
