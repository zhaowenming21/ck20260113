import pytest

from cn.com.zkjz.chapter11.chapter1102.survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """创建一个匿名调查问卷对象"""
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)


def test_store_single_response(language_survey):
    """测试单个答案会被妥善地存储"""
    question = "What language did you first learn to speak?"

    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_responses(language_survey):
    """测试三个答案会被妥善地存储"""
    question = "What language did you first learn to speak?"

    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
