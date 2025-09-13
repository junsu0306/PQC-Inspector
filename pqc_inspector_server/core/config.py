# File: pqc_inspector_server/core/config.py
# ⚙️ .env 파일로부터 환경 변수를 로드하고 관리하는 설정 파일입니다.
# Pydantic의 BaseSettings를 사용하여 타입 검증과 기본값 설정을 쉽게 처리합니다.

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    애플리케이션의 설정을 정의하는 클래스입니다.
    .env 파일이나 환경 변수로부터 값을 자동으로 읽어옵니다.
    """
    # .env 파일 경로를 명시적으로 지정합니다.
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8', extra='ignore')

    # --- 프로젝트 설정 ---
    PROJECT_NAME: str = "PQC Inspector"
    API_V1_STR: str = "/api/v1"
    SERVER_HOST: str = "127.0.0.1"
    SERVER_PORT: int = 8000

    # --- 외부 API 설정 ---
    EXTERNAL_API_BASE_URL: str = "https://jsonplaceholder.typicode.com"  # 테스트용 API
    EXTERNAL_API_KEY: str = "test-api-key"
    EXTERNAL_API_TIMEOUT: int = 30

    # --- 애플리케이션 설정 ---
    LOG_LEVEL: str = "INFO"

    # --- Ollama 모델 설정 ---
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    ORCHESTRATOR_MODEL: str = "gemma:7b"
    SOURCE_CODE_MODEL: str = "codellama:7b"
    BINARY_MODEL: str = "codellama:7b"
    PARAMETER_MODEL: str = "gemma:7b"
    LOG_CONF_MODEL: str = "gemma:7b"

# @lru_cache 데코레이터를 사용하여 Settings 객체를 한 번만 생성하도록 캐싱합니다.
# 이렇게 하면 애플리케이션 전체에서 동일한 설정 객체를 공유하게 됩니다.
@lru_cache()
def get_settings():
    return Settings()

# 설정 객체 인스턴스를 생성하여 다른 파일에서 쉽게 임포트하여 사용할 수 있도록 합니다.
settings = get_settings()
