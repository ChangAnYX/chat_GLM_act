from transformers import AutoModel, AutoTokenizer


class ChatGLMService:
    max_token: int = 100000
    temperature: float = 0.1
    top_p = 0.9
    tokenizer: object = None
    model: object = None

    def __init__(self):
        super().__init__()

    def load_model(self,
                   model_name_or_path: str = "/app/THUDM/chatglm-6b"):
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path,
            trust_remote_code=True
        )
        self.model = AutoModel.from_pretrained(model_name_or_path, trust_remote_code=True).half().cuda()
        self.model = self.model.eval()

    def getQA(self, prompt: str, history: list):
        response, _ = self.model.chat(
            self.tokenizer,
            prompt,
            history=history,
            max_length=self.max_token,
            temperature=self.temperature,
        )
        print(response)
        return response
