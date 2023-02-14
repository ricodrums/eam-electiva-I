from typing import List
# Herencia
class Person:
    def __init__(self, name:str, lastname:str, document:str) -> None:
        self.name:str = name
        self.lastname:str = lastname
        self.document:str = document

    def set_document(self, old:str, new:str) -> None:
        # TODO: validate old document must be the same that actual document
        self.document:str = new

class Student(Person):
    def __init__(self, name:str, lastname:str, document:str, code:str) -> None:
        super().__init__(name, lastname, document)
        self.code:str = code
        self.courses:List[str] = []

    def add_course(self, course:str) -> None:
        self.courses.append(course)

class Teacer(Person):
    pass

student1 = Student('Jase', 'Naut', 'CC123456', 'ST123456')


# Exercise page 253
class File:
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.contents: List[str] = []

    def add_content(self, content: str) -> None:
        self.contents.append(content)

    def size(self) -> int:
        file_size: int = 0
        for content in self.contents:
            file_size += len(content)
        return file_size

    def info(self) -> str:
        return f'Contents: {self.contents}\nPath:{self.path} Size: {self.size()}B'

class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int) -> None:
        super().__init__(path)
        self.codec: str = codec
        self.geoloc: tuple = geoloc
        self.duration: int = duration

    def info(self) -> str:
        return f'{super().info()}\nCodec: {self.codec}\nGeolocalization: {self.geoloc}\nDuration: {self.duration}s'

class VideoFile(MediaFile):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int, dimensions: tuple) -> None:
        super().__init__(path, codec, geoloc, duration)
        self.dimensions: tuple = dimensions

    def info(self) -> str:
        return f'{super().info()}\nDimensions: {self.dimensions}'

file_1 = VideoFile('/home/python/vanrossum.mp4', 'h264', (23.5454, 31.4343), 487, (1920, 1080))
file_1.add_content('audio/ogg')
file_1.add_content('video/webm')
print(file_1.info())





