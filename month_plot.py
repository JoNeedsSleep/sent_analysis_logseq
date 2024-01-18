from statistics import mean
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


from json_file import load_data

data = load_data('output.json')


average_scores_by_date = {}
for date, blocks in data.items():
    normalized_scores = [block['normalized_score'] for block in blocks.values()]
    average_scores_by_date[date] = mean(normalized_scores)

print(average_scores_by_date)

monthly_data = defaultdict(list)
for date_str, score in average_scores_by_date.items():
    year_month = datetime.strptime(date_str, "%Y_%m_%d").strftime("%Y-%m")
    monthly_data[year_month].append(score)
# Plotting
percentile_ranges = [-1.0, -0.7, -0.2, 0.2, 0.7, 1.0]
colors = ['#008000', '#ADFF2F', '#FFFF00', '#FFA500', '#FF0000']
fig, axis1 = plt.subplots(figsize=(25, 5))
axis2 = axis1.twinx()
meandemonths = []

for i, (year_month, values) in enumerate(monthly_data.items()):
    vsorted = sorted(values)
    prev_boundary_i = 0
    bottom = 0
    meanofthismonth = np.mean(values)
    meandemonths.append(meanofthismonth)

    for boundary in percentile_ranges[1:]:
        ib = np.searchsorted(vsorted, boundary)
        count = ib - prev_boundary_i
        percentage = count / len(values) * 100
        color = colors[percentile_ranges.index(boundary) - 1]
        axis1.bar(i, percentage, bottom=bottom, color=color)
        bottom += percentage
        prev_boundary_i = ib

axis2.plot(range(len(monthly_data)), meandemonths, 'ko-', alpha=0.5)
axis2.set_ylim(-1, 1)
ylim = axis1.get_ylim()
axis1.set_ylim(ylim[::-1])
plt.xticks(range(len(monthly_data)), monthly_data.keys(), rotation=45)

axis1.set_xlabel('Year_Month')
axis1.set_ylabel('Percentage')
axis2.set_ylabel('Mean Value')
plt.title('Logseq Journal Sentiment Analysis Percentile Analysis')

plt.show()