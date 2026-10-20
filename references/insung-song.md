# INSUNG SONG — 송인성

## Metadata
- URL: https://insungsong.com/kr/
- Collected At: 2026-10-20
- Last Reviewed: 2026-10-20
- Category: Landing Page, Personal Branding, Consulting
- Tags: SEO, B2B, Personal Branding, Case Study, Content Marketing, Conversion
- Focus: 전체 디자인 및 UX
- Analysis Status: 텍스트/문서 구조 확인 완료; 실제 렌더링 시각 요소와 인터랙션 일부 미확인

## 1. Overview
SEO·AI 검색 컨설턴트 송인성의 한국어 개인 브랜딩 및 서비스 소개 사이트. 주요 사용자는 SEO 컨설팅·교육·해외 검색 마케팅을 검토하는 기업 담당자다. 서비스 설명, 성과 사례, 전문가 소개, 콘텐츠, 문의로 구성된다.

## 2. Design Concept
전문가의 정체성과 검증 가능한 성과를 중심으로 신뢰를 형성하는 전환형 랜딩 페이지. 명확한 카피와 수치 기반 증거, 콘텐츠 축적을 결합한다. 구체적인 미학적 톤은 실제 화면 렌더링 미확인.

## 3. Visual Design
### Colors
정확한 색상 팔레트 및 HEX 미확인.
### Typography
H1 자기소개, H2 번호별 섹션, H3 세부 콘텐츠 제목으로 이어지는 의미적 계층 확인. 폰트명·크기·굵기 미확인.
### Spacing & Layout
서비스→사례→소개→읽을거리→문의 순서의 세로형 정보 구조 확인. 실제 여백·그리드 수치 미확인.
### Components
상단 서비스/콘텐츠 내비게이션, 언어 전환(KR/EN), CTA 링크, 서비스별 비용 표시 카드, 수치 중심 사례 링크, 고객사 로고 목록, 인터뷰·팟캐스트·블로그 목록, 뉴스레터 이메일/동의 폼, 문의 섹션, 소셜 링크 확인. 버튼 색상·테두리·그림자·이미지 비율 미확인.

## 4. Layout & Structure
### Desktop
헤더 내 서비스 메뉴, 사례·소개·블로그·팟캐스트·무료 도구·문의, 언어 전환이 제공된다. 히어로에는 자기소개와 인물 사진 및 문의 CTA가 있다. 본문은 1~5번 차례와 제공 서비스, 숫자로 본 사례, 어떤 사람인지, 읽을거리, 문의 섹션으로 구성된다. 정확한 열 배치 미확인.
### Mobile
원문에 중복된 내비게이션 구조가 있으나 실제 모바일 메뉴의 노출 및 동작은 미확인. 반응형 레이아웃 검증 필요.

## 5. UX & Interaction
- 상단 내비게이션과 섹션 차례를 통해 주요 정보 접근 경로를 제공한다.
- 히어로의 문의하기/제가 하는 일 보기 CTA가 전환과 탐색을 분리한다.
- 서비스 카드에서 설명과 비용을 함께 제공하여 초기 의사결정 부담을 줄인다.
- 성과 사례는 변화 수치, 측정 기간, 데이터 출처를 함께 제시하여 신뢰를 보강한다.
- 뉴스레터 구독에는 이메일 입력 및 마케팅 정보 수신 동의가 있다.
- 실제 클릭·호버·애니메이션·폼 제출 성공 상태는 테스트하지 않았으므로 미확인.

## 6. Reusable Design Patterns
### 1. 인물 중심 신뢰형 Hero
- 특징: 실명, 전문 영역, 경력, 인물 사진, 직접 문의 CTA.
- 해결 문제: 서비스 제공자의 신뢰성과 정체성 파악.
- 적용: 전문가 포트폴리오, B2B 컨설팅, 전문 서비스.
- 구현: HeroProfile, PrimaryCTA, SecondaryCTA 분리; 이미지 대체 텍스트와 명확한 제목 계층.

### 2. 비용 공개형 서비스 카드
- 특징: 서비스 범위·간략 설명·가격/견적 기준·상세 링크.
- 해결 문제: 서비스별 차이와 예산 적합성 판단.
- 적용: 컨설팅 상품, 교육 프로그램, 패키지 서비스.
- 구현: ServiceCard 데이터 모델에 title, summary, pricingNote, href; 가격과 VAT 표기 명료화.

### 3. 근거 중심 성과 사례
- 특징: 전후 지표, 측정 기간, 출처와 상세 링크.
- 해결 문제: 과장된 마케팅 메시지에 대한 불신.
- 적용: 에이전시, SaaS 고객 사례, 컨설팅 포트폴리오.
- 구현: MetricCaseStudy에 before, after, unit, period, source, caveat; 측정치와 추정치 구분.

### 4. 전문 콘텐츠 허브
- 특징: 인터뷰, 팟캐스트, 블로그, 뉴스레터를 소개 이후 배치.
- 해결 문제: 구매 전 전문성 검증과 장기 관계 형성.
- 적용: 전문가 브랜드, B2B 리드 생성.
- 구현: ContentFeed에 type, title, date, duration, href; 접근 가능한 링크 텍스트.

### 5. 단계형 랜딩 페이지 차례
- 특징: 번호와 섹션 이름을 연결한 정보 탐색.
- 해결 문제: 긴 페이지에서 위치와 구조 파악의 어려움.
- 적용: 장문 랜딩 페이지, 회사 소개, 포트폴리오.
- 구현: SectionNav와 section id 매핑, 스크롤 이동 시 헤더 오프셋 고려.

## 7. Implementation Hints
- 컴포넌트: HeaderNav, HeroProfile, SectionNav, ServiceGrid, CaseStudyList, ClientLogoStrip, AboutPreview, ContentFeed, NewsletterForm, ContactCTA, Footer.
- 구조: 시맨틱 header/nav/main/section/footer 및 일관된 max-width 컨테이너 권장.
- 반응형: 작은 화면에서 카드와 콘텐츠 목록을 단일 열로 전환하는 방식 검토(제안, 실제 사이트 구현 확인 아님).
- 디자인 토큰: --color-bg, --color-text, --color-accent, --space-section, --radius-card 등을 프로젝트 상황에 맞게 정의(원본 추출값 아님).
- 접근성: 메뉴 키보드 조작, 링크 포커스 표시, 폼 label/동의 안내, 성과 지표의 출처 텍스트 유지.
- 기술 스택은 미확인.

## 8. Strengths & Limitations
**강점:** 서비스 및 가격의 명확성, 성과 수치와 근거, 풍부한 전문 콘텐츠, 다수의 문의 진입점.
**제한:** 실제 컬러·폰트·간격·모바일·마이크로 인터랙션 미검증. 뉴스레터 폼의 실제 제출 흐름 미검증.

## 9. Reference Summary
전문가의 얼굴과 경력으로 관심을 만들고, 상품 정보와 정량 사례로 구매 불확실성을 줄인 뒤, 콘텐츠로 전문성을 보강하고 문의로 연결하는 랜딩 페이지 구조가 핵심 재사용 포인트다.

## 10. Sources & Verification Notes
- 원본: https://insungsong.com/kr/ (2026-10-20 접근)
- 확인 범위: 공개 HTML에서 추출된 본문, 링크, 이미지 대체 텍스트, 폼 구조.
- 직접 브라우저 렌더링 및 클릭 테스트를 수행하지 않아 정확한 색상·폰트·그리드·애니메이션·모바일 동작은 확인하지 않았다.
