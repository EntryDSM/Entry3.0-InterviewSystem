STUDY_PLAN = {
    'tags': ['Interview'],
    'description': '검색',
    'parameters': [
        {
            'name': 'access_token',
            'description': '엑세스 토큰, 헤더의 Authentication',
            'in': ' header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'exam_code',
            'description': '수험번호',
            'in': ' path',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': [
                {
                    "question_list": [
                        [
                            "question 1",
                            8
                        ]
                ],
                    "student_info": {
                        "name": "a",
                        "admission_type": "AdmissionEnum.NORMAL",
                        "img_path": "a",
                        "school": "CMD"
                    }
                }
            ]
        }
    }
}
