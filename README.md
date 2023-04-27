# chat_GLM_act
利用prompt，让chatGLM进行模拟各种人物与用户对话。

#### 用websocket连接
##### 提问
{
operation: quiz/clear  #问答操作抑或清空历史上下文
act: dog/monk/xun    #模拟人物
question: ""  #问题
}

##### 答复
{
"code": 200, 
"answer": ""/"清理聊天记录成功"
}

利用prompt对原chatGLM模型进行提示
![图片](https://user-images.githubusercontent.com/126737340/234813238-9fd4732e-3371-4acd-8b02-6d5f5248188c.png)
