from config import DEBUG, APP_NAME
from utils import add, shout
from utils.string_tools import whisper

def main():
    print(f"Приложение: {APP_NAME}")
    print("DEBUG mode:", DEBUG)

    print("Сумма:", add(5, 3))
    print("Громко:", shout("hello"))
    print("Тихо:", whisper("HELLO"))

if __name__ == "__main__":
    main()
