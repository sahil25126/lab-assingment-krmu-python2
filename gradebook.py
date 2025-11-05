"""
===============================================================
Title   : GradeBook Analyzer CLI
Author  : Kunal Singh
Date    : 05-Nov-2025
Purpose : A simple command-line tool for analyzing student marks.
          It can read marks from manual input or a CSV file,
          calculate basic statistics, assign letter grades,
          and show summary tables — all in one place.
===============================================================
"""

import csv
import pandas as pd
import statistics

# ------------------------------------------------------------
# 🏁  Welcome & Menu Display
# ------------------------------------------------------------
def show_menu():
    print("\n===================================================")
    print("🎓 Welcome to GradeBook Analyzer")
    print("===================================================")
    print("Choose an option:")
    print("1️⃣  Enter student marks manually")
    print("2️⃣  Import marks from a CSV file")
    print("3️⃣  Exit program")
    print("===================================================")


# ------------------------------------------------------------
# 🧍 Task 2: Data Entry (Manual or CSV)
# ------------------------------------------------------------
def get_manual_data():
    """Collect student names and marks manually from user input."""
    marks = {}
    try:
        count = int(input("Enter number of students: "))
        for i in range(count):
            name = input(f"Enter name of student {i + 1}: ").strip()
            score = float(input(f"Enter marks for {name}: "))
            marks[name] = score
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers correctly.")
    return marks


def get_csv_data():
    """Load marks from a CSV file with 'Name' and 'Marks' columns."""
    filename = input("Enter CSV filename (e.g., sample_marks.csv): ").strip()
    marks = {}

    try:
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            marks[row['Name']] = float(row['Marks'])
        print("✅ CSV data loaded successfully!")
    except FileNotFoundError:
        print("❌ File not found! Please check your filename.")
    except Exception as e:
        print(f"⚠️ Error reading CSV: {e}")
    return marks


# ------------------------------------------------------------
# 📊 Task 3: Statistical Functions
# ------------------------------------------------------------
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict) if marks_dict else 0


def calculate_median(marks_dict):
    return statistics.median(marks_dict.values()) if marks_dict else 0


def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else 0


def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else 0


# ------------------------------------------------------------
# 🎯 Task 4: Grade Assignment
# ------------------------------------------------------------
def assign_grades(marks_dict):
    """Assign letter grades based on numeric marks."""
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades


def show_grade_distribution(grades_dict):
    """Display how many students received each grade."""
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades_dict.values():
        distribution[grade] += 1

    print("\n📊 Grade Distribution:")
    for grade, count in distribution.items():
        print(f"  {grade}: {count} student(s)")


# ------------------------------------------------------------
# 🧮 Task 5: Pass / Fail Filter
# ------------------------------------------------------------
def show_pass_fail_summary(marks_dict):
    """Show which students passed or failed (pass mark = 40)."""
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]

    print("\n✅ Passed Students:")
    print(", ".join(passed) if passed else "None")

    print("\n❌ Failed Students:")
    print(", ".join(failed) if failed else "None")

    print(f"\nSummary: {len(passed)} passed, {len(failed)} failed.")


# ------------------------------------------------------------
# 🧾 Task 6: Display Final Results
# ------------------------------------------------------------
def display_results(marks_dict, grades_dict):
    """Print a clean table of students with marks and grades."""
    print("\n-------------------------------------------")
    print(f"{'Name':<15}{'Marks':<10}{'Grade':<5}")
    print("-------------------------------------------")
    for name, score in marks_dict.items():
        print(f"{name:<15}{score:<10}{grades_dict[name]}")
    print("-------------------------------------------")


# ------------------------------------------------------------
# 💾 Bonus: Export to CSV
# ------------------------------------------------------------
def export_to_csv(marks, grades, filename="final_results.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks", "Grade"])
        for name in marks:
            writer.writerow([name, marks[name], grades[name]])
    print(f"\nResults exported successfully to '{filename}'")

# ------------------------------------------------------------
# 🔁 Main CLI Loop
# ------------------------------------------------------------
def start_gradebook():
    """Main control loop for the GradeBook CLI."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            marks = get_manual_data()
        elif choice == "2":
            marks = get_csv_data()
        elif choice == "3":
            print("\n👋 Exiting GradeBook Analyzer. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")
            continue

        if not marks:
            print("⚠️ No data available to analyze.")
            continue

        # Perform analysis
        avg = calculate_average(marks)
        median = calculate_median(marks)
        highest = find_max_score(marks)
        lowest = find_min_score(marks)

        print("\n📈 Statistics Summary:")
        print(f"  Average Marks : {avg:.2f}")
        print(f"  Median Marks  : {median:.2f}")
        print(f"  Highest Score : {highest}")
        print(f"  Lowest Score  : {lowest}")

        # Assign grades and show summaries
        grades = assign_grades(marks)
        show_grade_distribution(grades)
        show_pass_fail_summary(marks)
        display_results(marks, grades)

        # Optional export
        save_option = input("\nWould you like to export results to CSV? (y/n): ").lower()
        if save_option == "y":
            export_to_csv(marks, grades)

        # Loop again?
        repeat = input("\nRun another analysis? (y/n): ").lower()
        if repeat != "y":
            print("👋 Thanks for using GradeBook Analyzer!")
            break


# ------------------------------------------------------------
# 🚀 Main Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    start_gradebook()
