# Countdown Timer & Stopwatch
# A dual-mode timer with countdown and stopwatch functionality

import time


def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"


def countdown_timer():
    print("\n--- COUNTDOWN TIMER ---")
    try:
        hrs = int(input("Hours: ") or 0)
        mins = int(input("Minutes: ") or 0)
        secs = int(input("Seconds: ") or 0)
    except ValueError:
        print("Invalid input!")
        return

    total = hrs * 3600 + mins * 60 + secs
    if total <= 0:
        print("Time must be greater than 0!")
        return

    print(f"\nCountdown started: {format_time(total)}")
    print("Press Ctrl+C to cancel.\n")

    try:
        while total > 0:
            print(f"\r  ⏳ {format_time(total)} ", end="", flush=True)
            time.sleep(1)
            total -= 1

        print(f"\r  ⏳ {format_time(0)} ")
        print("\n🔔 TIME'S UP!")
        # Beep alert
        for _ in range(3):
            print("\a", end="", flush=True)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"\n\nTimer cancelled with {format_time(total)} remaining.")


def stopwatch():
    print("\n--- STOPWATCH ---")
    print("Press Enter to start...")
    input()

    laps = []
    print("Stopwatch running! Press Enter for lap, type 'stop' + Enter to stop.\n")

    start_time = time.time()
    lap_start = start_time

    try:
        while True:
            user_input = input(f"  ⏱ Running... (Lap {len(laps) + 1}): ").strip().lower()

            current = time.time()

            if user_input == "stop":
                elapsed = current - start_time
                print(f"\n  Stopped at: {format_time(elapsed)}")
                break
            else:
                lap_time = current - lap_start
                total_time = current - start_time
                laps.append(lap_time)
                lap_start = current
                print(f"    Lap {len(laps)}: {format_time(lap_time)}  (Total: {format_time(total_time)})")

    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        print(f"\n\n  Stopped at: {format_time(elapsed)}")

    if laps:
        print(f"\n{'Lap':<8} {'Time':<12} ")
        print("-" * 20)
        for i, lap in enumerate(laps, 1):
            print(f"{'#' + str(i):<8} {format_time(lap):<12}")
        print("-" * 20)
        print(f"{'Best':<8} {format_time(min(laps))}")
        print(f"{'Worst':<8} {format_time(max(laps))}")
        print(f"{'Avg':<8} {format_time(sum(laps) / len(laps))}")


def pomodoro_timer():
    print("\n--- POMODORO TIMER ---")
    try:
        work_min = int(input("Work duration (minutes) [25]: ") or 25)
        break_min = int(input("Break duration (minutes) [5]: ") or 5)
        sessions = int(input("Number of sessions [4]: ") or 4)
    except ValueError:
        print("Invalid input!")
        return

    print(f"\nPomodoro: {work_min}min work / {break_min}min break x {sessions} sessions")
    print("Press Ctrl+C to cancel.\n")

    try:
        for session in range(1, sessions + 1):
            # Work phase
            print(f"📗 Session {session}/{sessions} - WORK ({work_min} min)")
            remaining = work_min * 60
            while remaining > 0:
                print(f"\r  ⏳ {format_time(remaining)} ", end="", flush=True)
                time.sleep(1)
                remaining -= 1
            print(f"\r  ⏳ {format_time(0)} ")
            print("🔔 Work done!\a")

            if session < sessions:
                # Break phase
                print(f"\n☕ BREAK ({break_min} min)")
                remaining = break_min * 60
                while remaining > 0:
                    print(f"\r  ⏳ {format_time(remaining)} ", end="", flush=True)
                    time.sleep(1)
                    remaining -= 1
                print(f"\r  ⏳ {format_time(0)} ")
                print("🔔 Break over!\a\n")

        total_work = work_min * sessions
        total_break = break_min * (sessions - 1)
        print(f"\n✅ All {sessions} sessions complete!")
        print(f"   Total work:  {format_time(total_work * 60)}")
        print(f"   Total break: {format_time(total_break * 60)}")

    except KeyboardInterrupt:
        print("\n\nPomodoro cancelled.")


def main():
    print("=" * 40)
    print("    COUNTDOWN TIMER & STOPWATCH")
    print("=" * 40)

    while True:
        print("\n1. Countdown Timer")
        print("2. Stopwatch")
        print("3. Pomodoro Timer")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            countdown_timer()
        elif choice == "2":
            stopwatch()
        elif choice == "3":
            pomodoro_timer()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
