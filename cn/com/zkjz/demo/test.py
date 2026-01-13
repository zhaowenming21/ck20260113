import dashscope

input_texts = "衣服的质量杠杠的，很漂亮，不枉我等了这么久啊，喜欢，以后还来这里买"
# aigccode
dashscope.api_key = 'sk-101efc3d4dfd468f8777e29bb72d8023'
resp = dashscope.TextEmbedding.call(
    model="text-embedding-v4",
    input=input_texts
)
print(resp)
