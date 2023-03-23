import logging

import uvicorn

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True,
    )
