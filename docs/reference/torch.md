# PyTorch Functions

이 문서는 pytorch 함수(, 기능)들을 정리해 놓은 문서입니다. 함수는 `import torch`를 기준으로 작성되었습니다.

## 01. `torch.tensor`

``` python
torch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)
```

### 기능

- 리스트, numpy 배열, 숫자 등에서 데이터를 복사해 새 텐서를 만든다.

### 매개변수

| 매개변수 | 역할 | 기본값 |
| --- | --- | --- |
| `data` | 원본 데이터 (리스트, 튜플, numpy 배열, 스칼라) | 없음 (필수) |
| `dtype` | 텐서의 자료형 | `None` (원본에서 추론. numpy면 원본 dtype 유지, 파이썬 float 리스트면 `float32`)
| `device` | 텐서를 만들 위치 | `None` (CPU) |
| `requires_grad` | 이 텐서에 대한 기울기를 추적 할지 | `False` |
| `pin_memory` | GPU로 빠르게 옮기기 위한 고정 메모리 사용 여부 | `False` |

### 반환값

- 새 `torch.Tensor`이다. 항상 데이터를 복사하므로 원본 numpy 배열과 메모리를 공유하지 않는다. 원본을 바꿔도 텐서는 바뀌지 않고, 그 반대도 마찬가지이다.