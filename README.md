# 🏃‍♂️ Sportify - 공공체육시설 API

Sportify는 전국의 공공체육시설 정보를 제공하는 API 서비스입니다. 사용자들이 주변의 공공체육시설을 쉽게 찾고, 프로그램 정보를 확인할 수 있도록 도와줍니다.

## 🌟 주요 기능

- 지역별 체육시설 정보 제공
- 프로그램 검색 및 필터링 (가격, 요일, 시간대)
- 종목별 프로그램 분류
- 실시간 프로그램 정보 업데이트

## 🛠 기술 스택

### Backend
- Python 3.11
- Django
- Django REST Framework
- MySQL (AWS RDS)

### Deployment
- Docker
- Nginx
- AWS EC2

## 📁 프로젝트 구조

```
sportify/
├── config/                 # 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── common/                 # 공통 기능
│   └── models.py
├── regions/               # 지역 관련 앱
│   ├── models.py         # Sido, Facility 모델
│   ├── serializers.py
│   └── views.py
├── categories/           # 카테고리 관련 앱
│   ├── models.py        # Category 모델
│   ├── serializers.py
│   └── views.py
├── programs/            # 프로그램 관련 앱
│   ├── models.py       # Program 모델
│   ├── serializers.py
│   ├── filters.py      # 필터링 설정
│   └── views.py
├── media/              # 미디어 파일 저장소
│   └── sido_images/    # 시도 이미지
├── staticfiles/        # 정적 파일
├── requirements.txt    # 의존성 목록
├── docker-compose.yml  # Docker 구성
├── Dockerfile         # Docker 빌드 설정
└── .env              # 환경 변수
```

## 📝 API 문서

### Programs API

#### 1. 프로그램 목록 조회
```http
GET /api/programs/
```

**Query Parameters:**
- `page`: 페이지 번호 (기본값: 1)
- `size`: 페이지 크기 (기본값: 10)
- `sido`: 시/도 이름으로 필터링
- `min_price`: 최소 가격
- `max_price`: 최대 가격
- `days`: 요일 필터링 (MON, TUE, WED, THU, FRI, SAT, SUN)
- `start_time`: 시작 시간으로 필터링 (HH:MM:SS)
- `end_time`: 종료 시간으로 필터링 (HH:MM:SS)
- `ordering`: 정렬 기준 (start_time, -start_time, progrm_prc, -progrm_prc)
- `search`: 프로그램명, 시설명 검색

**응답 예시:**
```json
{
    "count": 91,
    "next": "https://dev.hufsthon.site/api/programs/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "progrm_nm": "수영 초급반",
            "category_name": "수영",
            "facility_name": "종로스포츠센터",
            "facility_address": "서울시 종로구",
            "region": "서울특별시",
            "region_image": "https://dev.hufsthon.site/media/sido_images/seoul.png",
            "progrm_days": ["MON", "WED", "FRI"],
            "days_display": "월, 수, 금",
            "start_time": "09:00:00",
            "end_time": "10:00:00",
            "time_range": "09:00 ~ 10:00",
            "progrm_begin_de": "2024-10-01",
            "progrm_end_de": "2024-10-31",
            "progrm_prc": 50000,
            "progrm_rcrit_nmpr_co": 20,
            "progrm_trget_nm": "성인",
            "hmpg_url": "https://example.com"
        }
    ]
}
```

### Categories API

#### 1. 카테고리 목록 조회
```http
GET /api/categories/
```

**Query Parameters:**
- `parent`: 상위 카테고리 ID로 필터링
- `search`: 카테고리명 검색

### Regions API

#### 1. 시도 목록 조회
```http
GET /api/regions/sidos/
```

#### 2. 시설 목록 조회
```http
GET /api/regions/facilities/
```

**Query Parameters:**
- `sido`: 시도 ID로 필터링
- `search`: 시설명 또는 주소 검색

## 🚀 설치 및 실행 방법

1. 저장소 클론
```bash
git clone https://github.com/your-username/sportify.git
cd sportify
```

2. 환경 변수 설정 (.env 파일 생성)
```
DEBUG=True
SECRET_KEY=your-secret-key
RDS_DB_NAME=your-db-name
RDS_USERNAME=your-username
RDS_PASSWORD=your-password
RDS_HOSTNAME=your-db-host
RDS_PORT=3306
```

3. Docker 실행
```bash
docker-compose up --build
```

## 🤝 Contributing

버그 리포트나 새로운 기능 제안은 언제나 환영합니다. 이슈를 생성하거나 풀 리퀘스트를 보내주세요.

## 📜 License

This project is licensed under the MIT License - see the LICENSE.md file for details.
