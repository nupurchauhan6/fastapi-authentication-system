# FastAPI JWT Authentication Example

This FastAPI application demonstrates how to implement JWT (JSON Web Token) authentication, including the use of refresh tokens for maintaining user sessions securely. The application provides endpoints for user login, token refreshing, and accessing protected routes.

## Features

- User Authentication with JWT
- Access Token and Refresh Token generation
- Endpoints for login, token refresh, and user-specific data retrieval

## Installation

To run this project, you need to have Python installed on your system. The project uses FastAPI, so you'll also need to install FastAPI and other dependencies.

```bash
# Clone the repository
git clone https://github.com/nupurchauhan6/fastapi-authentication-system.git

# It's recommended to use a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
