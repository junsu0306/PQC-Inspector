# File: pqc_inspector_server/agents/base_agent.py
# 🤖 모든 전문 분석 에이전트들이 상속받을 추상 기본 클래스입니다.

from abc import ABC, abstractmethod
from typing import Dict, Any
from ..services.ollama_service import OllamaService, get_ollama_service
from ..api.schemas import AgentAnalysisResult

class BaseAgent(ABC):
    """
    모든 에이전트의 기본이 되는 추상 클래스입니다.
    모든 에이전트는 'analyze' 메소드를 반드시 구현해야 합니다.
    """
    
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.ollama_service = get_ollama_service()
        self.system_prompt = self._get_system_prompt()
    
    @abstractmethod
    def _get_system_prompt(self) -> str:
        """
        각 에이전트별 시스템 프롬프트를 반환합니다.
        """
        pass
    
    @abstractmethod
    async def analyze(self, file_content: bytes, file_name: str) -> Dict[str, Any]:
        """
        파일 내용을 분석하여 결과를 딕셔너리 형태로 반환합니다.

        Args:
            file_content (bytes): 분석할 파일의 내용입니다.
            file_name (str): 분석할 파일의 이름입니다.

        Returns:
            Dict[str, Any]: AgentAnalysisResult 스키마와 호환되는 분석 결과
        """
        pass
    
    async def _call_llm(self, prompt: str) -> Dict[str, Any]:
        """
        Ollama 모델을 호출하고 응답을 받습니다.
        """
        return await self.ollama_service.generate_response(
            model=self.model_name,
            prompt=prompt,
            system_prompt=self.system_prompt
        )
    
    def _parse_file_content(self, file_content: bytes) -> str:
        """
        바이트 파일 내용을 텍스트로 변환합니다.
        """
        try:
            return file_content.decode('utf-8')
        except UnicodeDecodeError:
            try:
                return file_content.decode('latin-1')
            except UnicodeDecodeError:
                return str(file_content)  # 바이너리 파일의 경우
