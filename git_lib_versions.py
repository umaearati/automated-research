import importlib.metadata
packages = [
    "langgraph",
    "langchain_community",
    "langchain_core",
    "tavily-python",
    "wikipedia",
"wikipedia",
"langchain-openai",
"langchain-google-genai",
"langchain-groq",
"structlog",
"python-docx",
"reportlab"
    ]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")