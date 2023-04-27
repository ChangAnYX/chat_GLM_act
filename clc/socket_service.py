from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        # 存放激活的ws连接对象
        self.active_connections: List[WebSocket] = []
        self.history = []

    async def connect(self, ws: WebSocket):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove(ws)

    @staticmethod
    async def send_personal_message(message, ws: WebSocket):
        # 发送个人消息
        mType = type(message)  # 判断数据类型
        if mType == str:
            await ws.send_text(message)
        elif mType == dict:
            await ws.send_json(message)
        elif mType == bytes:
            await ws.send_bytes(message)
        else:
            await ws.send_text(str(message))

    # async def broadcast(self, message):
    #     # 广播消息
    #     for connection in self.active_connections:
    #         mType = type(message)  # 判断数据类型
    #         if mType == str:
    #             await connection.send_text(message)
    #         elif mType == dict:
    #             await connection.send_json(message)
    #         elif mType == bytes:
    #             await connection.send_bytes(message)
    #         else:
    #             await connection.send_text(str(message))
            # await connection.send_text(message)

# manager = ConnectionManager()
#
#
# @app.websocket("/ws/{user}")
# async def websocket_endpoint(websocket: WebSocket, user: str):
#
#     await manager.connect(websocket)
#
#     await manager.broadcast(f"用户{user}进入聊天室")
#
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await manager.send_personal_message(f"你说了: {data}", websocket)
#             await manager.broadcast(f"用户:{user} 说: {data}")
#
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         await manager.broadcast(f"用户-{user}-离开")
#
