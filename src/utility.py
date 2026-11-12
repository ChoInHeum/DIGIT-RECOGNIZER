import torch

from datetime import datetime

def get_device() -> torch.device:
  if not torch.cuda.is_available():
    log(f"can't use cuda")
    return torch.device(type="cpu")

  return torch.device(type="cuda")

def log(msg, time_fmt: str = "%Y-%m-%d %H:%M:%S") -> None:
  prefix = f"[{datetime.now().strftime(time_fmt)}] "
  indent = " " * len(prefix)
  lines = str(msg).splitlines() or [""]

  text = "\n".join([prefix + lines[0]] + [indent + line for line in lines[1:]])
  print(text, flush=True)