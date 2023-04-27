from fastapi import FastAPI
from starlette.websockets import WebSocket, WebSocketDisconnect
from clc.socket_service import ConnectionManager
from langchain_application import LangChainApplication

app = FastAPI()

application = LangChainApplication()


@app.websocket("/ws/chat/GLM")
async def websocket_endpoint(websocket: WebSocket):
    socket = ConnectionManager()
    await socket.connect(websocket)
    act = None

    try:
        while True:
            data_json = await websocket.receive_json()
            print(data_json)
            if data_json["act"] != act:
                socket.history = []
                act = data_json["act"]

            if data_json["operation"] == "clear":
                socket.history = []
                await socket.send_personal_message({"code": 200, "answer": "清理聊天记录成功"}, websocket)
            else:
                result = application.get_knowledge_based_answer(data_json["question"], socket.history,
                                                                act=data_json["act"])
                socket.history.append((data_json["question"], result))
                await socket.send_personal_message({"code": 200, "answer": result}, websocket)

    except WebSocketDisconnect:
        socket.disconnect(websocket)


if __name__ == '__main__':
    import uvicorn

    # uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True)
    uvicorn.run(
        app='main:app',
        host=str("0.0.0.0"),
        port=7860
    )
