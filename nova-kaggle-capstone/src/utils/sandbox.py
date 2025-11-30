import sys
import io
import contextlib

@contextlib.contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

def run_code(code_string, global_vars=None):
    """
    Executes code string in a sandbox (captured output).
    Returns (output, error).
    """
    if global_vars is None:
        global_vars = {}
        
    with captured_output() as (out, err):
        try:
            exec(code_string, global_vars)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            
    return out.getvalue(), err.getvalue()
