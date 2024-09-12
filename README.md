# 1. Frontend Development (前端开发)

## Key changes:
- **State management**: Replaced the `state` with `useState` hooks for `user` and `seconds`.
- **Lifecycle methods**: Replaced `componentDidMount` and `componentDidUpdate` with `useEffect`, and the `clearInterval` function replaces `componentWillUnmount`.
- **Fetching data**: Moved the `fetchUserData` function inside the `useEffect` hook, and it triggers whenever `userId` changes, mimicking the behavior of `componentDidUpdate`.



# 2. Backend Development (后端开发)

## Screenshots:
![helloworld_screenshot](https://github.com/user-attachments/assets/b6401ba3-6b08-4a8a-977d-0c1634f19858)

![Weixin Image_20240911120016](https://github.com/user-attachments/assets/4ee0db14-c8c4-47ba-8544-a710927af07f)

![Weixin Image_20240911115901](https://github.com/user-attachments/assets/87a1e6bd-042c-43d2-96fc-4d2251d4f14e)



# 3. LLM (大模型微调数据)

## JSON File Format Description

The generated JSON file is a list containing multiple question-answer pairs, where each pair has the following attributes:

```json
[
  {
    "id": "<unique_identifier>",
    "Headline": "<headline_text>",
    "Question": "<question_text>",
    "Answer": "<answer_text>"
  },
  ...
]
```

It takes 7.58 seconds to generate 123282 question-answer pairs.

## Peek first few...
![1726173475892](https://github.com/user-attachments/assets/78bd667f-ba44-4d70-a660-a057fa2cbc5e)



# 4. Web Crawler (爬虫)

The data source is from https://www.bbc.com/news
it scraps 43 pieces of news from the main page.
![1726172178391](https://github.com/user-attachments/assets/ffb51e82-d486-4e4d-bfa3-6f41fa10eb38)


