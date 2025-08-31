
import contextlib
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth import AuthMiddleware
from .config import settings
from .tavily_mcp import mcp as tavily_mcp_server

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with tavily_mcp_server.session_manager.run():
        yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/.well-known/oauth-protected-resource/mcp")
async def oauth_protected_resource_metadata():
    """
    OAuth 2.0 Protected Resource Metadata endpoint for MCP client discovery.
    Required by the MCP specification for authorization server discovery.
    """
    return {
        "authorization_servers": [settings.SCALEKIT_AUTHORIZATION_SERVERS],
        "bearer_methods_supported": ["header"],
        "resource": f"http://localhost:{settings.PORT}/mcp",
        "resource_documentation": settings.SCALEKIT_RESOURCE_DOCS_URL,
        "scopes_supported": [
          "mcp:tools:search:read"
        ],
    }

mcp_server = tavily_mcp_server.streamable_http_app()
app.add_middleware(AuthMiddleware)
app.mount("/", mcp_server)

def main():
    """Main entry point for the MCP server."""
    uvicorn.run(app, host="localhost", port=settings.PORT, log_level="debug")

if __name__ == "__main__":
    main()
