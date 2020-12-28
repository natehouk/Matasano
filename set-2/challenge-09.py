import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.util import pad

print(pad("YELLOW SUBMARINE", 20))