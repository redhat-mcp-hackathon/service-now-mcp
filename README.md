# Service Now MCP Server

A Model Context Protocol (MCP) server that provides access to Red Hat Help center ticketing system. This server enables AI assistants automate and generate tickets to enable faster and streamline on-board of new employees.

## Overview

This MCP server communicates with Service Now APIs and provides the following tools:

- **`open_locker_ticket`** - Generate a new locker ticket for the employee


## Features

### Available Tools

#### 1.Open Locker Ticket (`open_locker_ticket`)

## Prerequisites

- Python 3.8+
- Podman or Docker

## Installation & Setup

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd service-now-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python mcp_server.py
```

### Container Deployment

## Building locally

To build the container image locally using Podman, run:

```sh
podman build -t service-now-mcp:latest .
```

This will create a local image named `service-now-mcp:latest` that you can use to run the server.

### VS Code Continue Integration

Example configuration to add to VS Code Continue:

```json
"experimental": {
    "modelContextProtocolServers": [
      {
        "name": "service-now-mcp",
        "transport": {
          "type": "stdio",
          "command": "podman",
          "args": [
            "run",
            "-i",
            "--rm",
            "-e", "API_BASE_URL",
            "localhost/service-now-mcp:latest"
          ],
          "env": {
            "API_BASE_URL": "https://redhat.service-now.com"
          }  
        }
      },
    ]
  }
```

### Run with Service Now Mock

1. Create a new podman network: `podman network create service-now`
1. Go to the mock directory and build it's image:
  1. `cd mock_service_now`
  1. `podman build -t service-mock:latest .`
1. Run the service now mock server: `podman run --rm -p 8000:8000 --network=service-now --name=service-mock service-mock`
1. Comment out the service now with real RH base url and add the mocked base url
```json
"experimental": {
    "modelContextProtocolServers": [
      // {
      //   "name": "service-now-mcp",
      //   "transport": {
      //     "type": "stdio",
      //     "command": "podman",
      //     "args": [
      //       "run",
      //       "-i",
      //       "--rm",
      //       "-e", "API_BASE_URL",
      //       "localhost/service-now-mcp:latest"
      //     ],
      //     "env": {
      //       "API_BASE_URL": "https://redhat.service-now.com"
      //     }  
      //   }
      // },
      {
        "name": "service-now-mcp-mock",
        "transport": {
          "type": "stdio",
          "command": "podman",
          "args": [
            "run",
            "-i",
            "--rm",
            "--network=service-now",
            "-e", "API_BASE_URL",
            "localhost/service-now-mcp:latest"
          ],
          "env": {
            "API_BASE_URL": "http://service-mock:8000"
          }  
        }
      }
    ]
  }
```

## Roadmap

- [x] Prove initial POC capabel of openning a simple ticket via serivce now API.
- [x] Update readme file to include installation details etc.
- [x] Create a mock service now server for faster feedback loop & reduced risk
- [ ] Add instructions or script for obtaining user authentication
- [ ] Create & use variables for: base url, header, cookies 
- [ ] Improve open locker ticket tool (looker size, floor, etc)
- [ ] Add additional tools: new badge request, payroll request, list open tickets, etc

## Environment Variables

TODO needs to be implemented

## Data Privacy

Currently this service requires obtaining the users:
- url
- headers
- cookies

This sensitive info is currently stored in a sensetive_data.py not commited to the repository.
We will further improve this implementation by passing this data as Environment Variables.
