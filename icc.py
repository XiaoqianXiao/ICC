import pandas as pd
import pingouin as pg
import os
import csv
project_dir = '/Users/xiaoqianxiao/lab/R01/ICC'
results_dir = os.path.join(project_dir, 'results')
rater_dir = os.path.join(project_dir, 'rating')
# Read data
# List files and subdirectories
refer_dir = os.path.join(rater_dir, 'IRR_tapes_answer')
csv_files = [f for f in os.listdir(refer_dir) if f.endswith('.csv')]
print(csv_files)
all_results = []
for f in csv_files:
    refer_file = os.path.join(refer_dir, f)
    yuchen_file = os.path.join(rater_dir, 'Yuchen', f)
    df_refer = pd.read_csv(refer_file)
    df_Yuchen = pd.read_csv(yuchen_file)
    for i in df_refer.columns:
        print(i)
        data = pd.DataFrame({
            'Rater_refer': list(df_refer[i]),
            'Rater_Yuchen': list(df_Yuchen[i])
        })
        # Reshape the DataFrame to long format
        data_long = data.melt(var_name='Rater', value_name='Score')
        data_long['Target'] = list(range(1, data.shape[0] + 1)) * data.shape[1]
        # Compute ICC
        icc_result = pg.intraclass_corr(data=data_long, targets='Target', raters='Rater', ratings='Score', nan_policy='omit')
        # Display the result
        print(f"ICC results for {i}: {icc_result}")
        # save the results
        icc_3_1 = icc_result[icc_result['Type'] == 'ICC3']
        icc_3_1['Questionare'] = i
        all_results.append(icc_3_1)
final_results = pd.concat(all_results, ignore_index=True)
results_path = os.path.join(results_dir, 'icc.csv')
final_results.to_csv(results_path, index=False)
