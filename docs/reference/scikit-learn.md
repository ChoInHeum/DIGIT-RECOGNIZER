# Scikit-Learn Functions

이 문서는 scikit-learn 함수(, 기능)들을 정리해 놓은 문서입니다.

## 01. `sklearn.model_selection.train_test_split`

``` python
train_test_split(*array, test_size=None, train_size=None, random_stat=None, shuffle=True, stratify=None)
```

### 기능

- 여러 배열을 같은 행 순서로 섞은 뒤, 각각 학습용과 검증용으로 나눈다.

### 매개변수

| 매개변수 | 역할 | 기본값 |
| --- | --- | --- |
| `*array` | 나눌 배열들. 첫 번째 축(행) 길이가 모두 같아야 함 | 없음 (필수) |
| `test_size` | 검증용 비율(0~1) 또는 개수 | `None` (`train_size`도 `None`이면 `0.25`) |
| `random_state` | 섞는 방식을 고정하는 시드 | `None` (실행할 때마다 다르게 나뉨) |
| `shuffle` | 나누기 전에 섞을지 | `True` |
| `stratify` | 이 병ㄹ의 클래스 비율을 양쪽에 똑같이 유지 | `None` |

### 반환값

- `list`이다. 입력 배열 하나마다 `(학습용, 검증용)` 쌍이 입력 순서대로 이어진다. 
  - 입력이 2개면 `[images_train, images_valid, labels_train, labels_valid]` 순서로 4개를 반환한다.
- 타입은 입력과 동일