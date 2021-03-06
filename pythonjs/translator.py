#!/usr/bin/env python
import sys, traceback

from python_to_pythonjs import main as python_to_pythonjs
from pythonjs import main as pythonjs_to_javascript
from pythonjs_to_dart import main as pythonjs_to_dart
from pythonjs_to_coffee import main as pythonjs_to_coffee
from pythonjs_to_lua import main as pythonjs_to_lua
from pythonjs_to_luajs import main as pythonjs_to_luajs


def main(script):
    if '--visjs' in sys.argv:
        import python_to_visjs
        return python_to_visjs.main( script )
    else:
        code = ''
        if '--dart' in sys.argv:
            a = python_to_pythonjs(script, dart=True)
            code = pythonjs_to_dart( a )
        elif '--coffee' in sys.argv:
            a = python_to_pythonjs(script, coffee=True)
            code = pythonjs_to_coffee( a )
        elif '--lua' in sys.argv:
            a = python_to_pythonjs(script, lua=True)
            try: code = pythonjs_to_lua( a )
            except SyntaxError:
                sys.stderr.write( '\n'.join([traceback.format_exc(),a]) )
                
        elif '--luajs' in sys.argv:
            a = python_to_pythonjs(script, lua=True)
            code = pythonjs_to_luajs( a )
        else:
            a = python_to_pythonjs(script)
            code = pythonjs_to_javascript( a )

        return code

def command():
    scripts = []
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg.endswith('.py'):
                scripts.append( arg )

    if len(scripts):
        a = []
        for script in scripts:
            a.append( open(script, 'rb').read() )
        data = '\n'.join( a )
    else:
        data = sys.stdin.read()

    js = main(data)
    print(js)


if __name__ == '__main__':
    command()
