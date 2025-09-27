import itertools

# Danh sách các phương án
alternatives = ["A", "B", "C", "D"]

# Giả sử kết quả so sánh cặp được người dùng/ chuyên gia cho trước
# (có thể là input từ khảo sát hoặc ma trận so sánh)
# Cấu trúc: ("A", "B", "A") nghĩa là A thắng B
comparisons = [
    ("A", "B", "A"),
    ("A", "C", "A"),
    ("A", "D", "D"),
    ("B", "C", "C"),
    ("B", "D", "B"),
    ("C", "D", "C"),
    ("A", "D", "A")
]

# Tính điểm thắng cho từng phương án
scores = {alt: 0 for alt in alternatives}

for x, y, winner in comparisons:
    scores[winner] += 1

# Sắp xếp theo điểm
ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("Kết quả Pairwise Comparison:")
for alt, score in ranking:
    print(f"{alt}: {score} điểm")