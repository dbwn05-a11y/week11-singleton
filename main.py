from singleton import SingletonCounter


def main():
    first = SingletonCounter.get_instance()
    second = SingletonCounter.get_instance()

    print("같은 인스턴스인가:", first is second)
    print("변경 전 second.count:", second.count)

    first.increment()
    print("first로 1 증가 후 second.count:", second.count)

    # 다시 요청해도 같은 객체이며, 변경한 상태가 유지되는지 확인한다.
    third = SingletonCounter.get_instance()
    print("다시 요청한 인스턴스도 같은가:", first is third)
    print("다시 요청한 후 third.count:", third.count)

    try:
        SingletonCounter()
    except TypeError as error:
        print("직접 생성 제한:", error)


if __name__ == "__main__":
    main()
