-- Supabase schema for NeuroSpace
create extension if not exists "pgcrypto";

create table if not exists files (
  id uuid primary key default gen_random_uuid(),
  file_key text not null,
  file_name text not null,
  user_id text not null,
  file_size bigint default 0,
  content_type text default '',
  status text default 'uploaded',
  chunks_count integer default 0,
  embedding_count integer default 0,
  last_error text,
  created_at timestamptz default now(),
  processed_at timestamptz
);

create index if not exists idx_files_user_id on files(user_id);
create index if not exists idx_files_status on files(status);

create table if not exists processing_jobs (
  id uuid primary key default gen_random_uuid(),
  file_id uuid references files(id) on delete cascade,
  user_id text not null,
  status text default 'queued',
  created_at timestamptz default now(),
  completed_at timestamptz
);

create index if not exists idx_processing_jobs_file_id on processing_jobs(file_id);
create index if not exists idx_processing_jobs_user_id on processing_jobs(user_id);
create index if not exists idx_processing_jobs_status on processing_jobs(status);

