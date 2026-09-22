import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

notebooks = {
    '1 - Missing Data.ipynb': [
        'Import numpy and pandas for array and DataFrame operations',
        'Example tuple of Python falsy values to show empties',
        'Check if any value in falsy_values is truthy (boolean any)',
        'Show numpy nan constant (numeric missing marker)',
        'Demonstrate NaN propagation with arithmetic',
        'Create numpy array containing NaN values',
        'Sum the array to show NaN effect on aggregation',
        'Compute the mean of the array (NaN effect)',
        'Show that None differs from NaN (raises on arithmetic)',
        'Create float array where None is coerced to NaN',
        'Display the array to inspect NaN positions',
        'Recreate array with NaNs for further demos',
        'Compute mean again to show NaN impact',
        'Compute sum again to show NaN propagation',
        'Show numpy infinity constant',
        'Arithmetic with infinity example',
        'Divide infinity by a number (infinite arithmetic)',
        'Divide inf by inf (undefined -> NaN)',
        'Create array mixing finite, inf and NaN',
        'Sum array with inf/NaN to show aggregation result',
        'Check np.isnan on a NaN value (element-wise test)',
        'Check np.isinf on an infinite value (element-wise test)',
        'Use np.isfinite to test for finite numbers',
        'np.isnan on array returns boolean mask of NaNs',
        'np.isinf on array returns boolean mask of infinities',
        'np.isfinite on array returns True only for finite numbers',
        'Recreate array with NaNs to demonstrate filtering',
        'Filter out NaNs using boolean mask (~np.isnan(a))',
        'Equivalent selection using np.isfinite(a)',
        'Sum only finite values (avoid NaN/Inf propagation)',
        'Mean only finite values (ignoring NaN/Inf)'
    ],
    '2 - Handling Missing Data with Pandas.ipynb': [
        'Import numpy and pandas for pandas missing-data examples',
        'pandas: pd.isnull(np.nan) detects NaN',
        'pd.isnull(None) shows None is treated as NA',
        'pd.isna(np.nan) alias of isnull',
        'pd.isna(None) shows None is NA',
        'pd.notnull(None) opposite of isnull',
        'pd.notnull(np.nan) shows NaN is missing',
        'pd.notna(np.nan) alias for notnull',
        'pd.notnull(3) non-missing scalar detection',
        'pd.isnull on a Series returns boolean mask',
        'pd.notnull on a Series returns boolean mask of non-missing',
        'pd.isnull on a DataFrame marks missing entries',
        'Series.count() counts non-NA values',
        'Series.sum() sums ignoring NaNs',
        'Series.mean() computes mean ignoring NaNs',
        'Create example Series s with NaNs for demos',
        'pd.notnull(s) boolean Series of non-missing',
        'pd.isnull(s) boolean Series of missing',
        'pd.notnull(s).sum() count non-missing entries',
        'pd.isnull(s).sum() count missing entries',
        's[pd.notnull(s)] filter Series to keep non-missing',
        's.isnull() Series method for missing mask',
        's.notnull() Series method for non-missing mask',
        's[s.notnull()] filter using Series method',
        'Show the example Series s',
        "s.fillna(0)",
        's.fillna(s.mean())',
        'Show original Series (no inplace change)',
        "s.fillna(method='ffill')",
        "s.fillna(method='bfill')",
        "pd.Series([np.nan, 3, np.nan, 9]).fillna(method='ffill')",
        "pd.Series([1, np.nan, 3, np.nan, np.nan]).fillna(method='bfill')",
        "Create example DataFrame df with NaNs",
        'Display df',
        'Show df.shape (rows, columns)',
        'df.info() summary of DataFrame',
        'df.isnull() boolean DataFrame showing NaNs',
        'df.isnull().sum() count NaNs per column',
        'df.dropna() drop rows containing any NaN',
        "df.dropna(axis=1) drop columns containing any NaN",
        'Create df2 to demo dropna how parameter',
        'Display df2',
        "df.dropna(how='all') drop rows only if all values are NaN",
        "df.dropna(how='any') drop rows with any NaN",
        'Show df again',
        'df.dropna(thresh=3) keep rows with >=3 non-NaN',
        "df.dropna(thresh=3, axis='columns') keep columns with >=3 non-NaN",
        's.dropna().count() count after dropping NaNs',
        'missing_values = len(s.dropna()) != len(s) boolean missing check',
        'len(s) total elements',
        's.count() count non-NaN values',
        'missing_values = s.count() != len(s) missing check using count',
        'pd.Series([True, False, False]).any() any example',
        'pd.Series([True, False, False]).all() all example',
        'pd.Series([True, True, True]).all() all True example',
        's.isnull() boolean mask of missing values',
        'pd.Series([1, np.nan]).isnull().any() check any NaNs',
        'pd.Series([1, 2]).isnull().any() check false when no NaNs',
        's.isnull().any() check if s has any NaN',
        's.isnull().values underlying boolean array',
        's.isnull().values.any() strict numpy any check'
    ],
    '3 - Cleaning Not Null Values.ipynb': [
        'Import numpy and pandas for examples',
        'Create DataFrame demonstrating invalid (not-missing) values',
        "df['Sex'].unique() list unique values to spot invalid categories",
        "df['Sex'].value_counts() frequency counts to see common values",
        "df['Sex'].replace('D','F') replace single invalid value",
        "df['Sex'].replace({'D':'F','N':'M'}) replace multiple values",
        'df.replace({...}) replace values across DataFrame by column',
        "df[df['Age'] > 100] find ages exceeding credibility threshold",
        "df.loc[df['Age'] > 100, 'Age'] = ... scale suspicious ages",
        'df display after cleaning',
        'Create ambassadors Series to demonstrate duplicates',
        'Display ambassadors',
        'ambassadors.duplicated() boolean mask for duplicates',
        "ambassadors.duplicated(keep='last') mark duplicates keeping last",
        "ambassadors.duplicated(keep=False) mark all occurrences as duplicates",
        'ambassadors.drop_duplicates() drop duplicate values',
        "ambassadors.drop_duplicates(keep='last') drop duplicates keeping last",
        "ambassadors.drop_duplicates(keep=False) drop all duplicates",
        'Create players DataFrame showing row-level duplicates',
        'Display players DataFrame',
        'players.duplicated() show duplicated rows',
        "players.duplicated(subset=['Name']) duplicated by Name only",
        "players.duplicated(subset=['Name'], keep='last') keep last duplicate",
        'players.drop_duplicates() drop duplicated rows',
        "players.drop_duplicates(subset=['Name']) drop duplicates by Name",
        "players.drop_duplicates(subset=['Name'], keep='last') drop keep last",
        "df = pd.DataFrame({'Data': [...]}) messy concatenated text column",
        'Display raw concatenated column',
        "df['Data'].str.split('_') split strings into lists by underscore",
        "df['Data'].str.split('_', expand=True) split into separate columns",
        "df = df['Data'].str.split('_', expand=True) replace with expanded cols",
        "df.columns = ['Year','Sex','Country','No Children'] name new columns",
        'df display cleaned columns',
        "df['Year'].str.contains('\\?') detect uncertain years marked with ?",
        "df['Country'].str.contains('U') example text containment",
        "df['Country'].str.strip() remove surrounding whitespace",
        "df['Country'].str.replace(' ', '') remove internal spaces",
        "df['Year'].str.replace(r'(?P<year>\\d{4})\\?', lambda m: m.group('year')) regex remove ?"
    ],
    '4 - More Visualizations.ipynb': [
        'Import numpy, pandas and matplotlib and enable inline plotting',
        'x = np.arange(-10,11) create x values for plotting',
        "Create figure and plot two curves using pyplot API",
        "Create figure with two subplots showing lines and labels",
        'Create OOP-style figure and axes via subplots()',
        'Use axes.plot to draw lines with styles, markers and legend',
        'Plot multiple lines showing linestyle variations',
        "Plot lines with color/marker shorthand and show legend",
        "Print available marker symbols (inspect matplotlib options)",
        "Show some example line styles",
        "Create subplots object and plot a simple line",
        "Create 2x2 subplot grid and return figure and axes",
        "Fill 2x2 grid with random data plots as examples",
        "Demonstrate subplot2grid layout positioning",
        "Prepare random data for scatter plot (positions/colors/sizes)",
        "Scatter plot with color mapping and colorbar",
        "Side-by-side scatter plots with different colormaps",
        "Sample data for histogram examples",
        "Plot a histogram with many bins and styling",
        "Save a figure to 'hist.png'",
        "Compute KDE using scipy gaussian_kde",
        "Plot KDE as line and filled area",
        "Combine histogram and KDE on same axes",
        "Create bar plot data arrays Y and Y2",
        "Plot a single bar chart with Y",
        "Plot stacked bars with Y and Y2 and add legend",
        "Create values with synthetic outliers for boxplot demo",
        "Plot histogram of values to see distribution including outliers",
        "Plot boxplot to detect outliers visually"
    ],
    '5 - Real Example.ipynb': [
        'Import pandas, numpy, seaborn and matplotlib and enable inline plotting',
        'Read CSV of Bitcoin and Ether prices, parse dates and set index',
        'df.head() show first rows to inspect dataset',
        "df.plot(figsize=(16,9)) visualize time series to spot issues",
        "Zoom into date range for Ether to inspect potential missing data",
        "Slice suspicious window into df_na for focused checks",
        "Check if Ether has any NaNs in the slice",
        "Show rows where Ether is NaN (find missing timestamps)",
        "Show slightly bigger window for context", 
        "Show backfilled values as a potential fill strategy",
        "Apply backfill to entire DataFrame inplace",
        "Plot after filling missing data to inspect result",
        "Plot focused ranges to visually identify large spikes/outliers",
        "Drop specific dates identified as outliers and create df_cleaned",
        "Plot dataset after removing outlier dates",
        "df.mean() compute mean (sensitive to outliers)",
        "df_cleaned.mean() mean after removing outliers",
        "df.median() compute median (robust)",
        "Plot Ether histogram to inspect distribution",
        "Seaborn distplot for Ether (histogram + KDE)",
        "Seaborn distplot for Bitcoin with rugplot",
        "KDE and rugplot separately for detailed view",
        "Cumulative distribution plotting with distplot cumulative=True",
        "Jointplot bivariate distribution with marginals",
        "Regplot scatter with regression fit",
        "Compute 20th quantile for Bitcoin",
        "Plot cumulative and mark 0.2 quantile line",
        "Compute median via quantile .5",
        "Compute median via median()",
        "Compute and plot quantile lines for visualization",
        "Compute range (max-min) sensitive to outliers",
        "Range after cleaning for comparison",
        "Variance example (sensitive to outliers)",
        "Standard deviation example",
        "Std after cleaning for comparison",
        "IQR for raw data (Q3-Q1)",
        "IQR for cleaned data (Q3-Q1)",
        "Compute Z-score based upper/lower limits using mean ± 2*std",
        "Print the calculated upper and lower limits",
        "Plot distribution and vertical lines at Z-score limits",
        "Compute IQR-based limits and plot vertical lines",
        "Use analytical upper limit to filter and plot data",
        "Drop rows above upper limit and plot result"
    ]
}


def add_comments(nb_path, comments):
    data = json.loads(nb_path.read_text(encoding='utf-8'))
    changed = False
    code_idx = 0
    for cell in data.get('cells', []):
        if cell.get('cell_type') == 'code':
            if code_idx < len(comments):
                comment = '# ' + comments[code_idx] + '\n'
            else:
                comment = '# (no specific hint provided)\n'
            src = cell.get('source', [])
            if not src:
                src = [comment]
                cell['source'] = src
                changed = True
            else:
                first = src[0]
                if isinstance(first, str) and first.lstrip().startswith('#'):
                    # already commented: skip
                    pass
                else:
                    src.insert(0, comment)
                    cell['source'] = src
                    changed = True
            code_idx += 1
    if changed:
        nb_path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding='utf-8')
    return changed


def main():
    for nb_name, comments in notebooks.items():
        path = BASE / nb_name
        if not path.exists():
            print(f'Skipping missing notebook: {nb_name}')
            continue
        changed = add_comments(path, comments)
        print(f'Updated {nb_name}: changed={changed}')


if __name__ == '__main__':
    main()
