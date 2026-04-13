import turtle as t
import pandas as pd

# --- إعداد النافذة (Screen Setup) ---
screen = t.Screen()
screen.title("Map Game")
screen.bgcolor("black")
screen.bgpic("map.png")
screen.setup(width=858, height=515)

# --- إعدادات القلم (Turtle Settings) ---
t.hideturtle()
t.speed("fastest")
t.color("red")
t.pencolor("black")

# --- إدارة البيانات (Data Management) ---
data = pd.read_csv("countries.csv")
# تحويل عمود الدول إلى قائمة لسهولة التعامل
remaining_countries = data.country.tolist()
total_count = len(remaining_countries)
correct_guesses = []

# --- الحلقة الرئيسية للعبة (Main Game Loop) ---
while len(correct_guesses) < total_count:

    # طلب اسم الدولة من المستخدم وتنسيق النص (Capitalize first letter)
    user_input = screen.textinput(
        title=f"{len(correct_guesses)}/{total_count} Countries Correct",
        prompt="Type name of the country (or type 'Exit'):"
    )

    # التحقق من أن المستخدم لم يضغط على Cancel
    if user_input is None:
        break
        
    answer = user_input.title().strip()

    # خيار الخروج وحفظ الدول المتبقية
    if answer == "Exit":
        missing_data = [country for country in remaining_countries if country not in correct_guesses]
        if missing_data:
            df = pd.DataFrame(missing_data, columns=["Country"])
            df.to_csv("missing_countries.csv")
        break

    # التحقق من صحة الإجابة
    if answer in remaining_countries and answer not in correct_guesses:
        # إضافة الإجابة لقائمة الإجابات الصحيحة
        correct_guesses.append(answer)
        
        # استخراج الإحداثيات من ملف البيانات
        country_row = data[data["country"] == answer]
        x_coord = int(country_row.x.item())
        y_coord = int(country_row.y.item())

        # التحرك للموقع ورسم العلامة والكتابة
        t.penup()
        t.goto(x_coord, y_coord)
        t.begin_fill()
        t.circle(20) # حجم الدائرة (تم تصغيره قليلاً ليكون أنسب)
        t.end_fill()
        t.write(answer, align="center", font=("Arial", 11, "bold"))

    else:
        # في حالة الإجابة الخاطئة أو المكررة، ننتقل للدورة التالية
        continue
