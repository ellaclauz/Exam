import pandas as pd
import matplotlib.pyplot as plt
exam = pd.read_csv('exam_grades.csv')
exam_clean = exam.fillna(value = 0)
hist = exam_clean['grade'].hist(bins=20)
plt.show()
