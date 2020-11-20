import time

def logging_time(func):
    """Decorator that logs time"""
    def logger():
        """Function that logs time"""
        start = time.time()
        func()
        print(f"Ausführungszeit für Funktion {func.__name__}: {time.time() - start:.5f}s")

    return logger

@logging_time
def calculate_sum():
    summe = sum(range(100000))
    print(f"Summe = {summe}")


if __name__ == '__main__':
    calculate_sum()