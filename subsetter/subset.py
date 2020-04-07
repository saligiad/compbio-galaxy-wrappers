import pandas as pd

# Read the cohort file
data = pd.read_csv("$cohort", sep="\t")
data_headers = data.columns.copy()

# Merge annotation file, if specified
#if $annotations.use_annotations == "use"
annotations = pd.read_csv("$annotations.ann_file", sep="\t")
data = data.merge(right=annotations, how="inner",
                  left_on="$annotations.cohort_key",
                  right_on="$annotations.ann_key")
#end if

# Filter the cohort using the column/value pairs provided in the inputs
columns = "$columns".split(',')
values = "$values".split(',')
#if $filter == "keep_values"
for c, v in zip(columns, values):
    data = data.loc[data[c]==v,:]
#else if $filter == "filter_values"
for c, v in zip(columns, values):
    data = data.loc[data[c]!=v,:]
#end if

# Prepare the final dataframe and write the file
#if $annotations.use_annotations == "use" and not $annotations.keep_cols
data = data[data_headers]
#end if
data.to_csv(path="filtered.tsv", sep="\t", header=True, index=False)

