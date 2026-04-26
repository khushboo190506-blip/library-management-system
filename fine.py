def calculate_fine(due_date, return_date):
    days_late = (return_date - due_date).days

    if days_late <= 0:
        return 0

    total_fine = 0

    for day in range(1, days_late + 1):
        week = (day - 1) // 7 + 1

        fine_per_day = 10
        for i in range(2, week + 1):
            fine_per_day *= i   # 10, 20, 60, 240...

        total_fine += fine_per_day

    return total_fine