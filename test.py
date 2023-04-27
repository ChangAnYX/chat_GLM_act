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

    try:
        while True:
            inpQ = await websocket.receive_text()
            if inpQ == "clear":
                socket.history = []
                await socket.send_personal_message(f"清理聊天记录成功", websocket)
            else:
                result = application.get_knowledge_based_answer(inpQ, socket.history)
                socket.history.append((inpQ, result))
                await socket.send_personal_message(f"答复: {result}", websocket)

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
