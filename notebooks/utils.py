import ast
import seaborn as sns
import matplotlib.pyplot as plt

def take_value_from_dict(x, key = 'value'):
    """
    Take the value of a key from a JSON string.

    Parameters
    ----------
    x : str
        The JSON string.

    key : str, optional
        The key of the value to take. The default is 'value'.
    
    Returns
    -------
    value : str
        The value of the key.
    """
    try:
        value = ast.literal_eval(x)[key]
    except ValueError:
        value = None

    return value if value != '' else None

def transform_salary_float(value):
    """
    Transform a salary value to float.

    Parameters
    ----------
    value : str
        The salary value.

    Returns
    -------
    float
        The salary value as float.
    """

    value = take_value_from_dict(value)

    if value is not None:
        return float(value.replace('.', '').replace(',', '.').replace('€', '').strip())
    else:
        return value

def update_salary_range(df):
    """
    Update the salary range of a job offer.

    Parameters
    ----------
    df : DataFrame
        The DataFrame with the job offer.

    Returns
    -------
    df : DataFrame
        The DataFrame with the updated salary range.
    """
    
    mult = 1
    if df.salaryPeriod == 'Bruto/mes':
        mult = 12
    elif df.salaryPeriod == 'Bruto/día':
        mult = 225
    elif df.salaryPeriod == 'Bruto/hora':
        mult = 1800

    df.salaryMin *= mult
    df.salaryMax *= mult

    return df
    
def plot_salary_outliers(df, group_by = 'category'):
    """
    Plot the outliers of a DataFrame.

    Parameters
    ----------
    df : DataFrame
        The DataFrame to plot.
    
    group_by : str, optional
        The column to group by. The default is 'category'.
    
    Returns
    -------
    Plot
        The plot of the outliers.
    """

    sns.set_theme(style="darkgrid")
    
    # Create a figure with two subfigures the figure size is 16x9
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9))

    sns.boxplot(x='salaryMin', y=group_by, data=df, ax=ax1,)

    ax1.set_title('Salary Min by Category')
    ax1.set_xlabel('Salary Min')
    ax1.set_ylabel(group_by)

    # disable y_values in the second subfigure
    sns.boxplot(x='salaryMax', y=group_by, data=df, ax=ax2)

    ax2.set_yticklabels([])
    ax2.set_ylabel('')
    ax2.set_title('Salary Max by Category')
    ax2.set_xlabel('Salary Max')

    # show the figure
    plt.show()

def plot_salary_heatmap(df, group_by = 'Province', title = 'Salary Heatmap'):
    """
    Plot a heatmap of the average salary by 'group_by' and salaryMin and salaryMax

    Parameters
    ----------
    df : DataFrame
        DataFrame with the data to plot
    group_by : str, optional
        Column to group by, by default 'Province'
    title : str, optional
        Title of the plot, by default 'Salary Heatmap'
        
    Returns
    -------
    Plot
        Heatmap of the average salary by 'group_by' and salaryMin and salaryMax
    """

    plt.suptitle(title, fontsize=16)

    ax1 = plt.subplot(1, 2, 1)
    ax2 = plt.subplot(1, 2, 2)

    heatmap1 = df.drop(columns=['salaryMax'])
    heatmap2 = df.drop(columns=['salaryMin'])

    sns.heatmap(data=heatmap1, cmap='Blues', ax=ax1)

    ax1.set_xlabel('Salary Min')
    ax1.set_ylabel(group_by)
    ax1.set_xticklabels([])

    sns.heatmap(data=heatmap2, cmap='Blues', ax=ax2)

    ax2.set_xlabel('Salary Max')
    ax2.set_ylabel('')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])

    plt.show()