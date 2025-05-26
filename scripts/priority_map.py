import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_priority(row):
    score = 0
    score += row['damage_level'] * 3
    score += row['survivors_detected'] * 5
    score += (1 - row['road_blocked']) * 2  # 1 if road is clear
    score -= row['distance_to_hospital'] * 0.1
    return score

def generate_priority_map(csv_path):
    df = pd.read_csv(csv_path)
    df['priority_score'] = df.apply(compute_priority, axis=1)

    grid_size = int(np.sqrt(len(df)))
    heatmap = df['priority_score'].values.reshape((grid_size, grid_size))

    plt.imshow(heatmap, cmap='hot', interpolation='nearest')
    plt.title("Priority Map")
    plt.colorbar(label="Priority Score")
    plt.show()

    return df

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        generate_priority_map(sys.argv[1])
    else:
        print("Usage: python priority_map.py <path_to_data.csv>")
