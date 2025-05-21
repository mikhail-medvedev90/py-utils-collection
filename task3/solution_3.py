def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Объединяет пересекающиеся или смежные интервалы."""
    if not intervals:
        return []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = [list(sorted_intervals[0])]
    for current in sorted_intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1][1] = max(last[1], current[1])
        else:
            merged.append(list(current))
    return [(i[0], i[1]) for i in merged]


def crop_and_merge(intervals_list: list[int], lesson_start: int, lesson_end: int) -> list[tuple[int, int]]:
    """Обрезает интервалы по уроку и объединяет их."""
    pairs = list(zip(intervals_list[::2], intervals_list[1::2]))
    cropped = []
    for s, e in pairs:
        new_s = max(s, lesson_start)
        new_e = min(e, lesson_end)
        if new_s < new_e:
            cropped.append((new_s, new_e))
    return merge_intervals(cropped)


def intersect(a: list[tuple[int, int]], b: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Находит пересечения двух списков интервалов."""
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        a_start, a_end = a[i]
        b_start, b_end = b[j]
        start = max(a_start, b_start)
        end = min(a_end, b_end)
        if start < end:
            result.append((start, end))
        if a_end < b_end:
            i += 1
        else:
            j += 1
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    """
    Возвращает время общего присутствия ученика и учителя на уроке (в секундах).
    """
    lesson_start, lesson_end = intervals['lesson']

    pupil = crop_and_merge(intervals['pupil'], lesson_start, lesson_end)
    tutor = crop_and_merge(intervals['tutor'], lesson_start, lesson_end)

    total = 0
    for start, end in intersect(pupil, tutor):
        total += end - start
    return total
