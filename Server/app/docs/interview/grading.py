GRADING_POST = {
    'tags': ['Interview'],
    'description': '면접 결과 제출',
    'parameters': [
        {
            'name': 'access_token',
            'description': '엑세스 토큰, 헤더의 Authentication',
            'in': ' header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'exam code',
            'description': '수험번호',
            'in': ' path',
            'type': 'int',
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
            'name': 'take_interview',
            'description': '면접 참가 여부',
            'in': 'json',
            'type': 'bool',
            'required': True
        },
        {
            'name': 'grading',
            'description': '채점 결과',
            'in': 'json',
            'type': 'json',
            'required': True
        },
        {
            'name': 'comment',
            'description': '메모',
            'in': 'json',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '200': {
            'description': '성공'
        },
        '400': {
            'description': '실패'
        }
    }
}

GRADING_GET = {
    'tags': ['Interview'],
    'description': '면접 결과 제출',
    'parameters': [
        {
            'name': 'access_token',
            'description': '엑세스 토큰, 헤더의 Authentication',
            'in': ' header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'exam code',
            'description': '수험번호',
            'in': ' path',
            'type': 'int',
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
        },
        '403': {
            'description': '실패'
        }
    }
}