# NeuroSpace

Your AI-Powered Second Brain, Reimagined.

## Overview

NeuroSpace is a full‑stack application: Next.js 15 (React 19, TypeScript, Tailwind, Framer Motion, Clerk) on the frontend and FastAPI on the backend. It integrates with AWS S3 for storage, Supabase (PostgreSQL) for data, Pinecone for vector search, and Nvidia NIM for embeddings and chat models.

## Architecture

- Frontend: Next.js 15, React 19, TypeScript, Tailwind CSS, Framer Motion, Clerk
- Backend: FastAPI (Python 3.9+), Uvicorn, Pydantic, Celery, Redis
- AI: Nvidia NIM embeddings and LLMs, Pinecone vector DB
- Infra: AWS S3, Supabase (PostgreSQL), Vercel (frontend), Railway/Render (backend)

## Prerequisites

- Node.js 18+
- Python 3.9+
- Accounts/keys: AWS, Nvidia NIM, Pinecone, Supabase, Clerk

## Local Setup

1) Install frontend deps

```bash
cd frontend
npm install
npm run dev
```

2) Install backend deps

```bash
cd ../backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

3) Configure environment variables

- Frontend: copy `.env.local.example` to `.env.local` and fill values
- Backend: copy `.env.example` to `.env` and fill values

4) Initialize database schema (Supabase)

- Run `backend/supabase_schema.sql` in Supabase SQL Editor

5) Start dev servers: see the commands above in steps 1 and 2.

## Environment Variables

Frontend required:

- NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY
- CLERK_SECRET_KEY
- NEXT_PUBLIC_SUPABASE_URL
- SUPABASE_ANON_KEY
- NEXT_PUBLIC_BACKEND_URL

Backend required:

- AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, AWS_S3_BUCKET_NAME
- NVIDIA_NIM_API_KEY
- PINECONE_API_KEY, PINECONE_ENVIRONMENT
- SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
- CLERK_JWKS_URL, CLERK_ISSUER
## Authentication

Frontend (Clerk):

- Add keys to `frontend/.env.local`
- Routes available: `/sign-in`, `/sign-up`
- Protected route: `/dashboard` (enforced by `middleware.ts`)

Backend (JWT verification):

- Set `CLERK_JWKS_URL` and `CLERK_ISSUER` in `backend/.env`
- `GET /me` returns token claims when called with `Authorization: Bearer <token>`


## Scripts

- Frontend: `npm run dev`, `npm run build`, `npm start`
- Backend: `python main.py`

## License

Proprietary – © ezDecode

