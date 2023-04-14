def solution(numbers):
    numbers = [str(number) for number in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))