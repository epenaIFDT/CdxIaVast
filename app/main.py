"""
Punto de entrada único para FastAPI y CLI
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        from app.chat import main_cli
        main_cli()
    else:
        from app.api import app
