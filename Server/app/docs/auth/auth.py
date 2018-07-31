AUTH = {
    'tags': ['Auth'],
    'description': '인증',
    'parameters': [
        {
            'name': 'email',
            'description': '이메일 주소',
            'in': ' json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'password',
            'description': '암호',
            'in': ' json',
            'type': 'str',
            'required': True
        }
        
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                "access_token": "<token>",
                "refresh_token": "<token>"
            }
        },
        '401': {
            'description': "실패"
        }
    }
}

REFRESH = {
    'tags': ['Auth'],
    'description': '재발급',
    'parameters': [
        {
            'name': 'refresh_token',
            'description': '리프레시 토큰',
            'in': ' header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                "access_token": "<access token>"
            }
        },
        '403': {
            'description': "실패"
        }
    }
}

LOGOUT = {
    'tags': ['Auth'],
    'description': '로그아웃',
    'parameters': [
        {
            'name': 'refresh_token',
            'description': '리프레시 토큰',
            'in': ' header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '성공',
        },
        '403': {
            'description': "실패"
        }
    }
}