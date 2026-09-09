# 성능 및 안정성 작업

orchestrator: Codex

| 작업 | owner | model | effort | depends_on | parallel_group | files | verification | status |
|---|---|---|---|---|---|---|---|---|
| 분석 및 설계 | Codex | gpt-6-astra | high | 없음 | misc | docs/runtime-hardening-* | 코드 확인 | completed |
| 구현 및 회귀 테스트 | Codex | gpt-6-astra | high | 분석 및 설계 | misc | scripts/generate_index.py, tests | 저장소 단위 테스트 | in_progress |

같은 파일에 대한 구현과 검증은 순차 수행한다. 저장소 간 작업은 상위 세션의 다른 Codex 작업과 병렬이다.


## 검증 결과 (2026-09-09)
- 폴더 목록을 한 번 읽어 HTML과 이미지 검색에 재사용하고 메타데이터 읽기 실패를 기본 제목 및 경고로 처리한다.
- python -m unittest discover -s tests -v: 4개 통과. 실제 사이트 생성·배포는 실행하지 않았다.
