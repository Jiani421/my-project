#!/usr/bin/env python3
"""BMI Calculator — supports both metric and imperial units."""


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("Weight and height must be positive values.")
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight (偏瘦)"
    elif bmi < 24.0:
        return "Normal weight (正常)"
    elif bmi < 28.0:
        return "Overweight (偏重)"
    else:
        return "Obese (肥胖)"


def get_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  请输入正数。")
                continue
            return value
        except ValueError:
            print("  输入无效，请输入数字。")


def main():
    print("=" * 40)
    print("       BMI 体重指数计算器")
    print("=" * 40)
    print("单位制 / Unit system:")
    print("  1. 公制 (kg / cm)")
    print("  2. 英制 (lbs / inches)")
    choice = input("请选择 (1/2): ").strip()

    if choice == "2":
        weight_lbs = get_float("体重 Weight (lbs): ")
        height_in = get_float("身高 Height (inches): ")
        weight_kg = weight_lbs * 0.453592
        height_m = height_in * 0.0254
    else:
        weight_kg = get_float("体重 Weight (kg): ")
        height_cm = get_float("身高 Height (cm): ")
        height_m = height_cm / 100

    bmi = calculate_bmi(weight_kg, height_m)
    category = classify_bmi(bmi)

    print("\n" + "-" * 40)
    print(f"  BMI 指数: {bmi:.1f}")
    print(f"  分类:     {category}")
    print("-" * 40)
    print("参考标准 (中国标准):")
    print("  < 18.5   偏瘦")
    print("  18.5–24  正常")
    print("  24–28    偏重")
    print("  ≥ 28     肥胖")
    print("=" * 40)


if __name__ == "__main__":
    main()
