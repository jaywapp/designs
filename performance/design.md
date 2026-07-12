# Design Spec — Performance Hub (performance)

FC 마포 유나이티드 축구 클럽 랜딩. **다크 테크 퍼포먼스 허브** 미학의 데이터 대시보드.
출처: `performance.html`

## 샘플 화면

![Performance Hub 샘플 화면](./performance.png)

> 렌더링 원본: [`performance.html`](./performance.html)

---

## 1. 디자인 컨셉

- **테마**: 다크 모드, 스포츠 애널리틱스 대시보드 (라임 온 다크)
- **분위기**: 브로드캐스트/데이터 허브 — 격자 배경, 발광 라임, 전술 보드
- **밀도**: 고밀도 단일 화면(뷰포트 고정) 6카드 그리드
- **뷰포트**: `height:100vh` / `min-height:900px` / `body overflow:hidden` (데스크톱 대시보드)

---

## 2. 컬러 토큰

| 토큰 | 값 | 용도 |
|------|-----|------|
| `--ink` | `#07131f` | 페이지 배경 (딥 다크) |
| `--panel` | `#0c1d2d` | 패널 배경 |
| `--panel2` | `#10283a` | 보조 패널 |
| `--line` | `#244054` | 경계선 |
| `--green` | `#9dff3a` | 주 액센트 (발광 라임) |
| `--grass` | `#1f9d58` | 잔디 그린 (그라디언트·필드) |
| `--white` | `#f6fbff` | 기본 텍스트 |
| `--muted` | `#91a9b8` | 보조 텍스트 |
| `--orange` | `#ffb45b` | 보조 강조 (정의됨) |

- 배경: 라디얼 글로우 + `115deg` 다크 그라디언트 + **40px 격자 오버레이**(`shell:before`)
- 발광: 라임 상태 점 `box-shadow:0 0 10px`

---

## 3. 타이포그래피

- **폰트**: `Inter,Pretendard,"Noto Sans KR",Arial,sans-serif` / 전역 `letter-spacing:-.02em`
- **H1**: `35px` / `font-weight:950` / `letter-spacing:-.055em` (강조어는 muted 650)
- **수치**: stat `950 35px`, 스코어 `950 40px`, 출석 `950 43px` — 데이터 강조
- **라벨/eyebrow**: `900`, 넓은 자간(`.14~.18em`), 대문자
- 얇은 각진 코너(`border-radius:4~7px`) — 소프트하지 않은 테크 톤

---

## 4. 레이아웃 구조

### 셸 (`.shell`)
- 라디얼 글로우 + 격자 배경, 뷰포트 고정

### 골격
- `header`(82px): 육각 크레스트+브랜드 / 중앙 네비(활성 라임 언더라인) / MATCH WEEK 상태·로그인
- `main`: `topline`(85px, eyebrow+H1 + 우측 액션 버튼) → **6카드 그리드**

### 카드 그리드 (`.grid`)
```
grid-template-columns: 1.05fr 1.55fr 0.9fr
grid-template-rows:    205px 1fr
```
- 상단행: match / pulse(시즌 스탯) / result
- 하단행: timeline(경기 일정) / **tactics(전술 필드)** / attendance(참석)

---

## 5. 컴포넌트

### 육각 크레스트 (`.crest`)
- `clip-path` 육각형(방패), 라임 배경 네이비 텍스트 "FMU"

### 시즌 펄스 (`.pulse .stats`)
- 4스탯(경기/승/득점/출석률), 각 값 아래 진행 바(라임 채움 %), 세로 구분선

### 전술 보드 (`.tactics .pitch`)
- CSS 축구장: 센터라인·센터서클(`:before/:after`), 좌우 페널티 박스(`.box`)
- 4-2-3 포메이션 9명 배치(`.p1~.p9` 절대좌표), 원형 dot(골키퍼=라임), 이름 라벨
- 하단 배경 거대 숫자 "19" 워터마크

### 타임라인 (`.fixture`)
- `47px 1fr auto`: 날짜(일/월) / 상대·시간·장소 / 태그(FRIENDLY/LEAGUE)
- 하단 고정 라임 CTA(`.apply`) — 모집 안내

### 참석 (`.attendance`)
- 대형 응답 수치 + capacity 바(잔디→라임 그라디언트)
- roles 2×2(GK/DF/MF/FW), 매치 브리핑 공지, 하단 고정 3버튼 응답(참석=라임)

---

## 6. 반응형

- `@media(max-width:1000px)`:
  - `body overflow:auto`, shell 높이 해제(세로 스택)
  - 네비 숨김, 그리드 1열(카드 min-height 지정), tactics 480px 등

---

## 7. 재현 체크리스트

- [ ] 딥 다크 배경 + 라디얼 글로우 + 40px 격자 오버레이
- [ ] 발광 라임(`#9dff3a`) 단일 액센트, 얇은 각진 코너
- [ ] 육각 clip-path 크레스트
- [ ] 뷰포트 고정 6카드 그리드(205px/1fr 2행)
- [ ] 시즌 스탯 4열 + 진행 바
- [ ] CSS 전술 필드(센터서클·페널티박스·4-2-3 배치·워터마크 숫자)
- [ ] 참석 capacity 바 + roles 2×2 + 고정 응답 버튼
