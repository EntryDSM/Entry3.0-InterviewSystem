NEW_POST = {
    'tags': ['Admin'],
    'description': '새 질문 생성',
    'parameters': [
        {
            'name': 'access_token',
            'description': '엑세스 토큰, 헤더의 Authentication',
            'in': ' header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'body',
            'description': '본문',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'form',
            'description': '평가항목',
            'in': 'json',
            'type': 'json',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '성공'
        }
    }
}

MAIN_GET = {
    'tags': ['Admin'],
    'description': '질문 목록 불러오기',
    'parameters': [
        {
            'name': 'access_token',
            'description': '엑세스 토큰, 헤더의 Authentication',
            'in': ' header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': [
                {
                    "form": {
                            "1": "subject name"
                        },
                    "title": "question 1",
                    "question_id": 1,
                    "body": "body"
                }
            ]
        }
    }
}

MANAGE_GET = {
    'tags': ['Admin'],
    'description': '질문 보기',
    'parameters': [
        {
            'name': 'access_token',
            'description': '엑세스 토큰, 헤더의 Authentication',
            'in': ' header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'question id',
            'description': '질문 번호',
            'in': ' path',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                "form":
                    {
                        "1": "subject name"
                    },
                "title": "question 1",
                "question_id": 1,
                "body": "body"
            }
        }
    }
}

MANAGE_PATCH = {
    'tags': ['Admin'],
    'description': '질문 수정',
    'parameters': [
        {
            'name': 'access_token',
            'description': '엑세스 토큰, 헤더의 Authentication',
            'in': ' header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'question id',
            'description': '질문 번호',
            'in': ' path',
            'type': 'int',
            'required': True
        },
        {
            'name': 'title',
            'description': '제목',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'body',
            'description': '본문',
            'in': 'json',
            'type': 'str',
            'required': False
        },
        {
            'name': 'form',
            'description': '평가항목',
            'in': 'json',
            'type': 'json',
            'required': False
        }
    ],
    'responses': {
        '200': {
            'description': '성공'
        }
    }
}

MANAGE_DELETE = {
    'tags': ['Admin'],
    'description': '질문 삭제',
    'parameters': [
        {
            'name': 'access_token',
            'description': '엑세스 토큰, 헤더의 Authentication',
            'in': ' header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'question id',
            'description': '질문 번호',
            'in': ' path',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '성공'
        },
        '403': {
            'description': '질문 검색 실패'
        }
    }
}