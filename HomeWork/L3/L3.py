

responses_new = [
    [200, 201],
    [300, 301, 302],
    [400, 401, 402]
]

responses_new_2 = []

try:
    # 先提取第一個元素
    for responses in responses_new:
        responses_new_2.append(responses[0])

    # 然後提取第二個元素
    for responses in responses_new:
        if len(responses) > 1:  # 確保有第二個元素
            responses_new_2.append(responses[1])

    # 最後提取第三個元素
    for responses in responses_new:
        if len(responses) > 2:  # 確保有第三個元素
            responses_new_2.append(responses[2])

except Exception as e:
    print(f"An error occurred: {e}")

print(responses_new_2)