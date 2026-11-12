# # MNIST Digit Recognizer with PyTorch (MLP $\cdot$ CNN $\cdot$ RNN)

## Git Commit Convention

[Conventional Commits](https://www.conventionalcommits.org/) 형식을 따르고, 커밋 메시지는 영어로 쓴다. 메시지는 제목 한 줄만 쓰고 body와 footer는 쓰지 않는다.

### 원형

```text
<type>(<scope>): <subject>
```

| 항목 | 필수 | 규칙 |
| --- | --- | --- |
| `type` | O | 변경의 종류. 아래 type 표에서 하나를 고른다 |
| `scope` | X | 변경된 영역. 아래 scope 표에서 고르고, 해당 없으면 생략한다 |
| `subject` | O | 무엇을 했는지 한 줄 요약. 영어 명령형 현재 시제(`add`, `fix`), 소문자로 시작, 끝에 마침표 없음, 50자 이내 |

### type

| type | 언제 쓰는가 | 예시 |
| --- | --- | --- |
| `feat` | 새 기능 추가 (함수, 모델, 학습·추론 코드) | `feat(model): add MLP classifier` |
| `fix` | 버그 수정 | `fix(preprocessing): pass dtype as keyword to torch.tensor` |
| `docs` | 문서만 변경 (README, `docs/`) | `docs(reference): add torch.tensor notes` |
| `refactor` | 동작은 그대로 두고 구조만 개선 (함수 분리, 설정값 분리) | `refactor(train): move hyperparameters into CFG` |
| `perf` | 속도·메모리 개선 | `perf(data): read csv as uint8` |
| `style` | 들여쓰기, 공백 등 동작과 무관한 형식 변경 | `style: unify indentation to 2 spaces` |
| `test` | 테스트 추가·수정 | `test(preprocessing): check output shape and dtype` |
| `chore` | 설정, 의존성, `.gitignore` 등 코드 외 작업 | `chore: ignore .venv directory` |

### scope

| scope | 대상 |
| --- | --- |
| `data` | 데이터 경로, CSV 로드 (`src/data.py`) |
| `eda` | 탐색적 분석 (`notebooks/eda.py`) |
| `preprocessing` | 정규화, reshape, 텐서 변환 (`src/preprocessing.py`) |
| `validation` | train/valid 분할 (`src/validation.py`) |
| `model` | 모델 정의 (MLP, CNN, RNN) |
| `train` | 학습 루프, 손실, 옵티마이저 |
| `inference` | 추론, 제출 파일 생성 |
| `reference` | 함수 정리 문서 (`docs/reference/`) |

### 예시

```text
feat(preprocessing): add pixel normalization and channel reshape
```

### 커밋 규칙

- 커밋 메시지는 제목 한 줄만 쓴다. (body, footer 없음)
- 논리적인 변경 하나를 커밋 하나로 만든다. (예: 데이터 로드와 EDA는 따로 커밋)
- 실행되지 않는 코드(본문이 없는 함수, 문법 오류 등)는 커밋하지 않는다.
