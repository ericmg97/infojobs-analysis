import requests
import pandas as pd
import tqdm
import os

def get_infojobs_datasets(api_key, path='data/'):
    """
    Get the jobs dataset from InfoJobs API and save it to a CSV file.

    Parameters
    ----------
    api_key : str
        The API key to access the InfoJobs API.
    path : str, optional
        The path to save the CSV files. The defaults are 'data/jobs_dataset.csv' and 'data/country_dataset.csv'.

    Returns
    -------
    None. Saves the datasets to CSV files.

    """

    # Set the Authentification Header for InfoJobs API
    headers = {
        'Authorization': api_key
    }

    # Create the directory if it doesn't exist
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Create the paths to the CSV files
    jobs_dataset_path = os.path.join(path, 'jobs_dataset.csv')
    country_dataset_path = os.path.join(path, 'country_dataset.csv')
    
    # Check if the datasets are already cached
    try:
        df = pd.read_csv(jobs_dataset_path)
        print('\nThe jobs dataset is already cached')
    except FileNotFoundError:
        print('\nGetting the jobs dataset from InfoJobs API...')

        # Get the first page of the dataset
        r = requests.get('https://api.infojobs.net/api/9/offer', headers=headers, params={'page': 1, 'maxResults': '50'})

        # Convert the response to JSON
        first_json = r.json()

        # Create a list with all the data
        all_data = first_json['offers']

        # Set up the progress bar
        progress_bar = tqdm.tqdm(total=first_json['totalResults'], unit='offers')

        for page in range(1, first_json['totalResults']//50 + 2):
            # Get the dataset from InfoJobs API
            r = requests.get('https://api.infojobs.net/api/9/offer', headers=headers, params={'page': page, 'maxResults': '50', 'country': 'espana'})

            # Convert the response to JSON
            json = r.json()

            try:
                # Add the data to the dictionary
                all_data += json['offers']
            except KeyError:
                page -= 1
                continue

            # Update the progress bar
            progress_bar.update(len(json['offers']))
        
        # Close the progress bar
        progress_bar.close()

        # Create a DataFrame with all the data
        df = pd.DataFrame(all_data)

        # Save the DataFrame to a CSV file
        df.to_csv(jobs_dataset_path, index=False)

        print(f'The dataset has been saved to {jobs_dataset_path}\n')

    
    try:
        df = pd.read_csv(country_dataset_path)
        print('\nThe country dataset is already cached')
    except FileNotFoundError:
        print('\nGetting the country dataset from InfoJobs API...')
        r = requests.get('https://api.infojobs.net/api/1/dictionary/country', headers=headers, params={'page': 1, 'maxResults': '50'})

        # Convert the response to JSON and create a the dataset
        df = pd.DataFrame(r.json())

        # Save the dataset to a CSV file
        df.to_csv(country_dataset_path, index=False)

        print(f'The dataset has been saved to {country_dataset_path}\n')

if __name__ == '__main__':
    # Get the private API key
    with open('api-key.txt', 'r') as file:
        api_key = file.read()

    # Get the jobs dataset from InfoJobs API and save it to a CSV file
    get_infojobs_datasets(api_key)