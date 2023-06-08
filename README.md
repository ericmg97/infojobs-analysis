# Analyze InfoJobs Offers

This project analyzes job offers from InfoJobs, a popular job search website in Spain. The project uses Python and several libraries to clean, analyze, and visualize the data.

## Requirements

To run this project, you need to have Python 3 and the following libraries installed:

- pandas
- tqdm
- JupyterLab
- matplotlib
- seaborn
- NLTK
- wordcloud

You can install these libraries using pip and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

To run the project, follow these steps:

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate
```

3. Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

4. Download the data from InfoJobs: (optional)

- In order to download the data, you need to have a developer account in InfoJobs. If you don't have one, you can create it for free in [InfoJobs Developer Site](https://developer.infojobs.net/).
- Once you have an account, create a file named `api-key.txt` in the root directory of the project, and add your credentials to it:

```bash
echo "YOUR_API_KEY" > api-key.txt
```

  > If you don't have an InfoJobs account, you can use the pre-downloaded data in the `data` directory.

1. Open the `analyze-infojobs-offers.ipynb` notebook in JupyterLab, and run the cells in order. The notebook will clean and analyze the data, and create visualizations.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details. The data is property of InfoJobs and is used for educational purposes only.

## Acknowledgments

This project was created for the Immune Tecnology Institute's Data Science Master. I would like to thank the following organizations for their resources and support:

- [InfoJobs](https://infojobs.net/)
- [Immune Tecnology Institute](https://www.immune.institute/)
