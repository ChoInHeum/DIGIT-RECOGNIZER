# Matplotlib Functions

이 문서는 matplotlib 함수(, 기능)들을 정리해 놓은 문서입니다. 함수는 `import matplotlib.pyplot as plt`를 기준으로 작성되었습니다.

## 01. `plt.imshow`

``` python
matplotlib.pyplot.imshow(X, cmap=None, ...)
```

기능: 2차원 배열의 각 값을 밝기(색)로 칠해서 이미지로 보여줍니다.

| 매개변수 | 역할 |
| --- | --- |
| `X` | 그릴 배열 | 
| `cmap` | 색 지도 |