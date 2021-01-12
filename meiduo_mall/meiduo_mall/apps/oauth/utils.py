from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadData
from django.conf import settings

from . import constants


def generate_eccess_token(openid):
    """
    签名openid
    :param openid: 用户的openid
    :return: access_token
    """
    serializer = Serializer(settings.SECRET_KEY, expires_in=constants.ACCESS_TOKEN_EXPIRES)
    data = {'openid': openid}
    token = serializer.dumps(data)
    return token.decode()


def check_access_token(access_token_openid):
    """
    反解、反序列化access_token_openid
    :param access_token_openid: openid密文
    :return: openid明文
    """
    # 创建序列化器对象
    s = Serializer(settings.SECRET_KEY, expires_in=constants.ACCESS_TOKEN_EXPIRES)
    # 反序列化openid密文
    try:
        data = s.loads(access_token_openid)
    except BadData:
        return None
    else:
        # 返回openid明文
        return data.get('openid')