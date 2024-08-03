class Storage:
    file_name="storage.txt"

    @classmethod
    def to_txt(cls,text):
        file  = open(cls.file_name,"+a")
        file.write(text + "\n")
        file.close()

