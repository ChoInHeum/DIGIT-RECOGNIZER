# Pandas Functions

이 문서는 pandas 함수(, 기능)들을 정리해 놓은 문서입니다. 함수는 `import pandas as pd`를 기준으로 작성되었습니다.

## 01. `[row_selector, column_selector]`

``` python
DataFrame.iloc[row_selector, column_selector]
# 슬라이스 문법: start:stop:step (stop 위치는 포함하지 않음, 생략하면 처음/끝/1)
```

기능: 행과 열을 위치 번호(0부터)로 골라낸다. 라벨 이름이 아니라 몇 번째인지 고르는 방식이다. 이름으로 고르는 것은 `.lloc`이다.

| 매개변수 | 역할 | 예시(`iloc[0, 1:]`)
| --- | --- | --- |
| `row_selector` | 고를 행 위치 | `0` $\rightarrow$ 첫 번째 행 하나 |
| `column_selector` | 고를 열 위치 | `1:` $\rightarrow$ 1번 열부터 끝까지 |
| `start` (슬라이스) | 시작 위치 (포함) | `1` $\rightarrow$ `pixel0`. 0번 열인 `label`은 건너뜀 |
| `stop` (슬라이스) | 끝 위칠 (미포함) | 생략 $\rightarrow$ 마지막 열(`pixel783`)까지 |
| `step` (슬라이스) | 간격 | 생략 $\rightarrow$ `1` |


