import subprocess
import sys

# flex получает на вход sys.argv[1] и генерирует sys.argv[2].

inp = "input.l"
outp = "output.c"

if "-h" in sys.argv:
  print("usage: python3 run.py inp_file outp_file")
  sys.exit(0)

if len(sys.argv) > 2:
  inp = sys.argv[1]
  outp = sys.argv[2]
subprocess.check_call(['flex', '-o', outp, inp])
subprocess.check_call(['gcc', '-o', outp+".out", outp])
