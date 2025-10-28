# ==============================================================================
# Installation & Setup
# ==============================================================================

# Install dependencies using uv package manager.
# For Windows, please ensure 'uv' is installed and in your PATH.
# You can install it using PowerShell:
#   irm https://astral.sh/uv/install.ps1 | iex
install:
	@echo "Installing backend and frontend dependencies..."
	uv sync --dev && (cd frontend && npm install)
	@echo "Installation complete."

# ==============================================================================
# Playground Targets
# ==============================================================================

# Launch local dev playground
playground: build-frontend-if-needed
	@echo "==============================================================================="
	@echo "| 🚀 Starting your agent playground...                                        |"
	@echo "|                                                                             |"
	@echo "| 🌐 Access your app at: http://localhost:8000                               |"
	@echo "| 💡 Try asking: I want to learn machine learning!                         |"
	@echo "|                                                                             |"
	@echo "| 🔍 IMPORTANT: Select the 'ai_tutor' folder to interact with your agent.          |"
	@echo "==============================================================================="
	uv run python -m ai_tutor.utils.expose_app --mode local --local-agent ai_tutor.agent.root_agent

# ==============================================================================
# Local Development Commands
# ==============================================================================

# Launch local development server with hot-reload
local-backend:
	uv run python -m ai_tutor.utils.expose_app --mode local --port 8000  --local-agent ai_tutor.agent.root_agent

# ==============================================================================
# ADK Live Commands
# ==============================================================================

# Build the frontend for production
build-frontend:
	(cd frontend && npm run build)

# Build the frontend only if needed (conditional build)
# This target uses a Python script for cross-platform compatibility.
build-frontend-if-needed:
	@python scripts/check_frontend_build.py && $(MAKE) build-frontend || echo "Frontend build is up to date. Skipping build."

# Connect to remote deployed agent
playground-remote: build-frontend-if-needed
	@echo "==============================================================================="
	@echo "| 🚀 Connecting to REMOTE agent...                                           |"
	@echo "|                                                                             |"
	@echo "| 🌐 Access your app at: http://localhost:8000                               |"
	@echo "| ☁️  Connected to deployed agent engine                                      |"
	@echo "==============================================================================="
	uv run python -m app.utils.expose_app --mode remote

# Start the frontend UI separately for development (requires backend running separately)
ui:
	(cd frontend && PORT=8501 npm start)

# Launch dev playground with both frontend and backend hot-reload
playground-dev:
	@echo "==============================================================================="
	@echo "| 🚀 Starting your agent playground in DEV MODE...                           |"
	@echo "|                                                                             |"
	@echo "| 🌐 Frontend: http://localhost:8501                                         |"
	@echo "| 🌐 Backend:  http://localhost:8000                                         |"
	@echo "| 💡 Try asking: I want to learn machine learning!                         |"
	@echo "| 🔄 Both frontend and backend will auto-reload on changes                    |"
	@echo "==============================================================================="
	@echo "Starting backend server..."
	$(MAKE) local-backend &
	@echo "Starting frontend dev server..."
	$(MAKE) ui

# ==============================================================================
# Backend Deployment Targets
# ==============================================================================

# Deploy the agent remotely
backend:
	# Export dependencies to requirements file using uv export.
	uv export --no-hashes --no-header --no-dev --no-emit-project --no-annotate > .requirements.txt 2>/dev/null || \
	uv export --no-hashes --no-header --no-dev --no-emit-project > .requirements.txt && uv run ai_tutor/agent_engine_app.py


# ==============================================================================
# Infrastructure Setup
# ==============================================================================

# Set up development environment resources using Terraform
setup-dev-env:
	PROJECT_ID=$$(gcloud config get-value project) && \
	(cd deployment/terraform/dev && terraform init && terraform apply --var-file vars/env.tfvars --var dev_project_id=$$PROJECT_ID --auto-approve)

# ==============================================================================
# Testing & Code Quality
# ==============================================================================

# Run unit and integration tests
test:
	uv run pytest tests/unit && uv run pytest tests/integration

# Run code quality checks (codespell, ruff, mypy)
lint:
	uv sync --dev --extra lint
	uv run codespell
	uv run ruff check . --diff
	uv run ruff format . --check --diff
	uv run mypy .

# ==============================================================================
# Gemini Enterprise Integration
# ==============================================================================

# Register the deployed agent to Gemini Enterprise
# Usage: make register-gemini-enterprise GEMINI_ENTERPRISE_APP_ID=projects/{project_number}/locations/{location}/collections/{collection}/engines/{engine_id} [AGENT_ENGINE_ID=<id>]  # Defaults to deployment_metadata.json
register-gemini-enterprise:
	uvx --from agent-starter-pack agent-starter-pack-register-gemini-enterprise \
		$(if $(GEMINI_ENTERPRISE_APP_ID),--gemini-enterprise-app-id="$(GEMINI_ENTERPRISE_APP_ID)",) \
		$(if $(AGENT_ENGINE_ID),--agent-engine-id="$(AGENT_ENGINE_ID)",) \
		$(if $(GEMINI_DISPLAY_NAME),--display-name="$(GEMINI_DISPLAY_NAME)",) \
		$(if $(GEMINI_DESCRIPTION),--description="$(GEMINI_DESCRIPTION)",) \
		$(if $(GEMINI_TOOL_DESCRIPTION),--tool-description="$(GEMINI_TOOL_DESCRIPTION)",) \
		$(if $(GEMINI_AUTHORIZATION_ID),--authorization-id="$(GEMINI_AUTHORIZATION_ID)",)