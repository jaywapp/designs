# ARCOA NOW

## Metadata
- URL: https://now.arcoa.kr/
- Collected At: 2026-10-20
- Last Reviewed: 2026-10-20
- Category: Landing Page, Brand Hub
- Tags: Minimal, Editorial, Brand Identity, Content Navigation, Portfolio
- Focus: 전체 디자인
- Analysis Status: 부분 확인 (HTML 콘텐츠 확인, 실제 렌더링 및 상호작용 미검증)

## 1. Overview
ARCOA NOW는 아르코아(ARCOA)의 공식 허브 페이지다. 앱, 굿즈, 스토리를 한곳에 소개하며 브랜드와 콘텐츠를 탐색하려는 방문자를 대상으로 한다. 화면의 HTML 텍스트에서 브랜드 슬로건 '일상을 다정하고 명료하게', 브랜드명 '아르코아', APPS / GOODS / STORIES 구획을 확인했다.

## 2. Design Concept
브랜드 슬로건과 짧은 카테고리명을 중심으로 한 간결한 정보 설계. 차분하고 친근한 브랜드 경험을 지향하는 것으로 해석된다. 실제 화면의 시각적 분위기와 세부 스타일은 미검증이다.

## 3. Visual Design
### Colors
- 정확한 색상 및 HEX: 미확인.
### Typography
- 브랜드명이 H1, APPS / GOODS / STORIES가 H2로 표기된 HTML 구조 확인.
- 실제 폰트, 크기, 굵기 및 자간: 미확인.
### Spacing & Layout
- 여백 수치, 정렬, 그리드, 섹션 간격: 미확인.
### Components
- ARCOA 로고 이미지, 브랜드 슬로건, 카테고리 제목, 스토리 링크/이미지, 푸터 정보 확인.
- 버튼 스타일, 카드 외곽선, 그림자, 아이콘 스타일: 미확인.

## 4. Layout & Structure
### Desktop
- 콘텐츠 순서(HTML 기준): 외부 메인 사이트 링크 → 로고/슬로건/브랜드명 → APPS → GOODS → STORIES → 대표자/문의/저작권.
- 실제 데스크톱 배치와 컬럼 수는 미확인.
### Mobile
- 모바일 화면 및 반응형 동작 미확인.

## 5. UX & Interaction
- 콘텐츠 카테고리 구분을 통해 탐색 영역을 명확히 제시한다.
- 메인 사이트(arcoa.kr) 링크와 스토리 관련 콘텐츠가 존재한다.
- 클릭 후 화면, 호버, 전환 애니메이션, 스크롤 반응, 키보드 접근성은 미검증.
- JavaScript 허용 안내 문구가 HTML에 포함되어 있다.

## 6. Reusable Design Patterns
### 패턴 A: 세 갈래 브랜드 허브
- 특징: 브랜드 소개 아래 APPS / GOODS / STORIES처럼 핵심 콘텐츠를 소수의 명확한 범주로 나눈다.
- UX 문제: 여러 활동을 하는 소규모 브랜드에서 탐색 복잡도를 낮춘다.
- 적용: 1인 개발자 포트폴리오, 크리에이티브 스튜디오, 제품·콘텐츠 통합 랜딩.
- 구현 고려: 카테고리별 콘텐츠가 비어 있을 때의 상태와 모바일 탐색 우선순위를 설계한다.

### 패턴 B: 짧은 정체성 문구 + 콘텐츠 진입점
- 특징: 짧은 슬로건과 브랜드명을 먼저 제시하고 콘텐츠 카테고리로 이어간다.
- UX 문제: 처음 방문한 사용자가 사이트의 성격을 빠르게 이해하도록 돕는다.
- 적용: 브랜드 소개, 인디 메이커 소개, 소규모 서비스 허브.
- 구현 고려: H1/H2 의미론과 링크 레이블을 유지한다.

## 7. Implementation Hints
- 제안 컴포넌트: BrandHeader, CategorySection, StoryItem, SiteFooter.
- 데이터 기반 카테고리 렌더링을 사용해 신규 앱/상품/스토리 추가를 쉽게 한다.
- CSS Grid/Flexbox로 데스크톱과 모바일 레이아웃을 분기하는 것은 구현 제안이며 원본 기술 스택을 뜻하지 않는다.
- 디자인 토큰은 실제 화면 확인 후 정의한다. 임의의 색상·폰트를 원본 사양으로 기재하지 않는다.
- 링크의 포커스 표시, 대체 텍스트, 반응형 제목 계층을 확인한다.

## 8. Strengths & Limitations
- 강점(확인): 브랜드 메시지가 짧고 카테고리 구조가 단순하다.
- 한계(분석): 실제 렌더링 화면, CSS, 모바일, 인터랙션을 검증하지 못했다.

## 9. Reference Summary
브랜드 메시지와 APPS / GOODS / STORIES 세 카테고리를 중심으로 구성된 공식 허브. 소규모 브랜드의 여러 활동을 하나의 진입점으로 묶는 정보 구조를 재사용하기 좋다.

## 10. Sources & Verification Notes
- 원본: https://now.arcoa.kr/
- 확인일: 2026-10-20
- 검증 방식: 공개 웹페이지 HTML 텍스트 확인.
- 확인된 문구: '일상을 다정하고 명료하게', '아르코아', 'APPS', 'GOODS', 'STORIES', '© 2026 ARCOA ✦ Archive of Calm.'
- 실제 시각적 렌더링, 폰트, 색상, 애니메이션, 모바일 동작은 확인되지 않았으며 추정으로 채우지 않았다.
