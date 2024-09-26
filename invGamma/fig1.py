import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma, invgamma

# パラメータの設定
params = [
    (2, 3),
    (5, 2),
    (1, 5),
    (3, 1)
]

# x軸の範囲
x = np.linspace(0, 6, 400)

# プロットの作成
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

for i, (alpha, beta) in enumerate(params):
    row = i // 2
    col = i % 2

    # ガンマ分布
    gamma_pdf = gamma.pdf(x, a=alpha, scale=1/beta)
    axes[row, col].plot(x, gamma_pdf, label=f"Gamma (α={alpha}, β={beta})")

    # 逆ガンマ分布
    invgamma_pdf = invgamma.pdf(x, a=alpha, scale=beta)
    axes[row, col].plot(x, invgamma_pdf, label=f"Inv. Gamma (α={alpha}, β={beta})")

    axes[row, col].set_title(f"α={alpha}, β={beta}")
    axes[row, col].set_xlabel("x")
    axes[row, col].set_ylabel("Probability Density")
    axes[row, col].grid()
    axes[row, col].legend()

plt.tight_layout()
plt.show()
