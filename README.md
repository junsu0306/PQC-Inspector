📖 PQC Inspector AI
양자내성암호(PQC) 전환을 돕기 위해 소스코드, 바이너리, 설정 파일 등에서 비양자내성암호(Non-PQC) 사용 여부를 탐지하는 AI 기반 분석 시스템입니다.

✨ 주요 기능
AI 오케스트레이터: 분석 요청된 파일의 종류를 자동으로 분류합니다.

전문 에이전트: 각 파일 유형(소스코드, 바이너리, 설정 등)에 특화된 AI 에이전트가 심층 분석을 수행합니다.

결과 저장 및 보고: 분석된 모든 결과는 데이터베이스에 저장되며, 필요시 요약 보고서를 생성할 수 있습니다.

🛠️ 시작하기
사전 준비
Python 3.9+

Docker 및 Docker Compose

Git

설치 및 실행
프로젝트 클론

git clone [https://github.com/your-username/pqc-inspector.git](https://github.com/your-username/pqc-inspector.git)
cd pqc-inspector

환경 변수 설정
.env 파일을 생성하고 아래 내용을 채워넣습니다. (프로젝트 루트에 제공된 .env 파일 예시 참고)

DATABASE_URL="postgresql://user:password@db:5432/pqc_db"
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=pqc_db
# ... 기타 모델 경로 등

Docker로 실행 (권장)
아래 명령어를 실행하면 API 서버와 데이터베이스가 함께 실행됩니다.

docker-compose up --build

이제 웹 브라우저에서 http://localhost:8000 로 접속하여 "PQC Inspector AI is running!" 메시지를 확인할 수 있습니다.

로컬에서 직접 실행 (개발 시)
가상 환경을 만들고 의존성을 설치합니다.

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 별도의 터미널에서 Docker로 DB만 실행
# docker-compose up db

# API 서버 실행
uvicorn main:app --reload

🗂️ 프로젝트 구조
(생략 - 나중에 파일 구조 설계 내용을 여기에 추가할 수 있습니다.)

🌐 API 엔드포인트
GET /: 서버 상태 확인

POST /api/v1/analyze: 파일 분석 요청 (구현 예정)

GET /api/v1/report/{report_id}: 분석 결과 보고서 조회 (구현 예정)