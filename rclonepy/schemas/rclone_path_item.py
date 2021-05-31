from pydantic import BaseModel

class RclonePathItem(BaseModel):
    Path: str 
    Name: str
    Size: int
    MimeType: str # 'text/x-python; charset=utf-8', 
    ModTime: str # '2021-05-31T16:41:34.452008100+03:00', 
    IsDir: bool
