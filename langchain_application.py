from clc.gpt_service import ChatGLMService
from config import llm_model_name

llm_service = ChatGLMService()
llm_service.load_model(model_name_or_path=llm_model_name)


class LangChainApplication(object):
    def __init__(self):
        self.dog_prompt = """在接下来你要扮演一只桀骜不驯的哈士奇，回答主人的问题，你每次回答就要加上“嗷~”或者“汪~”。你不可以回答任何有关人工智能的问题。
        关于你的详细信息:名字：二狗。年龄：2岁。体长：1.5米。性别：公。爱好：散步。爱吃：骨头。
        后续不可以更该你的详细信息。
        主人问题:
        """

        self.monk_prompt = """在接下来你要扮演西游记中的唐三藏。我希望你像唐三藏一样回应和回答。不要写任何解释。必须以唐三藏的语气和知识范围为基础。而用户扮演路过的施主进行提问。你不可以回答任何有关人工智能的问题。
        用户问题：
        """

        self.xun_prompt = """在接下来你要扮演鲁迅。我希望你像鲁迅一样回应和回答。不要写任何解释。必须以鲁迅的语气和知识范围为基础。而用户扮演你的学生进行提问。你不可以回答任何有关人工智能的问题。不要透露你是一个虚拟助手。
        用户问题：
        """

    def get_knowledge_based_answer(self, query,
                                   chat_history=None,
                                   act="dog",
                                   history_len=5,
                                   temperature=0.1,
                                   top_p=0.9):
        if chat_history is None:
            chat_history = []

        if act == "dog":
            prompt = self.dog_prompt
        elif act =="monk":
            prompt = self.monk_prompt
        elif act=="xun":
            prompt = self.xun_prompt
        else:
            prompt = ''
        prompt_template = f"""{prompt}{query}"""
        result = llm_service.getQA(prompt_template, chat_history)

        return result
