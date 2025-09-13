import os
import json
from typing import Dict, Any

import httpx
from fastapi import Depends, HTTPException, status, Request
from jose import jwt
from jose.exceptions import JWTError


class ClerkJWKSCache:
    def __init__(self) -> None:
        self._jwks: Dict[str, Any] | None = None
        self._cached_url: str | None = None

    async def get_jwks(self, jwks_url: str) -> Dict[str, Any]:
        if self._jwks is not None and self._cached_url == jwks_url:
            return self._jwks
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(jwks_url)
            resp.raise_for_status()
            self._jwks = resp.json()
            self._cached_url = jwks_url
            return self._jwks


jwks_cache = ClerkJWKSCache()


async def verify_clerk_jwt(request: Request) -> Dict[str, Any]:
    authorization = request.headers.get("authorization") or request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")

    token = authorization.split(" ", 1)[1]
    issuer = os.getenv("CLERK_ISSUER", "")
    jwks_url = os.getenv("CLERK_JWKS_URL", "")
    if not issuer or not jwks_url:
        raise HTTPException(status_code=500, detail="Auth not configured")

    jwks = await jwks_cache.get_jwks(jwks_url)

    try:
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")
        if not kid:
            raise HTTPException(status_code=401, detail="Invalid token header")

        key = None
        for jwk in jwks.get("keys", []):
            if jwk.get("kid") == kid:
                key = jwk
                break

        if key is None:
            raise HTTPException(status_code=401, detail="Signing key not found")

        claims = jwt.decode(
            token,
            key,
            algorithms=[unverified_header.get("alg", "RS256")],
            audience=None,
            issuer=issuer,
            options={"verify_aud": False},
        )
        return claims
    except JWTError as exc:
        raise HTTPException(status_code=401, detail=f"Invalid token: {exc}") from exc

