# John Jung

## Metadata
- URL: https://jungeuihyung.com/
- Collected At: 2026-10-20
- Last Reviewed: 2026-10-20
- Category: Personal Portfolio, App Showcase
- Tags: Storytelling, Playful Interaction, Character, Minimalism, App Directory
- Focus: 전체 디자인 및 UX
- Analysis Status: 텍스트 콘텐츠 직접 확인; 실제 렌더링 및 모바일 시각 검증 제한

## 1. Overview
정의형(John Jung)의 개인 웹사이트. 일본 홋카이도 마쿠베쓰에 거주하는 앱 제작자로서 창작 철학과 직접 만든 앱을 소개한다. 방문자는 제작자, 앱 사용자, 협업 관심자 등으로 해석된다.

## 2. Design Concept
간단하고 따뜻하며 일상적으로 사용하는 앱을 지향한다는 제작 철학을 서사형 자기소개와 작은 우편배달 비행기 캐릭터에 연결한다. 감성적·놀이적 인상은 텍스트 및 인터랙션 안내를 기반으로 한 해석이며 렌더링 화면 검증은 별도 필요하다.

## 3. Visual Design
### Colors
- 실제 컬러 팔레트 및 HEX: 미확인.
### Typography
- 일본어 표기 헤딩, 영어 자기소개 및 대문자 섹션명(APPS, ELSEWHERE)이 확인된다.
- 실제 폰트, 크기, 행간: 미확인.
### Spacing & Layout
- 소개 → 앱 목록 → 외부 링크 순서의 정보 구조가 확인된다.
- 픽셀 단위 여백과 그리드: 미확인.
### Components
- 번호가 붙은 앱 목록(01~10), 짧은 설명, iOS/Android 스토어 링크.
- 출시 예정 앱의 'Coming soon' 상태 표시.
- Instagram, YouTube, Threads, note, Email 연결.
- 비행기 캐릭터가 본문에서 언급됨. 정확한 이미지 형태는 미확인.

## 4. Layout & Structure
### Desktop
- 첫 부분에 이름 및 장문 자기소개, 이후 APPS와 ELSEWHERE 섹션.
- 실제 컬럼 수, 고정 요소, 헤더 형태: 미확인.
### Mobile
- 모바일 실제 화면 및 반응형 전환: 미확인.

## 5. UX & Interaction
- 주요 사용자 흐름: 제작자 소개 읽기 → 앱 선택 → 플랫폼별 스토어 이동.
- 페이지 텍스트에서 'Tap anywhere and the postman will fly to you'라고 명시한다. 실제 탭 동작은 검증하지 못했다.
- 'Tap the words'라는 안내가 있어 텍스트 상호작용을 암시하지만 구체적 반응은 미확인.
- 앱마다 플랫폼 링크를 개별 제공하여 설치 목적의 탐색을 단순화한다.
- 키보드 접근성, 모션 감소 설정, 포커스 상태는 미확인.

## 6. Reusable Design Patterns
### 1. Narrative-first Creator Portfolio
- 특징: 제품보다 제작 철학과 개인적 이야기를 먼저 소개.
- 해결 문제: 낯선 제작자와 제품 사이의 신뢰·맥락 부족.
- 적용: 인디 메이커, 크리에이터, 1인 개발자 포트폴리오.
- 고려: 소개가 길어질 때 빠른 앱 탐색 앵커 제공.

### 2. Numbered App Directory
- 특징: 일련번호 + 앱명 + 한 줄 가치 제안 + 플랫폼 링크.
- 해결 문제: 여러 제품의 비교 및 접근 경로 혼란.
- 적용: 마이크로 SaaS 모음, 실험 프로젝트 아카이브.
- 고려: 링크 접근성, 출시 상태, 플랫폼별 제공 여부 명확화.

### 3. Character-led Microinteraction
- 특징: 우편배달 비행기 캐릭터가 사용자 탭에 반응한다고 안내.
- 해결 문제: 정적인 소개 페이지의 낮은 정서적 기억성.
- 적용: 개인 브랜드, 소규모 게임, 실험적 랜딩 페이지.
- 고려: prefers-reduced-motion, 포인터/터치/키보드 대안, 성능. 실제 움직임은 미검증.

## 7. Implementation Hints
- 제안 컴포넌트: CreatorIntro, AppList, AppListItem, PlatformLinks, PostmanCharacter, SocialLinks.
- 앱 목록은 name, description, iosUrl, androidUrl, status 데이터로 분리.
- 콘텐츠 우선 시맨틱 구조: main, section, heading, ol, nav/footer.
- 캐릭터 인터랙션 구현 시 pointer 이벤트와 키보드 접근성, reduced-motion 대안 고려.
- 반응형 구성은 좁은 화면에서 링크 줄바꿈과 충분한 터치 영역 확보.
- CSS 토큰은 실제 디자인을 확인한 후 정의. 원본 기술 스택은 미확인.

## 8. Strengths & Limitations
- 강점: 제작자의 개성이 명확하고 앱 목록 및 다운로드 경로가 직관적이다. 캐릭터 인터랙션의 콘셉트가 기억에 남는다.
- 제한: 장문 소개의 스캔 효율은 실제 화면 검토가 필요하며, 시각 스타일·애니메이션·모바일 접근성은 미검증.

## 9. Reference Summary
개인적 서사, 가벼운 캐릭터 인터랙션, 번호형 제품 디렉터리를 결합한 인디 메이커 포트폴리오 사례. 복제보다 '개성 있는 이야기 + 빠른 제품 접근'의 균형을 재사용할 가치가 있다.

## 10. Sources & Verification Notes
- 원본: https://jungeuihyung.com/ (2026-10-20 접근)
- 직접 확인: 페이지 텍스트, 앱 목록 10개, 스토어 및 외부 채널 링크, 탭 인터랙션 안내.
- 미확인: 실제 렌더링, 색상 HEX, 폰트, 반응형 레이아웃, 애니메이션 실행, 내부 구현 기술.
- 관찰과 해석을 구분했으며 확인되지 않은 시각 속성을 추정으로 확정하지 않았다.
