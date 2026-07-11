# Design Spec — Mission Control (Option A)

UE5 개발 관제 대시보드. **우주 관제소(mission control)** 미학의 다크 틸 테마.
출처: `option-a.html`

## 샘플 화면

![Mission Control 샘플 화면](./option-a.png)

> 렌더링 원본: [`option-a.html`](./option-a.html)

---

## 1. 디자인 컨셉

- **테마**: 다크 모드, 네이비-틸 계열 관제 대시보드
- **분위기**: 항공/우주 관제소 콘솔 — 상단 라디얼 글로우, 발광 상태 인디케이터
- **밀도**: 고밀도 (좌측 레일 + 메인 + 우측 알림 사이드바 3분할)
- **최소 높이**: `800px`, `overflow:hidden` (데스크톱 전용)
- **인터랙션**: 실제 네비 클릭 시 active 토글 (하단 `<script>`)

---

## 2. 컬러 토큰

| 토큰 | 값 | 용도 |
|------|-----|------|
| `--bg` | `#061019` | 페이지 배경 (딥 네이비) |
| `--panel` | `#0a1822` | 패널 배경 |
| `--panel2` | `#0d202b` | 보조 패널 |
| `--line` | `#183642` | 경계선 |
| `--muted` | `#6f8992` | 보조 텍스트 |
| `--text` | `#d9e8e8` | 기본 텍스트 |
| `--teal` | `#22d3b6` | 주 액센트 (활성·강조) |
| `--cyan` | `#49b9d6` | 링크성 ID (CL 번호) |
| `--amber` | `#f2b84b` | 경고 / 진행 중 |
| `--red` | `#ef6b73` | P0 알림 / 에러 |
| `--green` | `#50d890` | 정상 / 상승 지표 |

- 배경에 라디얼 글로우: `radial-gradient(circle at 45% -20%,#12303b,transparent 35%)`
- 발광 효과: teal/green 상태 점에 `box-shadow` glow

---

## 3. 타이포그래피

- **본문 폰트**: `"Segoe UI","Noto Sans KR",sans-serif` — **산세리프** 기본, 13px
- **수치 폰트**: `Consolas,monospace` (KPI 값, CL 번호, 메타 등)
- **혼용 규칙**: UI 라벨=산세리프, 데이터·코드성 값=모노스페이스
- **주요 사이즈**
  - 브랜드 H1: `16px` / `letter-spacing:.08em`
  - KPI 값: `28px` / `700` / Consolas
  - 섹션 헤드: `11px` / 대문자 / `letter-spacing:.18em`
  - 알림/서비스 본문: `9~11px`

---

## 4. 레이아웃 구조

### 앱 골격 (3열 × 3행 그리드)
```
grid-template-columns: 76px minmax(0,1fr) 310px   (레일 | 메인 | 사이드)
grid-template-rows:    72px 1fr 34px               (탑바 | 본문 | 푸터)
```

- **좌측 레일** (`76px`, 세로 전체): 로고 `SP` + 아이콘 네비(대시보드/빌드/P4/WorkHub/서비스) + 하단 설정·아바타. active 항목은 발광 좌측 마커.
- **탑바** (`72px`): 브랜드마크(이중 테두리) + 프로젝트명 + 우측 메타(CL·엔진 버전·ALPHA D-38 배지)
- **메인** (스크롤): 섹션 헤드 → KPI 4열 → 파이프라인 → 2열 카드 그리드
- **우측 사이드바** (`310px`): ACTIVE ALERTS + SERVICE STATUS
- **푸터** (`34px`): 라이브 텔레메트리 상태

---

## 5. 컴포넌트

### KPI 카드 (`.kpi` × 4)
- `repeat(4,1fr)` 그리드
- 그라디언트 배경 `linear-gradient(145deg,#0c1c26,#091720)`
- 우상단 짧은 teal 라인 액센트(`:after`)
- 라벨 → 값(28px) → 서브. 값 색: `.up`=그린, `.warn`=앰버

### 파이프라인 스텝 (`.steps` × 5)
- 5단계 가로 노드(Sync/Compile/Cook/Package/Smoke Test)
- 노드 뒤 연결선(`.steps:before`)
- 원형 dot: `.done`=teal 채움+✓, `.active`=amber 테두리+글로우+진행바
- 각 스텝: 상태 dot → 이름 → 소요시간

### 카드 그리드 (`.grid2`, 1.25 : 0.75)
- **좌**: 최근 제출(Perforce) 커밋 리스트 — CL(cyan) / 설명·작성자 / 태그
- **우**: 빌드 처리량 막대 차트 — `data-v` 라벨, 요일 축, 범례

### 알림 (`.alert`)
- 좌측 컬러 바로 심각도 구분: red(P0) / amber(P1) / teal(INFO)
- 헤드(제목+시각) → 본문 → 링크

### 서비스 상태 (`.service`)
- 서비스명 + 발광 상태 점(green/`warn` amber) + 세부(지연·에이전트 수)

---

## 6. 반응형

- `@media(max-width:1100px)`:
  - 레일 `76px → 64px`, 사이드바(`aside`) 숨김
  - KPI 4열 → 2열, 카드 그리드 1열
  - 탑바 메타 일부 숨김

---

## 7. 재현 체크리스트

- [ ] 딥 네이비 배경 + 상단 라디얼 글로우
- [ ] teal 단일 액센트, cyan=ID, green/amber/red=상태
- [ ] 산세리프 UI + 모노스페이스 데이터 혼용
- [ ] 3분할(레일·메인·알림 사이드) 그리드
- [ ] KPI 4열 + 5단계 파이프라인(글로우 active 노드)
- [ ] 커밋 리스트 + 막대 차트 2열
- [ ] 심각도 컬러 바 알림 + 발광 서비스 점
- [ ] 네비 클릭 active 토글 동작
