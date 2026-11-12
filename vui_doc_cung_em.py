import os
import tkinter as tk
from tkinter import messagebox

# Dữ liệu 4 chủ đề bài học lớp 1
lessons_data = {
    1: {
        "title": "Chủ đề 1: Tôi và các bạn",
        "text": "Tôi tên là Nam, học sinh lớp 1A. Ngày đầu đến trường, mặc bộ đồng phục mới, tôi hãnh diện lắm. Tôi có thêm nhiều bạn mới. Giờ ra chơi, chúng tôi cùng nhau chơi trò chơi kéo co vui vẻ.",
        "question": "Bạn Nam học lớp mấy?",
        "options": ["Lớp 1A", "Lớp 2B", "Lớp mẫu giáo"],
        "correct": 0
    },
    2: {
        "title": "Chủ đề 2: Mái ấm gia đình",
        "text": "Mỗi tối, gia đình em quây quần bên phòng khách. Bố đọc báo, mẹ gọt trái cây còn em ngồi chăm chú làm bài tập. Em rất yêu mái ấm nhỏ bé và ngập tràn tiếng cười của mình.",
        "question": "Ai là người đọc báo trong bài?",
        "options": ["Mẹ", "Bố", "Em"],
        "correct": 1
    },
    3: {
        "title": "Chủ đề 3: Bài học từ cuộc sống",
        "text": "Trên đường đi học về, Nam nhìn thấy bà cụ đang đứng ngập ngừng qua đường. Nam liền chạy tới, lễ phép nắm tay dẫn bà sang đường an toàn. Bà cụ mỉm cười khen Nam là em bé ngoan ngoãn.",
        "question": "Bạn Nam đã giúp ai qua đường?",
        "options": ["Em bé", "Bà cụ", "Thầy giáo"],
        "correct": 1
    },
    4: {
        "title": "Chủ đề 4: Thiên nhiên kì thú",
        "text": "Buổi sáng, khu vườn ngập tràn ánh nắng vàng ấm áp. Những chú bướm rực rỡ sắc màu đang dập dờn bay lượn trên những đóa hoa cúc trắng. Cạnh đó, chim hót líu lo chào đón một ngày mới tuyệt vời.",
        "question": "Loài vật nào bay lượn trên đóa hoa cúc trắng?",
        "options": ["Ong vàng", "Chim sẻ", "Chú bướm"],
        "correct": 2
    }
}

class HocLieuSoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vui Đọc Cùng Em - Lớp 1")
        self.root.geometry("900x650")
        self.root.config(bg="#e8f4f8")
        
        self.current_lesson = None
        self.create_cover_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_cover_screen(self):
        self.clear_screen()

        # Khung chính cho trang bìa
        cover_frame = tk.Frame(self.root, bg="#d4edda")
        cover_frame.pack(fill=tk.BOTH, expand=True)

        # Tiêu đề logo ứng dụng
        lbl_logo = tk.Label(
            cover_frame, text="📖 VUI ĐỌC CÙNG EM 🌟", 
            font=("Arial", 26, "bold"), fg="#d63031", bg="#d4edda"
        )
        lbl_logo.pack(pady=40)

        # Lời chào / Phụ đề
        lbl_welcome = tk.Label(
            cover_frame, text="Xin chào bạn!", 
            font=("Arial", 20, "bold"), fg="#2d3436", bg="#d4edda"
        )
        lbl_welcome.pack(pady=10)

        lbl_sub = tk.Label(
            cover_frame, text="Chúng mình cùng nhau luyện đọc nhé!", 
            font=("Arial", 14), fg="#2d3436", bg="#d4edda"
        )
        lbl_sub.pack(pady=5)

        # Nút Bắt đầu lớn, bo tròn màu xanh lá nổi bật
        btn_start = tk.Button(
            cover_frame, text="BẮT ĐẦU", 
            font=("Arial", 16, "bold"), bg="#27ae60", fg="white",
            padx=30, pady=12, bd=0, cursor="hand2",
            command=self.create_topic_screen
        )
        btn_start.pack(pady=50)

    def create_topic_screen(self):
        self.clear_screen()
        
        lbl_title = tk.Label(self.root, text="🌟 Chọn Chủ Đề Bài Học 🌟", font=("Arial", 22, "bold"), fg="#d63031", bg="#f7f9fc")
        lbl_title.pack(pady=20)
        
        lbl_sub = tk.Label(self.root, text="Bé hãy chọn một chủ đề bên dưới nhé!", font=("Arial", 14), fg="#2d3436", bg="#f7f9fc")
        lbl_sub.pack(pady=10)

        frame_topics = tk.Frame(self.root, bg="#f7f9fc")
        frame_topics.pack(pady=20)

        topics_list = [
            (1, "🧑‍🤝‍🧑 Chủ đề 1: Tôi và các bạn"),
            (2, "🏠 Chủ đề 2: Mái ấm gia đình"),
            (3, "📚 Chủ đề 3: Bài học từ cuộc sống"),
            (4, "🌿 Chủ đề 4: Thiên nhiên kì thú")
        ]

        for topic_id, name in topics_list:
            btn = tk.Button(
                frame_topics, text=name, font=("Arial", 13, "bold"), 
                bg="white", fg="#2d3436", width=35, height=2, bd=2,
                cursor="hand2",
                command=lambda t=topic_id: self.open_lesson_screen(t)
            )
            btn.pack(pady=8)

    def open_lesson_screen(self, topic_id):
        self.current_lesson = lessons_data[topic_id]
        self.clear_screen()

        # Nút quay lại
        btn_back = tk.Button(self.root, text="⬅ Chọn chủ đề khác", font=("Arial", 11, "bold"), bg="#74b9ff", fg="white", command=self.create_topic_screen, cursor="hand2")
        btn_back.pack(anchor="w", padx=20, pady=10)

        # Tiêu đề bài học
        lbl_lesson_title = tk.Label(self.root, text=self.current_lesson["title"], font=("Arial", 18, "bold"), fg="#e17055", bg="#f7f9fc")
        lbl_lesson_title.pack(pady=5)

        # Hộp chứa nội dung văn bản
        self.txt_content = tk.Text(self.root, font=("Arial", 14), wrap=tk.WORD, width=65, height=6, bd=2)
        self.txt_content.pack(pady=10)
        self.txt_content.insert(tk.END, self.current_lesson["text"])
        self.txt_content.config(state=tk.DISABLED)

        # Nút hướng dẫn đọc
        btn_read = tk.Button(self.root, text="🔊 Hướng dẫn luyện đọc", font=("Arial", 12, "bold"), bg="#00b894", fg="white", padx=15, pady=5, cursor="hand2", command=self.play_audio)
        btn_read.pack(pady=10)

        # Phần trắc nghiệm mini-game
        lbl_q = tk.Label(self.root, text=f"❓ Câu hỏi: {self.current_lesson['question']}", font=("Arial", 12, "bold"), fg="#00796b", bg="#f7f9fc")
        lbl_q.pack(pady=10)

        frame_options = tk.Frame(self.root, bg="#f7f9fc")
        frame_options.pack(pady=5)

        for idx, opt_text in enumerate(self.current_lesson["options"]):
            btn_opt = tk.Button(
                frame_options, text=opt_text, font=("Arial", 11), bg="white", width=30,
                cursor="hand2",
                command=lambda i=idx: self.check_answer(i)
            )
            btn_opt.pack(pady=5)

    def play_audio(self):
        messagebox.showinfo("Hướng dẫn luyện đọc", "Bé hãy đọc to rõ ràng từng tiếng theo đoạn văn trên màn hình nhé!")

    def check_answer(self, selected_index):
        correct_index = self.current_lesson["correct"]
        if selected_index == correct_index:
            messagebox.showinfo("Kết quả", "🎉 Chính xác! Bé rất giỏi!")
        else:
            messagebox.showerror("Kết quả", "❌ Chưa đúng rồi, bé thử lại nhé!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HocLieuSoApp(root)
    root.mainloop()