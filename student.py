from student import Student

def main():
    print("=== ระบบคำนวณเกรดนักเรียน ===")

    student_id = input("รหัสนักเรียน: ")
    name = input("ชื่อ: ")

    try:
        score = float(input("คะแนน (0-100): "))
    except ValueError:
        print("❌ คะแนนต้องเป็นตัวเลข")
        return

    if score < 0 or score > 100:
        print("❌ คะแนนต้องอยู่ระหว่าง 0 - 100")
        return

    student = Student(student_id, name, score)

    print("\n--- ผลลัพธ์ ---")
    print(f"รหัส: {student.student_id}")
    print(f"ชื่อ: {student.name}")
    print(f"คะแนน: {student.score}")
    print(f"เกรด: {student.grade()}")

if __name__ == "__main__":
    main()
