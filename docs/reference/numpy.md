# Numpy Functions

이 문서는 Numpy 함수(, 기능)들을 정리해 놓은 문서입니다. 함수는 `import numpy as np`를 기준으로 작성되었습니다.

## 01. `np.reshape`

``` python
numpy.reshape(array, shape, order="C", *, copy=None)
ndarray.reshape(shape, order="C", *, copy=None) # 매서드 형태 (더 많이 사용한다)
```

### 기능

- 원소 값과 순서는 그대로 두고 배열의 모양(shape)만 바꾼 배열을 돌려준다.

### 매개변수

| 매개변수 | 역할 | 기본값 |
| --- | --- | --- |
| `array` | 모양을 바꿀 배열 (`np.reshape` 일 때만) | 없음 (필수)
| `shap` | 새 모양. 정수 하나 또는 튜플. 한 자리에 `-1`을 넣으면 나머지도 자동 계산 | 없음 (필수) |
| `order` | 원소를 읽고 채우는 순서 (`"C"`: 행 우선, `"F"`: 열 우선) | `"C"` |
| `copy` | `None`: 가능하면 view, 안 되면 복사 / `True`: 항상 복사 / `False`: 복사가 필요하면 에러 | `None`


### 반환값

- 새 `shpae`의 `numpy.ndarray`이다.
  - 원본은 바뀌지 않는다.(in-place 아님). 반드시 반환값을 변수에 받아야 한다.
  - 대부분 원본과 메모리를 공유하는 view이다. 그래서 반환된 배열의 값을 수정하면 원본 값도 바뀐다.

## 02. `ndarray.flatten`

``` python
ndarry.flatten(order="c")
```

기능: 다차원 배열을 1차원으로 펼친 새 배열을 만듭니다.

| 매개변수 | 역할 | 기본값 |
| --- | --- | --- |
| `order` | 펼치는 순서 | 기본값 `"C"`: 행 단위로 펼침. 첫 줄 왼쪽 $\rightarrow$ 오른쪽, 그다음 둘째 줄 순서 | 

반환값: 1차원 `numpy.ndarray`(복사본). 원본 `axes`는 바뀌지 않고 2차원 그대로

## 03. `ndarray.astype`

``` python
ndarray.astype(dtype, order="K", casting="unsafe", subok=True, copy=True)
```

### 기능

- 배열의 원소를 지정한 dtype을 바꾼 배열을 만든다.

### 매개변수

| 매개변수 | 역할 | 기본값 |
| --- | --- | --- |
| `dtype` | 바꿀 자료형 (`np.float32`, `np.int64` 등) | 없음 (필수) |
| `copy` | `True`면 항상 새 배열을 만듦. `False`면 dtype이 이미 같을 때 원본을 그대로 반환 | `True` |
| `casting` | 변환을 얼마나 허용할지(`"unsafe"`는 정보가 손실되는 변환도 허용) | `"unsafe"` |

### 반환값

- 지정한 dtype의 `numpy.ndarray`이다. 기본값(`copy=True`)이면 새 배열이고, 원본은 바뀌지 않는다(in-place 아님).