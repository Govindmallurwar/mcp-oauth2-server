# 🔐 OAuth2 Authentication for MCP Server

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![MCP](https://img.shields.io/badge/MCP-1.9+-orange.svg)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OAuth2.1](https://img.shields.io/badge/OAuth-2.1-red.svg)](https://oauth.net/2.1/)

A secure **Model Context Protocol (MCP) server** with **OAuth 2.1 authentication** that provides web search capabilities through the Tavily API. Built with FastAPI and designed for enterprise-grade security.
## 🚀 Features

- **🔐 OAuth 2.1 Authentication** - Enterprise-grade security using Scalekit authorization server
- **🌐 Web Search Integration** - Powered by Tavily API for real-time web search capabilities
- **⚡ FastAPI Performance** - High-performance async server with automatic API documentation
- **🛡️ MCP Compliance** - Full compliance with Model Context Protocol authorization specification
- **🎯 Scope-based Authorization** - Fine-grained access control with custom scopes
- **📊 Token Validation** - Robust token validation with audience checking
- **🔒 Security Best Practices** - PKCE support, proper error handling, and secure defaults

## 🏗️ Architecture

This MCP server implements a secure architecture with:

- **OAuth 2.1 Flow**: Complete authorization flow with Scalekit
- **MCP Protocol**: Standardized communication between LLMs and tools
- **Web Search Tool**: Tavily-powered search functionality
- **Middleware Security**: Request-level authentication and authorization

## 📋 Prerequisites

- **Python 3.11+** - Required for modern async features
- **Scalekit Account** - [Sign up here](https://app.scalekit.com/ws/signup)
- **Tavily API Key** - [Get your key here](https://tavily.com)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.dev/Govindmallurwar/mcp-oauth2-server.git
cd mcp-oauth2-server
```

### 2. Install Dependencies

```bash
# Using pip
pip install -e .

# Or using uv (recommended)
uv sync
```

### 3. Environment Configuration

Create a `.env` file with your configuration:

```env
# Scalekit Configuration
SCALEKIT_ENVIRONMENT_URL=https://your-company.scalekit.com
SCALEKIT_CLIENT_ID=your_client_id
SCALEKIT_CLIENT_SECRET=your_client_secret
SCALEKIT_AUDIENCE_NAME=your_audience_name

# Server Configuration
PORT=10000

# Tavily API Configuration
TAVILY_API_KEY=your_tavily_api_key_here
```

### 4. Scalekit Setup

1. Navigate to **MCP servers** in your Scalekit dashboard
2. Click **Add MCP server**
3. Configure:
    - **Server name**: "Web Search MCP Server"
    - **Resource identifier**: Your server URL
    - **Allow dynamic client registration**: ✅ Enable
    - **Access token lifetime**: 300-3600 seconds
    - **Scopes**: `search:read`

## 🚀 Quick Start

### Run the Server

```bash
python src/server.py
```

The server will start on `http://localhost:10001`


## 📚 API Documentation

### OAuth Discovery Endpoints

- `GET /.well-known/oauth-protected-resource/mcp` - MCP resource metadata

### MCP Endpoints

- `POST /tools/call` - Execute web search tool (requires authentication)

### Authentication Flow

1. **Discovery**: Client discovers authorization server via metadata endpoint
2. **Registration**: Dynamic client registration with Scalekit
3. **Authorization**: OAuth 2.1 flow with PKCE
4. **Token Usage**: Bearer token in Authorization header
5. **Validation**: Server validates token and checks scopes

## 🔧 Configuration

### Environment Variables

| Variable | Description                   | Required |
|----------|-------------------------------|----------|
| `SCALEKIT_ENVIRONMENT_URL` | Your Scalekit environment URL | ✅ |
| `SCALEKIT_CLIENT_ID` | Scalekit client ID            | ✅ |
| `SCALEKIT_CLIENT_SECRET` | Scalekit client secret        | ✅ |
| `SCALEKIT_AUDIENCE_NAME` | Token audience identifier     | ✅ |
| `PORT` | Server port (default: 10001)  | ❌ |
| `TAVILY_API_KEY` | Tavily API key for web search | ✅ |

### Security Settings

The server implements several security features:

- **Token Audience Validation**: Ensures tokens are issued for this specific server
- **Scope-based Authorization**: Controls access to web search functionality
- **PKCE Support**: Protects against authorization code interception
- **Proper Error Responses**: Returns WWW-Authenticate headers as per MCP spec


## 🔍 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Token validation fails | Check `SCALEKIT_AUDIENCE_NAME` matches Scalekit config |
| Client registration fails | Verify Scalekit environment URL and credentials |
| Web search not working | Ensure Tavily API key is valid and has quota |
| CORS errors | Configure `allow_origins` in production |

### Debug Mode

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Health Checks

```bash
# Check OAuth metadata
curl http://localhost:10000/.well-known/oauth-protected-resource/mcp
```

## 📁 Project Structure

```
mcp-oauth2-server/
├── src/
│   ├── server.py          # Main FastAPI server
│   ├── auth.py            # OAuth middleware
│   ├── tavily_mcp.py      # MCP server implementation
│   └── config.py          # Configuration management
├── docs/
├── pyproject.toml         # Project dependencies
├── .env                   # Environment with placeholder
└── README.md              # This file
```


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.