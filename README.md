# designs

UI 디자인 시안 모음. 각 디자인은 **샘플 HTML + `design.md` 스펙 + PNG 미리보기** 한 세트로 자족적으로 구성됩니다.

## Sample Project — UE5 개발 관제 대시보드

동일한 콘텐츠(빌드 파이프라인 · 체인지리스트 · 서비스 상태)를 세 가지 컨셉으로 시각화한 시안입니다.

| 디자인 | 컨셉 | 테마 | 미리보기 |
|--------|------|------|----------|
| [mission-control](./mission-control/) | Mission Control — 우주 관제소 | 다크 네이비-틸 / 산세리프 | ![](./mission-control/option-a.png) |
| [production-brief](./production-brief/) | Production Brief — 에디토리얼 브리프 | 라이트 페이퍼 / Georgia 세리프 | ![](./production-brief/option-b.png) |
| [build-console](./build-console/) | Build Console — CI 터미널 콘솔 | 다크 / 라임·앰버 모노스페이스 | ![](./build-console/option-c.png) |

각 폴더의 `design.md`에 컬러 토큰, 타이포그래피, 레이아웃, 컴포넌트, 반응형, 재현 체크리스트가 정리되어 있습니다.

## 폴더 구조

```
designs/
├── mission-control/    # 샘플 HTML + design.md + PNG
├── production-brief/
└── build-console/
```
