from fastapi import Request, HTTPException

async def login(request: Request):
    try:
        body = await request.json()
        username = body.get("username")
        password = body.get("password")

        if not username or not password:
            raise HTTPException(status_code=400, detail="Username and password required")

        # Anfrage an DB Handler

        return HTTPException(status_code=200, detail="Anfrage erfolgreich")
    except Exception as e:
        print(f"Error in login function: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))